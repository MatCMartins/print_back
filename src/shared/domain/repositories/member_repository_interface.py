from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.member import Member


class IMemberRepository(ABC):

    @abstractmethod
    def get_member(self, member_id: str) -> Member:
        """
        If member_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_all_members(self) -> List[Member]:
        """
        If member_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def create_member(self, new_member: Member) -> Member:
        """
        Creates new Member and returns it
        """
        pass

