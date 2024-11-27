from .create_student_organization_usecase import CreateStudentOrganizationUsecase
from .create_student_organization_viewmodel import CreateStudentOrganizationViewModel
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, Created
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.domain_errors import EntityError

class CreateStudentOrganizationController:
    def __init__(self, usecase: CreateStudentOrganizationUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            params = ["name", "description", "creation_date", "logo", "instagram", "website_link"]

            for param in params:
                if request.data.get(param) is None:
                    raise MissingParameters(param)

            stu_org = self.usecase(
                name=request.data.get("name"),
                description=request.data.get("description"),
                creation_date=request.data.get("creation_date"),
                logo=request.data.get("logo"),
                instagram=request.data.get("instagram"),
                website_link=request.data.get("website_link")
            )

            viewmodel = CreateStudentOrganizationViewModel(
                stu_org_id=stu_org.stu_org_id,
                name=stu_org.name,
                description=stu_org.description,
                creation_date=stu_org.creation_date,
                logo=stu_org.logo,
                instagram=stu_org.instagram,
                website_link=stu_org.website_link
            )

            return Created(viewmodel.to_dict())
        
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except EntityError as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])
    
