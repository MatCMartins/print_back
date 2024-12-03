from typing import List, Optional

from src.shared.domain.entities.notification import Notification
from src.shared.domain.repositories.notification_repository_interface import INotificationRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.notification_dynamo_dto import NotificationDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class NotificationRepositoryDynamo(INotificationRepository):

    @staticmethod
    def partition_key_format(notification_id: str) -> str:
        return f"notification#{notification_id}"

    @staticmethod
    def sort_key_format(notification_id: str) -> str:
        return f"#{notification_id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_tables["NOTIFICATION"],  # Usa a tabela de notificacoes
            region=Environments.get_envs().region,
            partition_key="PK",
            sort_key="SK" 
        )

    def get_notification(self, notification_id: str) -> Notification:
        resp = self.dynamo.get_item(
            partition_key=self.partition_key_format(notification_id),
            sort_key=self.sort_key_format(notification_id)
        )

        if resp.get('Item') is None:
            raise NoItemsFound("notification_id")

        notification_dto = NotificationDynamoDTO.from_dynamo(resp["Item"])
        return notification_dto.to_entity()

    def get_all_notifications(self) -> List[Notification]:
        resp = self.dynamo.get_all_items()
        notification = []
        for item in resp.get('Items', []):
            if item.get("entity") == 'notification':
                notification.append(NotificationDynamoDTO.from_dynamo(item).to_entity())

        return notification

    def create_notification(self, new_notification: Notification) -> Notification:
        notification_dto = NotificationDynamoDTO.from_entity(notification=new_notification)
        self.dynamo.put_item(
            partition_key=self.partition_key_format(new_notification.notification_id),
            sort_key=self.sort_key_format(new_notification.notification_id),
            item=notification_dto.to_dynamo()
        )
        return new_notification

    def delete_notification(self, notification_id: str) -> Notification:
        resp = self.dynamo.delete_item(
            partition_key=self.partition_key_format(notification_id),
            sort_key=self.sort_key_format(notification_id)
        )

        if "Attributes" not in resp:
            raise NoItemsFound("notification_id")

        return NotificationDynamoDTO.from_dynamo(resp['Attributes']).to_entity()

    def update_notification(
        self,
        notification_id: str,
        new_name: Optional[str] = None,
        new_description: Optional[str] = None,
        new_creation_date: Optional[int] = None,
        new_has_seen: Optional[list] = None
    ) -> Notification:
        item_to_update = {}

        if new_name is not None:
            item_to_update['title'] = new_name
        if new_description is not None:
            item_to_update['description'] = new_description
        if new_creation_date is not None:
            item_to_update['creation_date'] = new_creation_date
        if new_has_seen is not None:
            item_to_update['has_seen'] = new_has_seen

        if not item_to_update:
            raise NoItemsFound("Nothing to update")

        resp = self.dynamo.update_item(
            partition_key=self.partition_key_format(notification_id),
            sort_key=self.sort_key_format(notification_id),
            update_dict=item_to_update
        )

        return NotificationDynamoDTO.from_dynamo(resp['Attributes']).to_entity()
