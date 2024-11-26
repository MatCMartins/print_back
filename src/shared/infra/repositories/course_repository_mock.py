from typing import List, Optional

from src.shared.domain.entities.course import Course
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class CourseRepositoryMock(ICourseRepository):
        courses: List[Course]
    
        def __init__(self):
            self.courses = [
                Course(
                course_id="7d644e62-ef8b-4728-a92b-becb8930c24e",
                name="Computer Science",
                course_photo="https://example.com/computer_science_photo.jpg",
                coordinator="Alice Johnson",
                coordinator_photo="https://example.com/alice_photo.jpg",
                description="A course focused on programming, algorithms, and systems.",
                link="https://example.com/computer_science"
            ),
                Course(
                course_id="7d644e62-ef8b-4728-a92b-becb8930c24b",
                name="Data Analytics",
                course_photo="https://example.com/data_analytics_photo.jpg",
                coordinator="Bob Smith",
                coordinator_photo="https://example.com/bob_photo.jpg",
                description="Learn how to analyze data and extract meaningful insights.",
                link="https://example.com/data_analytics"
            ),
                Course(
                course_id="7d644e62-ef8b-4728-a92b-becb8930c24a",
                name="Marketing",
                course_photo="https://example.com/marketing_photo.jpg",
                coordinator="Carla Williams",
                coordinator_photo="https://example.com/carla_photo.jpg",
                description="Explore strategies for product promotion and brand management.",
                link=None 
            )
            ]
    
        def get_course(self, course_id: str) -> Course:
            for course in self.courses:
                if course.course_id == course_id:
                    return course
            raise NoItemsFound("course_id")
    
        def get_all_courses(self) -> List[Course]:
            return self.courses
    
        def create_course(self, new_course: Course) -> Course:
            self.courses.append(new_course)
            return new_course
    
        def delete_course(self, course_id: str) -> Course:
            for course in self.courses:
                if course.course_id == course_id:
                    self.courses.remove(course)
                    return course
            raise NoItemsFound("course_id")
    
        def update_course(self, course_id: str, new_name: Optional[str] = None, new_course_photo: Optional[str] = None, new_coordinator: Optional[str] = None, new_coordinator_photo: Optional[str] = None, new_description: Optional[str] = None, new_link: Optional[str] = None) -> Course:
            for course in self.courses:
                if course.course_id == course_id:
                    if new_name is not None:
                        course.name = new_name
                    if new_course_photo is not None:
                        course.course_photo = new_course_photo
                    if new_coordinator is not None:
                        course.coordinator = new_coordinator
                    if new_coordinator_photo is not None:
                        course.coordinator_photo = new_coordinator_photo
                    if new_description is not None:
                        course.description = new_description
                    course.link = new_link
                    return course
            raise NoItemsFound("course_id")