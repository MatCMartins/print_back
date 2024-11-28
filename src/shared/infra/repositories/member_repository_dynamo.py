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
        # Atualiza para usar a tabela específica do DynamoDB para "Member"
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_tables["MEMBER"],  # Usa a tabela de membros
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
            raise NoItemsFound("member_id")

        member_dto = MemberDynamoDTO.from_dynamo(resp["Item"])
        return member_dto.to_entity()

    def get_all_members(self) -> List[Member]:
        resp = self.dynamo.get_all_items()
        members = []
        for item in resp.get('Items', []):
            if item.get("entity") == 'member':
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

    def delete_member(self, member_id: int) -> Member:
        resp = self.dynamo.delete_item(
            partition_key=self.partition_key_format(member_id),
            sort_key=self.sort_key_format(member_id)
        )

        if "Attributes" not in resp:
            raise NoItemsFound("member_id")

        return MemberDynamoDTO.from_dynamo(resp['Attributes']).to_entity()

    def update_member(
        self,
        member_id: int,
        new_name: Optional[str] = None,
        new_email: Optional[str] = None,
        new_role: Optional[str] = None,
        new_photo: Optional[str] = None
    ) -> Member:
        item_to_update = {}

        if new_name is not None:
            item_to_update['name'] = new_name
        if new_email is not None:
            item_to_update['email'] = new_email
        if new_role is not None:
            item_to_update['role'] = new_role
        if new_photo is not None:
            item_to_update['photo'] = new_photo

        if not item_to_update:
            raise NoItemsFound("Nothing to update")

        resp = self.dynamo.update_item(
            partition_key=self.partition_key_format(member_id),
            sort_key=self.sort_key_format(member_id),
            update_dict=item_to_update
        )

        return MemberDynamoDTO.from_dynamo(resp['Attributes']).to_entity()
