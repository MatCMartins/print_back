from typing import List, Optional

from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.member_dynamo_dto import MemberDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class MemberRepositoryDynamo(IMemberRepository):

    @staticmethod
    def partition_key_format(member_id: int) -> str:
        return f"member#{member_id}"

    @staticmethod
    def sort_key_format(member_id: int) -> str:
        return f"#{member_id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_tables["MEMBER"],
            region=Environments.get_envs().region,
            partition_key="PK",
            sort_key="SK" 
        )

    def get_member(self, member_id: int) -> Member:
        resp = self.dynamo.get_item(
            partition_key=self.partition_key_format(member_id),
            sort_key=self.sort_key_format(member_id)
        )

        if resp.get('Item') is None:
            return None

        member_dto = MemberDynamoDTO.from_dynamo(resp["Item"])
        return member_dto.to_entity()

    def get_all_members(self) -> List[Member]:
        resp = self.dynamo.get_all_items()
        members = []
        for item in resp.get('Items', []):
            if item.get("entity") == 'Member':
                members.append(MemberDynamoDTO.from_dynamo(item).to_entity())

        return members

    def create_member(self, new_member: Member) -> Member:
        member_dto = MemberDynamoDTO.from_entity(member=new_member)
        self.dynamo.put_item(
            partition_key=self.partition_key_format(new_member.member_id),
            sort_key=self.sort_key_format(new_member.member_id),
            item=member_dto.to_dynamo()
        )
        return new_member


