import os

import pytest

from src.shared.infra.repositories.course_repository_dynamo import CourseRepositoryDynamo
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock
from src.shared.domain.entities.course import Course


class Test_CourseRepositoryDynamo:

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_create_course(self):

        course_repository = CourseRepositoryDynamo()
        course_repository_mock = CourseRepositoryMock()

        course = Course(
            name="Maua Tech",
            description="Technology organization focused on promoting knowledge and projects in the field of technology and innovation.",
            course_photo="https://mauatech.com/logo.png",
            coordinator="John Doe",
            coordinator_photo="https://example.com/john_photo.jpg",
            link="https://mauatech.com"
        )

        resp = course_repository.create_course(course)

        assert course_repository_mock.courses[0].name == resp.name

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_course(self):

        course_repository = CourseRepositoryDynamo()
        course_repository_mock = CourseRepositoryMock()
        resp = course_repository.get_course(course_repository_mock.courses[0].course_id)
        assert course_repository_mock.courses[0].name == resp.name

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_delete_course(self):
        
        course_repository = CourseRepositoryDynamo()
        course_repository_mock = CourseRepositoryMock()
        resp = course_repository.delete_course(course_repository_mock.courses[1].course_id)

        assert course_repository_mock.courses[1].name == resp.name

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_courses(self):
        
        course_repository = CourseRepositoryDynamo()
        course_repository_mock = CourseRepositoryMock()
        resp = course_repository.get_all_courses()

        assert len(course_repository_mock.courses) == len(resp)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_update_course(self):
        
        course_repository = CourseRepositoryDynamo()
        course_repository_mock = CourseRepositoryMock()
        resp = course_repository.update_course(course_id=course_repository_mock.courses[0].course_id, new_name="Maua Tech")

        assert resp.name == "Maua Tech"