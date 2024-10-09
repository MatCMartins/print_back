from src.shared.domain.entities.student_organization import StudentOrganization



class GetStudentOrganizationViewmodel:
    stu_org_id: str
    name: str
    description: str
    creation_date: str
    logo: str
    instagram: str
    website_link: str

    def __init__(self, stu_org_id: str, name: str, description: str, creation_date: str, logo: str, instagram: str, website_link: str):
        self.stu_org_id = stu_org_id
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.logo = logo
        self.instagram = instagram
        self.website_link = website_link
    
    def to_dict(self):
        return {
            "stu_org_id": self.stu_org_id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "logo": self.logo,
            "instagram": self.instagram,
            "website_link": self.website_link
        }
    
class GetAllStudentOrganizationsViewmodel:
    def __init__(self, student_organizations: list[StudentOrganization]):
        self.student_organizations = student_organizations
    
    def to_dict(self):
        return {
            "student_organizations": [stu_org.to_dict() for stu_org in self.student_organizations]
        }
    