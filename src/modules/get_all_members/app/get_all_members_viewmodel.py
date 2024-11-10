from src.shared.domain.entities.member import Member

class GetAllMembersViewmodel:
    def __init__(self, members: list[Member]):
        self.members = members
    
    def to_dict(self):
        return {
            "members": [member.to_dict() for member in self.members]
        }
    