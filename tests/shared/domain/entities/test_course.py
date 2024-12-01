from src.shared.domain.entities.course import Course
from src.shared.helpers.errors.domain_errors import EntityError
import pytest


class Test_Course:
    def test_course(self):
        course = Course(
            course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name="Computer Science",
            course_photo="https://example.com/computer_science_photo.jpg",
            coordinator="Alice Johnson",
            coordinator_photo="https://example.com/alice_photo.jpg",
            description="A course focused on programming, algorithms, and systems.",
            link="https://example.com/computer_science"
            )

        assert  course.name == "Computer Science"
        assert  course.course_photo == "https://example.com/computer_science_photo.jpg"
        assert  course.coordinator == "Alice Johnson"
        assert  course.coordinator_photo == "https://example.com/alice_photo.jpg"
        assert  course.description == "A course focused on programming, algorithms, and systems."
        assert  course.link == "https://example.com/computer_science"
    
    def test_course_with_optional_link(self):
        course = Course(
            course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name="Marketing",
            course_photo="https://example.com/marketing_photo.jpg",
            coordinator="Carla Williams",
            coordinator_photo="https://example.com/carla_photo.jpg",
            description="Explore strategies for product promotion and brand management.",
            link=None
            )
        
        assert course.link == None

    def test_course_with_invalid_name(self):
        with pytest.raises(EntityError):
            Course(
                course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
                name=None,
                course_photo="https://example.com/computer_science_photo.jpg",
                coordinator="Alice Johnson",
                coordinator_photo="https://example.com/alice_photo.jpg",
                description="A course focused on programming, algorithms, and systems.",
                link="https://example.com/computer_science"
            )

    def test_course_with_invalid_course_photo(self):
        with pytest.raises(EntityError):
            Course(
                course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
                name="Computer Science",
                course_photo=None,
                coordinator="Alice Johnson",
                coordinator_photo="https://example.com/alice_photo.jpg",
                description="A course focused on programming, algorithms, and systems.",
                link="https://example.com/computer_science"
            )
    
    def test_course_with_invalid_coordinator(self):
        with pytest.raises(EntityError):
            Course(
                course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
                name="Computer Science",
                course_photo="https://example.com/computer_science_photo.jpg",
                coordinator=None,
                coordinator_photo="https://example.com/alice_photo.jpg",
                description="A course focused on programming, algorithms, and systems.",
                link="https://example.com/computer_science"
            )
    
    def test_course_with_invalid_coordinator_photo(self):
        with pytest.raises(EntityError):
            Course(
                course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
                name="Computer Science",
                course_photo="https://example.com/computer_science_photo.jpg",
                coordinator="Alice Johnson",
                coordinator_photo=None,
                description="A course focused on programming, algorithms, and systems.",
                link="https://example.com/computer_science"
            )
    
    def test_course_with_invalid_description(self):
        with pytest.raises(EntityError):
            Course(
                course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
                name="Computer Science",
                course_photo="https://example.com/computer_science_photo.jpg",
                coordinator="Alice Johnson",
                coordinator_photo="https://example.com/alice_photo.jpg",
                description=None,
                link="https://example.com/computer_science"
            )
    
    def test_course_with_invalid_link(self):
        with pytest.raises(EntityError):
            Course(
                course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
                name="Computer Science",
                course_photo="https://example.com/computer_science_photo.jpg",
                coordinator="Alice Johnson",
                coordinator_photo="https://example.com/alice_photo.jpg",
                description="A course focused on programming, algorithms, and systems.",
                link=123
            )