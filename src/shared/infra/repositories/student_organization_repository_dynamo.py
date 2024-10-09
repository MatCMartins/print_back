
from typing import List

from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.student_organization_dynamo_dto import StudentOrganizationDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class StudentOrganizationRepositoryDynamo(IStudentOrganizationRepository):

    @staticmethod
    def partition_key_format(stu_org_id) -> str:
        return f"stu_org#{stu_org_id}"

    @staticmethod
    def sort_key_format(stu_org_id: int) -> str:
        return f"#{stu_org_id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)
    def get_stu_org(self, stu_org_id: int) -> StudentOrganization:
        resp = self.dynamo.get_item(partition_key=self.partition_key_format(stu_org_id), sort_key=self.sort_key_format(stu_org_id))

        if resp.get('Item') is None:
            raise NoItemsFound("stu_org_id")

        stu_org_dto = StudentOrganizationDynamoDTO.from_dynamo(resp["Item"])
        return stu_org_dto.to_entity()

    def get_all_stu_orgs(self) -> List[StudentOrganization]:
        resp = self.dynamo.get_all_items()
        stu_orgs = []
        for item in resp['Items']:
            if item.get("entity") == 'student_organization':
                stu_orgs.append(StudentOrganizationDynamoDTO.from_dynamo(item).to_entity())

        return stu_orgs


    def create_stu_org(self, new_stu_org: StudentOrganization) -> StudentOrganization:
        stu_dto = StudentOrganizationDynamoDTO.from_entity(stu_org=new_stu_org)
        resp = self.dynamo.put_item(partition_key=self.partition_key_format(new_stu_org.stu_org_id),
                                    sort_key=self.sort_key_format(stu_org_id=new_stu_org.stu_org_id), item=stu_dto.to_dynamo())
        return new_stu_org

    def delete_stu_org(self, stu_org_id: int) -> StudentOrganization:
        resp = self.dynamo.delete_item(partition_key=self.partition_key_format(stu_org_id), sort_key=self.sort_key_format(stu_org_id))

        if "Attributes" not in resp:
            raise NoItemsFound("stu_org_id")

        return StudentOrganizationDynamoDTO.from_dynamo(resp['Attributes']).to_entity()

    def update_stu_org(self, stu_org_id: int, new_name: str = None, new_description: str = None, new_creation_date: int = None, new_logo: str = None, new_instagram: str = None, new_website_link: str = None) -> StudentOrganization:
        item_to_update = {}

        if new_name is not None:
            item_to_update['name'] = new_name
        if new_description is not None:
            item_to_update['description'] = new_description
        if new_creation_date is not None:
            item_to_update['creation_date'] = new_creation_date
        if new_logo is not None:
            item_to_update['logo'] = new_logo
        if new_instagram is not None:
            item_to_update['instagram'] = new_instagram
        if new_website_link is not None:
            item_to_update['website_link'] = new_website_link
        
        if item_to_update == {}:
            raise NoItemsFound("Nothing to update")

        resp = self.dynamo.update_item(partition_key=self.partition_key_format(stu_org_id), sort_key=self.sort_key_format(stu_org_id), update_dict=item_to_update)

        return StudentOrganizationDynamoDTO.from_dynamo(resp['Attributes']).to_entity()
