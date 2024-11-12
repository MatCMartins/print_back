from src.shared.domain.entities.course import Course
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock
import pytest


class Test_CourseRepositoryMock:

    def test_get_course(self):
        repo = CourseRepositoryMock()
        course = repo.get_course(repo.courses[0].course_id)

        assert course.name == "Computer Science"
        assert course.course_photo == "https://example.com/computer_science_photo.jpg"
        assert course.coordinator == "Alice Johnson"
        assert course.coordinator_photo == "https://example.com/alice_photo.jpg"
        assert course.description == "A course focused on programming, algorithms, and systems."
        assert course.link == "https://example.com/computer_science"

    def test_get_course_not_found(self):
        repo = CourseRepositoryMock()
        with pytest.raises(NoItemsFound):
            repo.get_course("32")
    
    def test_get_all_courses(self):
        repo = CourseRepositoryMock()
        courses = repo.get_all_courses()
        assert len(courses) == 3

    def test_create_course(self):
        repo = CourseRepositoryMock()
        course = Course(
            name="Physics",
            course_photo="https://example.com/physics_photo.jpg",
            coordinator="John Doe",
            coordinator_photo="https://example.com/john_photo.jpg",
            description="A course focused on physics.",
            link="https://example.com/physics"
        )

        repo.create_course(course)

        assert repo.courses[3].name == "Physics"
        assert repo.courses[3].course_photo == "https://example.com/physics_photo.jpg"
        assert repo.courses[3].coordinator == "John Doe"
        assert repo.courses[3].coordinator_photo == "https://example.com/john_photo.jpg"
        assert repo.courses[3].description == "A course focused on physics."
        assert repo.courses[3].link == "https://example.com/physics"
    
    def test_delete_course(self):
        repo = CourseRepositoryMock()
        course = repo.delete_course(repo.courses[0].course_id)

        assert course.name == "Computer Science"
        assert len(repo.courses) == 2
    
    def test_delete_course_not_found(self):
        repo = CourseRepositoryMock()
        with pytest.raises(NoItemsFound):
            repo.delete_course("32")
    
    def test_update_course(self):
        repo = CourseRepositoryMock()
        course = repo.update_course(repo.courses[0].course_id, new_name="Physics", new_course_photo="https://example.com/physics_photo.jpg", new_coordinator="John Doe", new_coordinator_photo="https://example.com/john_photo.jpg", new_description="A course focused on physics.", new_link="https://example.com/physics")

        assert course.name == "Physics"
        assert repo.courses[0].name == "Physics"
        assert repo.courses[0].course_photo == "https://example.com/physics_photo.jpg"
        assert repo.courses[0].coordinator == "John Doe"
        assert repo.courses[0].coordinator_photo == "https://example.com/john_photo.jpg"
        assert repo.courses[0].description == "A course focused on physics."
        assert repo.courses[0].link == "https://example.com/physics"
    
    def test_update_course_not_found(self):
        repo = CourseRepositoryMock()
        with pytest.raises(NoItemsFound):
            repo.update_course("32", new_name="Physics")

    def test_update_course_name(self):
        repo = CourseRepositoryMock()
        course = repo.update_course(repo.courses[0].course_id, new_name="Physics")

        assert course.name == "Physics"
        assert repo.courses[0].name == "Physics"
    
    def test_update_course_link(self):
        repo = CourseRepositoryMock()
        course = repo.update_course(repo.courses[0].course_id, new_link=None)

        assert repo.courses[0].link == None

   