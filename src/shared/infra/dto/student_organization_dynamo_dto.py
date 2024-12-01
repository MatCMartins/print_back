
from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.enums.state_enum import STATE


class StudentOrganizationDynamoDTO:
    stu_org_id: str
    name: str
    description: str
    creation_date: int
    logo: str
    instagram: str
    website_link: str

    def __init__(self, stu_org_id: str, name: str, description: str, creation_date: int, logo: str, instagram: str, website_link: str):
        self.stu_org_id = stu_org_id
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.logo = logo
        self.instagram = instagram
        self.website_link = website_link

    @staticmethod
    def from_entity(stu_org: StudentOrganization) -> "StudentOrganizationDynamoDTO":
        """
        Parse data from StudentOrganization to StudentOrganizationDynamoDTO
        """
        return StudentOrganizationDynamoDTO(
            stu_org_id=stu_org.stu_org_id,
            name=stu_org.name,
            description=stu_org.description,
            creation_date=stu_org.creation_date,
            logo=stu_org.logo,
            instagram=stu_org.instagram,
            website_link=stu_org.website_link
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from StudentOrganizationDynamoDTO to dict
        """
        return {
            "entity": "student_organization",
            "stu_org_id": self.stu_org_id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "logo": self.logo,
            "instagram": self.instagram,
            "website_link": self.website_link
        }

    @staticmethod
    def from_dynamo(stu_org_data: dict) -> "StudentOrganizationDynamoDTO":
        """
        Parse data from DynamoDB to StudentOrganizationDynamoDTO
        @param stu_org_data: dict from DynamoDB
        """
        return StudentOrganizationDynamoDTO(
            stu_org_id=stu_org_data["stu_org_id"],
            name=stu_org_data["name"],
            description=stu_org_data["description"],
            creation_date=stu_org_data["creation_date"],
            logo=stu_org_data["logo"],
            instagram=stu_org_data["instagram"],
            website_link=stu_org_data["website_link"]
        )

    def to_entity(self) -> StudentOrganization:
        """
        Parse data from StudentOrganizationDynamoDTO to StudentOrganization
        """
        return StudentOrganization(
            stu_org_id=self.stu_org_id,
            name=self.name,
            description=self.description,
            creation_date=int(self.creation_date),
            logo=self.logo,
            instagram=self.instagram,
            website_link=self.website_link
        )

    def __repr__(self):
        return f"StudentOrganizationDynamoDTO(stu_org_id={self.stu_org_id} name={self.name}, description={self.description}, creation_date={self.creation_date}, logo={self.logo}, instagram={self.instagram}, website_link={self.website_link})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
