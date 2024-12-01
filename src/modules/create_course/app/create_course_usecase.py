from typing import Optional
from uuid import uuid4
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.domain.entities.course import Course

class CreateCourseUsecase:

    def __init__(self, repo: ICourseRepository):
        self.repo = repo
    def __call__(self, name: str, course_photo: str, coordinator: str, coordinator_photo: str, description: str, link: Optional[str] = None):
        
        course_id = str(uuid4())

        course = Course(
            course_id=course_id,
            name=name,
            course_photo=course_photo,
            coordinator=coordinator,
            coordinator_photo=coordinator_photo,
            description=description,
            link=link
        )
        return self.repo.create_course(course)