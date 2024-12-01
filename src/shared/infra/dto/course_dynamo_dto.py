
from src.shared.domain.entities.course import Course
from src.shared.domain.enums.state_enum import STATE


class CourseDynamoDTO:

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

    @staticmethod
    def from_entity(course: Course) -> "CourseDynamoDTO":
        """
        Parse data from Course to CourseDynamoDTO
        """
        return CourseDynamoDTO(
            course_id=course.course_id,
            name=course.name,
            course_photo=course.course_photo,
            coordinator=course.coordinator,
            coordinator_photo=course.coordinator_photo,
            description=course.description,
            link=course.link
        )
    
    def to_dynamo(self) -> dict:
        """
        Parse data from CourseDynamoDTO to dict
        """
        return {
            "entity": "course",
            "course_id": self.course_id,
            "name": self.name,
            "course_photo": self.course_photo,
            "coordinator": self.coordinator,
            "coordinator_photo": self.coordinator_photo,
            "description": self.description,
            "link": self.link
        }
    
    @staticmethod
    def from_dynamo(course_data: dict) -> "CourseDynamoDTO":
        """
        Parse data from DynamoDB to CourseDynamoDTO
        @param course_data: dict from DynamoDB
        """
        return CourseDynamoDTO(
            course_id=course_data["course_id"],
            name=course_data["name"],
            course_photo=course_data["course_photo"],
            coordinator=course_data["coordinator"],
            coordinator_photo=course_data["coordinator_photo"],
            description=course_data["description"],
            link=course_data["link"]
        )
    
    def to_entity(self) -> Course:
        """
        Parse data from CourseDynamoDTO to Course
        """
        return Course(
            course_id=self.course_id,
            name=self.name,
            course_photo=self.course_photo,
            coordinator=self.coordinator,
            coordinator_photo=self.coordinator_photo,
            description=self.description,
            link=self.link
        )
    
    def __repr__(self):
        return f"CourseDynamoDTO(course_id={self.course_id} name={self.name}, course_photo={self.course_photo}, coordinator={self.coordinator}, coordinator_photo={self.coordinator_photo}, description={self.description}, link={self.link})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__