from src.shared.domain.entities.course import Course

class GetCourseViewmodel:
    course_id: str
    name: str
    course_photo: str
    coordinator: str
    coordinator_photo: str
    description: str
    link: str

    def __init__(self, course_id: str, name: str, course_photo: str, coordinator: str, coordinator_photo: str, description: str, link: str):
        self.course_id = course_id
        self.name = name
        self.course_photo = course_photo
        self.coordinator = coordinator
        self.coordinator_photo = coordinator_photo
        self.description = description
        self.link = link
    
    def to_dict(self):
        return {
            "course_id": self.course_id,
            "name": self.name,
            "course_photo": self.course_photo,
            "coordinator": self.coordinator,
            "coordinator_photo": self.coordinator_photo,
            "description": self.description,
            "link": self.link
        }

class GetAllCoursesViewmodel:
    def __init__(self, courses: list[Course]):
        self.courses = courses
    
    def to_dict(self):
        return {
            "courses": [course.to_dict() for course in self.courses]
        }
    