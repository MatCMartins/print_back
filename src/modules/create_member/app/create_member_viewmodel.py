class CreateMemberViewmodel:
    member_id: str
    name: str
    email: str
    activities: list

    def __init__(self, member_id: str, name: str, email: str, activities: list):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.activities = activities
    
    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "activities": self.activities
        }

    