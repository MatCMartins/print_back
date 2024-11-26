
from typing import List, Optional

from src.shared.domain.entities.course import Course
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.course_dynamo_dto import CourseDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class CourseRepositoryDynamo(ICourseRepository):

    @staticmethod
    def partition_key_format(course_id) -> str:
        return f"course#{course_id}"

    @staticmethod
    def sort_key_format(course_id: str) -> str:
        return f"#{course_id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)
    def get_course(self, course_id: str) -> Course:
        resp = self.dynamo.get_item(
            partition_key=self.partition_key_format(course_id),
            sort_key=self.sort_key_format(course_id)
        )

        if resp.get('Item') is None:
            raise NoItemsFound("course_id")

        course_dto = CourseDynamoDTO.from_dynamo(resp["Item"])
        return course_dto.to_entity()

    def get_all_courses(self) -> List[Course]:
        resp = self.dynamo.get_all_items()
        courses = []
        for item in resp['Items']:
            if item.get("entity") == 'student_organization':
                courses.append(CourseDynamoDTO.from_dynamo(item).to_entity())

        return courses


    def create_course(self, new_course: Course) -> Course:
        course_dto = CourseDynamoDTO.from_entity(course=new_course)
        resp = self.dynamo.put_item(partition_key=self.partition_key_format(new_course.course_id),
                                    sort_key=self.sort_key_format(course_id=new_course.course_id), item=course_dto.to_dynamo())
        return new_course

    def delete_course(self, course_id: str) -> Course:
        resp = self.dynamo.delete_item(partition_key=self.partition_key_format(course_id), sort_key=self.sort_key_format(course_id))

        if "Attributes" not in resp:
            raise NoItemsFound("course_id")

        return CourseDynamoDTO.from_dynamo(resp['Attributes']).to_entity()

    def update_course(self, course_id: str, new_name: Optional[str] = None, new_course_photo: Optional[str] = None, new_coordinator: Optional[str] = None, new_coordinator_photo: Optional[str] = None, new_description: Optional[str] = None, new_link: Optional[str] = None) -> Course:
        item_to_update = {}

        if new_name is not None:
            item_to_update['name'] = new_name
        if new_description is not None:
            item_to_update['description'] = new_description
        if new_course_photo is not None:
            item_to_update['course_photo'] = new_course_photo
        if new_coordinator is not None:
            item_to_update['coordinator'] = new_coordinator
        if new_coordinator_photo is not None:
            item_to_update['coordinator_photo'] = new_coordinator_photo
        if new_link is not None:
            item_to_update['link'] = new_link
        
        if item_to_update == {}:
            raise NoItemsFound("Nothing to update")

        resp = self.dynamo.update_item(partition_key=self.partition_key_format(course_id), sort_key=self.sort_key_format(course_id), update_dict=item_to_update)

        return CourseDynamoDTO.from_dynamo(resp['Attributes']).to_entity()
