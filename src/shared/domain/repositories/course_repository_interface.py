from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.course import Course


class ICourseRepository(ABC):

    @abstractmethod
    def get_course(self, course_id: str) -> Course:
        """
        If course_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_all_courses(self) -> List[Course]:
        """
        If course_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def create_course(self, new_course: Course) -> Course:
        """
        Creates new course and returns it
        """
        pass

    @abstractmethod
    def delete_course(self, course_id: str) -> Course:
        """
        If course_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def update_course(self, course_id: str, new_name: Optional[str] = None, new_course_photo: Optional[str] = None, new_coordinator: Optional[str] = None, new_coordinator_photo: Optional[str] = None, new_description: Optional[str] = None, new_link: Optional[str] = None) -> Course:
        """
        If course_id not found raise NoItemsFound
        """
        pass