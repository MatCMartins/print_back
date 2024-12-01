from src.shared.domain.entities.course import Course
from src.shared.domain.enums.state_enum import STATE
from src.shared.infra.dto.course_dynamo_dto import CourseDynamoDTO
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock


class Test_CourseDynamoDTO:
    def test_from_entity(self):
        repo = CourseRepositoryMock()

        course_dto = CourseDynamoDTO.from_entity(course=repo.courses[0])

        expected_course_dto = CourseDynamoDTO(
            course_id=repo.courses[0].course_id,
            name=repo.courses[0].name,
            course_photo=repo.courses[0].course_photo,
            coordinator=repo.courses[0].coordinator,
            coordinator_photo=repo.courses[0].coordinator_photo,
            description=repo.courses[0].description,
            link=repo.courses[0].link
        )

        assert course_dto == expected_course_dto

    def test_to_dynamo(self):
        repo = CourseRepositoryMock()

        course_dto = CourseDynamoDTO(
            course_id=repo.courses[0].course_id,
            name=repo.courses[0].name,
            course_photo=repo.courses[0].course_photo,
            coordinator=repo.courses[0].coordinator,
            coordinator_photo=repo.courses[0].coordinator_photo,
            description=repo.courses[0].description,
            link=repo.courses[0].link
        )

        course_dynamo = course_dto.to_dynamo()

        expected_dict = {
            "entity": "course",
            "course_id": repo.courses[0].course_id,
            "name": repo.courses[0].name,
            "course_photo": repo.courses[0].course_photo,
            "coordinator": repo.courses[0].coordinator,
            "coordinator_photo": repo.courses[0].coordinator_photo,
            "description": repo.courses[0].description,
            "link": repo.courses[0].link
        }

        assert course_dynamo == expected_dict

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'course_id': 1234,
                                'name': 'mateus',
                                'SK': '#' + str(1234),
                                'PK': 'course#' + str(1234),
                                'entity': 'course',
                                'course_photo': 'course_photo',
                                'coordinator': 'coordinator',
                                'coordinator_photo': 'coordinator_photo',
                                'description': 'description',
                                'link': 'link'
                                },
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}
    
        course_dto = CourseDynamoDTO.from_dynamo(course_data=dynamo_dict["Item"])

        expected_course_dto = CourseDynamoDTO(
            course_id=1234,
            name='mateus',
            course_photo='course_photo',
            coordinator='coordinator',
            coordinator_photo='coordinator_photo',
            description='description',
            link='link'
        )

        assert course_dto == expected_course_dto
    
    def test_to_entity(self):
        repo = CourseRepositoryMock()

        course_dto = CourseDynamoDTO(
            course_id=repo.courses[0].course_id,
            name=repo.courses[0].name,
            course_photo=repo.courses[0].course_photo,
            coordinator=repo.courses[0].coordinator,
            coordinator_photo=repo.courses[0].coordinator_photo,
            description=repo.courses[0].description,
            link=repo.courses[0].link
        )

        course = course_dto.to_entity()

        assert course.name == repo.courses[0].name
        assert course.course_photo == repo.courses[0].course_photo
        assert course.coordinator == repo.courses[0].coordinator
        assert course.coordinator_photo == repo.courses[0].coordinator_photo
        assert course.description == repo.courses[0].description
        assert course.link == repo.courses[0].link
    
    def test_from_dynamo_to_entity(self):
        dynamo_item = {'Item': {'course_id': "b9799d9d-798c-4f44-9fd7-b9ae41c77496",
                                'name': 'mateus',
                                'SK': '#' + str("b9799d9d-798c-4f44-9fd7-b9ae41c77496"),
                                'PK': 'course#' + str("b9799d9d-798c-4f44-9fd7-b9ae41c77496"),
                                'entity': 'course',
                                'course_photo': 'course_photo',
                                'coordinator': 'coordinator',
                                'coordinator_photo': 'coordinator_photo',
                                'description': 'description',
                                'link': 'link'
                                }}

        course_dto = CourseDynamoDTO.from_dynamo(course_data=dynamo_item["Item"])

        course = course_dto.to_entity()

        expected_course = Course(
            course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name='mateus',
            course_photo='course_photo',
            coordinator='coordinator',
            coordinator_photo='coordinator_photo',
            description='description',
            link='link',
        )

        assert course.name == expected_course.name
        assert course.course_photo == expected_course.course_photo
        assert course.coordinator == expected_course.coordinator
        assert course.coordinator_photo == expected_course.coordinator_photo
        assert course.description == expected_course.description
        assert course.link == expected_course.link