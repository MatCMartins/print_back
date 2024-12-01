from src.shared.domain.entities.notification import Notification
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_Notifications:
    def test_student_organization(self):
        Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", title="Teste", description="Lorem ipsum", creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])
        
    def test_notification_id_is_None(self):
        with pytest.raises(EntityError):
            Notification(notification_id=None, title="Teste", description="Lorem ipsum", creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])

    def test_notification_id_is_wrong_length(self):
        with pytest.raises(EntityError):
            Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c7749", title="Teste", description="Lorem ipsum", creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])
    
    def test_title_is_none(self):
        with pytest.raises(EntityError):
            Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c7749", title=None, description="Lorem ipsum", creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])

    def test_description_is_none(self):
        with pytest.raises(EntityError):
            Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c7749", title="Teste", description=None, creation_date=28394930, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])
    
    def test_creation_date_is_none(self):
        with pytest.raises(EntityError):
            Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c7749", title="Teste", description="Lorem ipsum", creation_date=None, has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"])

    def test_has_seen_is_none(self):
        with pytest.raises(EntityError):
            Notification(notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c7749", title="Teste", description="Lorem ipsum", creation_date=28394930, has_seen=None)

