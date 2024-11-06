import pytest
from src.shared.domain.entities.event import event
from src.shared.helpers.errors.domain_errors import EntityError

class TestEvent:
    def test_event_creation_successful(self):
        event_instance = event(
            name="Tech Conference 2024",
            description="A conference for tech enthusiasts.",
            creation_date=1612137600,
            banner="https://example.com/banner.png",
            start_date=1612238400,
            end_date=1612324800,
            rooms={"Main Hall": 100, "Workshop Area": 50},
            subscribers={"24.00000-0": "Main Hall", "25.00000-1": "Workshop Area"}
        )
        assert event_instance.name == "Tech Conference 2024"
        assert event_instance.event_id is not None

    def test_name_is_none(self):
        with pytest.raises(EntityError, match="Invalid name"):
            event(
                name=None,
                description="A conference for tech enthusiasts.",
                creation_date=1612137600,
                banner="https://example.com/banner.png",
                start_date=1612238400,
                end_date=1612324800,
                rooms={"Main Hall": 100},
                subscribers={"24.00000-0": "Main Hall"}
            )

    def test_description_is_none(self):
        with pytest.raises(EntityError, match="Invalid description"):
            event(
                name="Tech Conference 2024",
                description=None,
                creation_date=1612137600,
                banner="https://example.com/banner.png",
                start_date=1612238400,
                end_date=1612324800,
                rooms={"Main Hall": 100},
                subscribers={"24.00000-0": "Main Hall"}
            )

    def test_creation_date_is_not_int(self):
        with pytest.raises(EntityError, match="Invalid creation_date"):
            event(
                name="Tech Conference 2024",
                description="A conference for tech enthusiasts.",
                creation_date="1612137600",
                banner="https://example.com/banner.png",
                start_date=1612238400,
                end_date=1612324800,
                rooms={"Main Hall": 100},
                subscribers={"24.00000-0": "Main Hall"}
            )

    def test_banner_is_not_str(self):
        with pytest.raises(EntityError, match="Invalid banner"):
            event(
                name="Tech Conference 2024",
                description="A conference for tech enthusiasts.",
                creation_date=1612137600,
                banner=123,
                start_date=1612238400,
                end_date=1612324800,
                rooms={"Main Hall": 100},
                subscribers={"24.00000-0": "Main Hall"}
            )

    def test_rooms_is_not_dict(self):
        with pytest.raises(EntityError, match="Invalid rooms"):
            event(
                name="Tech Conference 2024",
                description="A conference for tech enthusiasts.",
                creation_date=1612137600,
                banner="https://example.com/banner.png",
                start_date=1612238400,
                end_date=1612324800,
                rooms="Main Hall",
                subscribers={"24.00000-0": "Main Hall"}
            )

    def test_rooms_invalid_capacity_type(self):
        with pytest.raises(EntityError, match="Invalid rooms"):
            event(
                name="Tech Conference 2024",
                description="A conference for tech enthusiasts.",
                creation_date=1612137600,
                banner="https://example.com/banner.png",
                start_date=1612238400,
                end_date=1612324800,
                rooms={"Main Hall": "100"},
                subscribers={"24.00000-0": "Main Hall"}
            )

    def test_subscribers_is_not_dict(self):
        with pytest.raises(EntityError, match="Invalid subscribers"):
            event(
                name="Tech Conference 2024",
                description="A conference for tech enthusiasts.",
                creation_date=1612137600,
                banner="https://example.com/banner.png",
                start_date=1612238400,
                end_date=1612324800,
                rooms={"Main Hall": 100},
                subscribers="24.00000-0: Main Hall"
            )

    def test_subscribers_invalid_room_reference(self):
        with pytest.raises(EntityError, match="Invalid subscribers"):
            event(
                name="Tech Conference 2024",
                description="A conference for tech enthusiasts.",
                creation_date=1612137600,
                banner="https://example.com/banner.png",
                start_date=1612238400,
                end_date=1612324800,
                rooms={"Main Hall": 100},
                subscribers={"24.00000-0": "Invalid Room"}
            )
