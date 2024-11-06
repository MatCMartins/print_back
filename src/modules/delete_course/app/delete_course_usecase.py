from src.shared.domain.entities.course import Course
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteCourseUsecase:

    def __init__(self, repo: ICourseRepository):
        self.repo = repo
    
    def __call__(self, course_id: str) -> Course:

        if not self.repo.get_course(course_id):
            raise NoItemsFound("Course not found")
        
        return self.repo.delete_course(course_id)
