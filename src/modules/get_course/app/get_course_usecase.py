from src.shared.domain.entities.course import Course
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound



class GetCourseUsecase:

    def __init__(self, repo: ICourseRepository):
        self.repo = repo
    
    def __call__(self, course_id: str):

        if not self.repo.get_course(course_id):
            raise NoItemsFound("Course")
        
        return self.repo.get_course(course_id)
