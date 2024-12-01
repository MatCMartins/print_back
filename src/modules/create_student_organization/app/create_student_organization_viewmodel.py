class CreateStudentOrganizationViewModel:
    stu_org_id: str
    name: str
    description: str
    creation_date: str
    logo: str
    instagram: str

    def __init__(self, stu_org_id: str, name: str, description: str, creation_date: str, logo: str, instagram: str):
        self.stu_org_id = stu_org_id
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.logo = logo
        self.instagram = instagram
    
    def to_dict(self):
        return {
            "stu_org_id": self.stu_org_id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "logo": self.logo,
            "instagram": self.instagram
        }

    