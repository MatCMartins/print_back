from src.shared.domain.entities.course import Course
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound



class GetAllCoursesUsecase:

    def __init__(self, repo: ICourseRepository):
        self.repo = repo
    
    def __call__(self) -> list[Course]:
        courses = self.repo.get_all_courses()
        
        if len(courses) == 0:
            raise NoItemsFound("courses")
        
        return courses
