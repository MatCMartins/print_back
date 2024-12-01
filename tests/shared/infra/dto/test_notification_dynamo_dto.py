from src.shared.domain.entities.notification import Notification
from src.shared.domain.enums.state_enum import STATE
from src.shared.infra.dto.notification_dynamo_dto import NotificationDynamoDTO
# from src.shared.infra.repositories.notificationn_repository_mock import NotificationRepositoryMock


                                

class Test_NotificationDynamoDTO:
    def test_from_entity(self):
        repo = Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", title="Teste", description="Lorem ipsum", creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])


        notification_dto = NotificationDynamoDTO.from_entity(notification=repo)

        expected_notification_dto = NotificationDynamoDTO(
            notification_id=repo.notification_id,
            title=repo.title,
            description=repo.description,
            creation_date=repo.creation_date,
            has_seen=repo.has_seen
        )

        assert notification_dto == expected_notification_dto

    def test_to_dynamo(self):
        repo = Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", title="Teste", description="Lorem ipsum", creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])

        notification_dto = NotificationDynamoDTO(
            notification_id=repo.notification_id,
            title=repo.title,
            description=repo.description,
            creation_date=repo.creation_date,
            has_seen=repo.has_seen
        )

        notification_dynamo = notification_dto.to_dynamo()

        expected_dict = {
            "entity": "notification",
            "notification_id": repo.notification_id,
            "title": repo.title,
            "description": repo.description,
            "creation_date": repo.creation_date,
            "has_seen": repo.has_seen
        }

        assert notification_dynamo == expected_dict

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'notification_id': '1234',
                                'title': 'mateus',
                                'SK': '#' + str(1234),
                                'PK': 'notification#' + str(1234),
                                'entity': 'notification',
                                'description': 'description',
                                'creation_date': 1234,
                                'has_seen': ['1234']
                                }}

        notification_dto = NotificationDynamoDTO.from_dynamo(notification_data=dynamo_dict["Item"])

        expected_notification_dto = NotificationDynamoDTO(
            notification_id='1234',
            title='mateus',
            description='description',
            creation_date=1234,
            has_seen=['1234']
        )

        assert notification_dto == expected_notification_dto

    def test_to_entity(self):
        repo = Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", title="Teste", description="Lorem ipsum", creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])

        notification_dto = NotificationDynamoDTO(
            notification_id=repo.notification_id,
            title=repo.title,
            description=repo.description,
            creation_date=repo.creation_date,
            has_seen=repo.has_seen
        )

        notification = notification_dto.to_entity()

        assert notification.title == repo.title
        assert notification.description == repo.description
        assert notification.creation_date == repo.creation_date
        assert notification.has_seen == repo.has_seen

    def test_from_dynamo_to_entity(self):
        dynamo_item = {'Item': {'notification_id': 'b9799d9d-798c-4f44-9fd7-b9ae41c77496',
                                'title': 'mateus',
                                'SK': '#' + str("b9799d9d-798c-4f44-9fd7-b9ae41c77496"),
                                'PK': 'notification#' + str("b9799d9d-798c-4f44-9fd7-b9ae41c77496"),
                                'entity': 'notification',
                                'description': 'description',
                                'creation_date': 1234,
                                'has_seen': ['1234']
                                }}

        notification_dto = NotificationDynamoDTO.from_dynamo(notification_data=dynamo_item["Item"])

        notification = notification_dto.to_entity()

        expected_notification = Notification(
            notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            title='mateus',
            description='description',
            creation_date=1234,
            has_seen=['1234'],
        )

        assert notification.title == expected_notification.title
        assert notification.description == expected_notification.description
        assert notification.creation_date == expected_notification.creation_date
        assert notification.has_seen == expected_notification.has_seen


    def test_from_entity_to_dynamo(self):
        repo = Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", title="Teste", description="Lorem ipsum", creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])

        notification_dto = NotificationDynamoDTO.from_entity(notification=repo)

        notification_dynamo = notification_dto.to_dynamo()

        expected_dict = {
            "entity": "notification",
            "notification_id": repo.notification_id,
            "title": repo.title,
            "description": repo.description,
            "creation_date": repo.creation_date,
            "has_seen": repo.has_seen
        }

        assert notification_dynamo == expected_dict
