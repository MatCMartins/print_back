from typing import Optional
from src.shared.domain.entities.course import Course
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class UpdateCourseUsecase:

    def __init__(self, repo: ICourseRepository):
        self.repo = repo

    def __call__(self, course_id: str, name: Optional[str], course_photo: Optional[str], coordinator: Optional[str], coordinator_photo: Optional[str], description: Optional[str], link: Optional[str]) -> Course:
        
        if not self.repo.get_course(course_id):
            raise NoItemsFound("Course")
        
        return self.repo.update_course(course_id=course_id, new_name=name, new_course_photo=course_photo, new_coordinator=coordinator, new_coordinator_photo=coordinator_photo, new_description=description, new_link=link)