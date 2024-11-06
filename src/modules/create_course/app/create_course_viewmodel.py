from typing import Optional


class CreateCourseViewModel:
    course_id: str
    name: str
    course_photo: str
    coordinator: str
    coordinator_photo: str
    description: str
    link: Optional[str] = None

    def __init__(self, course_id: str, name: str, course_photo: str, coordinator: str, coordinator_photo: str, description: str, link: Optional[str] = None):
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

    