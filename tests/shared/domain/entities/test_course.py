from src.shared.domain.entities.course import Course
from src.shared.helpers.errors.domain_errors import EntityError
import pytest


class Test_Course:
    def test_course(self):
        course = Course(
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
                name="Computer Science",
                course_photo="https://example.com/computer_science_photo.jpg",
                coordinator="Alice Johnson",
                coordinator_photo="https://example.com/alice_photo.jpg",
                description="A course focused on programming, algorithms, and systems.",
                link=123
            )
    



    # def test_name_is_none(self):
    #     with pytest.raises(EntityError):
    #         Course(name=None, description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua", website_link="https://devmaua.com")

    # def test_name_is_not_str(self):
    #     with pytest.raises(EntityError):
    #         Course(name=1, description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua", website_link="https://devmaua.com")

    # def test_description_is_none(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description=None, creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua", website_link="https://devmaua.com")

    # def test_description_is_not_valid(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description=321312, creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua", website_link="https://devmaua.com")

    # def test_creation_date_is_none(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=None, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua", website_link="https://devmaua.com")

    # def test_creation_date_is_not_valid(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date="1612137600", logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua", website_link="https://devmaua.com")

    # def test_logo_is_none(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo=None, instagram="https://instagram.com/devcommunitymaua", website_link="https://devmaua.com")

    # def test_logo_is_not_valid(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo=123, instagram="https://instagram.com/devcommunitymaua", website_link="https://devmaua.com")

    # def test_instagram_is_none(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram=None, website_link="https://devmaua.com")

    # def test_instagram_is_not_valid(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram=12, website_link="https://devmaua.com")

    # def test_instagram_is_none(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua", website_link=None)

    # def test_instagram_is_not_valid(self):
    #     with pytest.raises(EntityError):
    #         Course(name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua", website_link=321)

