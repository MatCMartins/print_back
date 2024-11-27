import enum
from enum import Enum
import os

from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.domain.repositories.event_repository_interface import IEventRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    HOMOLOG = "HOMOLOG"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.
    """

    stage: STAGE
    region: str
    s3_buckets: dict
    dynamo_tables: dict
    endpoint_url: str = None
    cloud_front_distribution_domain: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.DOTENV.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

        self.region = os.environ.get("REGION", "us-east-1")
        
        self.s3_buckets = {
            "COURSE": os.environ.get("COURSE_BUCKET_NAME"),
            "EVENT": os.environ.get("EVENT_BUCKET_NAME"),
            "MEMBER": os.environ.get("MEMBER_BUCKET_NAME"),
            "STUDENT_ORG": os.environ.get("STUDENT_ORG_BUCKET_NAME"),
        }

        self.dynamo_tables = {
            "COURSE": os.environ.get("DYNAMO_COURSE_TABLE"),
            "EVENT": os.environ.get("DYNAMO_EVENT_TABLE"),
            "MEMBER": os.environ.get("DYNAMO_MEMBER_TABLE"),
            "STUDENT_ORG": os.environ.get("DYNAMO_STUDENT_ORG_TABLE"),
        }

        self.endpoint_url = os.environ.get("ENDPOINT_URL")
        self.cloud_front_distribution_domain = os.environ.get("CLOUD_FRONT_DISTRIBUTION_DOMAIN")

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        """
        envs = Environments()
        envs.load_envs()
        return envs

    @staticmethod
    def get_course_repo() -> ICourseRepository:
        """
        Retorna a instância do repositório de cursos baseado no stage.
        """
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock
            return CourseRepositoryMock()
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.course_repository_dynamo import CourseRepositoryDynamo
            return CourseRepositoryDynamo()
        else:
            raise Exception("No repository found for this stage")


    @staticmethod
    def get_event_repo() -> IEventRepository:
        """
        Retorna a instância do repositório de eventos baseado no stage.
        """
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
            return EventRepositoryMock()
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.event_repository_dynamo import EventRepositoryDynamo
            return EventRepositoryDynamo()
        else:
            raise Exception("No repository found for this stage")


    @staticmethod
    def get_member_repo() -> IMemberRepository:
        """
        Retorna a instância do repositório de membros baseado no stage.
        """
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
            return MemberRepositoryMock()
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.member_repository_dynamo import MemberRepositoryDynamo
            return MemberRepositoryDynamo()
        else:
            raise Exception("No repository found for this stage")


    @staticmethod
    def get_student_org_repo() -> IStudentOrganizationRepository:
        """
        Retorna a instância do repositório de organizações estudantis baseado no stage.
        """
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
            return StudentOrganizationRepositoryMock()
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.student_organization_repository_dynamo import StudentOrganizationRepositoryDynamo
            return StudentOrganizationRepositoryDynamo()
        else:
            raise Exception("No repository found for this stage")

    def __repr__(self):
        return str(self.__dict__)
