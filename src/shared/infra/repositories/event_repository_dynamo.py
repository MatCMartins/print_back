from typing import List, Optional

from src.shared.domain.entities.event import Event
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.event_dynamo_dto import EventDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class EventRepositoryDynamo(IEventRepository):

    @staticmethod
    def partition_key_format(event_id: str) -> str:
        return f"event#{event_id}"

    @staticmethod
    def sort_key_format(event_id: str) -> str:
        return f"#{event_id}"

    def __init__(self):
        # Atualiza para usar a tabela específica do DynamoDB para "Event"
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_tables["EVENT"],  # Usa a tabela de eventos
            region=Environments.get_envs().region
        )

    def get_event(self, event_id: str) -> Event:
        resp = self.dynamo.get_item(
            partition_key=self.partition_key_format(event_id),
            sort_key=self.sort_key_format(event_id)
        )

        if resp.get('Item') is None:
            raise NoItemsFound("event_id")

        event_dto = EventDynamoDTO.from_dynamo(resp["Item"])
        return event_dto.to_entity()

    def get_all_events(self) -> List[Event]:
        resp = self.dynamo.get_all_items()
        events = []
        for item in resp.get('Items', []):
            if item.get("entity") == 'event':
                events.append(EventDynamoDTO.from_dynamo(item).to_entity())

        return events

    def create_event(self, new_event: Event) -> Event:
        event_dto = EventDynamoDTO.from_entity(new_event)
        self.dynamo.put_item(
            partition_key=self.partition_key_format(new_event.event_id),
            sort_key=self.sort_key_format(new_event.event_id),
            item=event_dto.to_dynamo()
        )
        return new_event

    def delete_event(self, event_id: str) -> Event:
        resp = self.dynamo.delete_item(
            partition_key=self.partition_key_format(event_id),
            sort_key=self.sort_key_format(event_id)
        )

        if "Attributes" not in resp:
            raise NoItemsFound("event_id")

        return EventDynamoDTO.from_dynamo(resp['Attributes']).to_entity()

    def update_event(
        self,
        event_id: str,
        new_name: Optional[str] = None,
        new_description: Optional[str] = None,
        new_banner: Optional[str] = None,
        new_start_date: Optional[int] = None,
        new_end_date: Optional[int] = None,
        new_rooms: Optional[dict] = None,
        new_subscribers: Optional[dict] = None
    ) -> Event:
        item_to_update = {}

        if new_name is not None:
            item_to_update['name'] = new_name
        if new_description is not None:
            item_to_update['description'] = new_description
        if new_banner is not None:
            item_to_update['banner'] = new_banner
        if new_start_date is not None:
            item_to_update['start_date'] = new_start_date
        if new_end_date is not None:
            item_to_update['end_date'] = new_end_date
        if new_rooms is not None:
            item_to_update['rooms'] = new_rooms
        if new_subscribers is not None:
            item_to_update['subscribers'] = new_subscribers

        if not item_to_update:
            raise NoItemsFound("Nothing to update")

        resp = self.dynamo.update_item(
            partition_key=self.partition_key_format(event_id),
            sort_key=self.sort_key_format(event_id),
            update_dict=item_to_update
        )

        return EventDynamoDTO.from_dynamo(resp['Attributes']).to_entity()
