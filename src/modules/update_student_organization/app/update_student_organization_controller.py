from .update_student_organization_usecase import UpdateStudentOrganizationUsecase
from .update_student_organization_viewmodel import UpdateStudentOrganizationViewmodel
from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class UpdateStudentOrganizationController:
    def __init__(self, usecase: UpdateStudentOrganizationUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get("stu_org_id") is None:
                raise MissingParameters("stu_org_id")
            
            if request.data.get("name") is not None:
                if StudentOrganization.validate_parameters(request.data.get("name")) is False:
                    raise WrongTypeParameter("name", str, str(type(request.data.get("name"))))
            
            if request.data.get("description") is not None:
                if StudentOrganization.validate_parameters(request.data.get("description")) is False:
                    raise WrongTypeParameter("description", str, str(type(request.data.get("description"))))
            
            if request.data.get("creation_date") is not None:
                if StudentOrganization.validate_creation_date(request.data.get("creation_date")) is False:
                    raise WrongTypeParameter("creation_date", int, str(type(request.data.get("creation_date"))))
            
            if request.data.get("logo") is not None:
                if StudentOrganization.validate_parameters(request.data.get("logo")) is False:
                    raise WrongTypeParameter("logo", str, str(type(request.data.get("logo"))))
            
            if request.data.get("instagram") is not None:
                if StudentOrganization.validate_parameters(request.data.get("instagram")) is False:
                    raise WrongTypeParameter("instagram", str, str(type(request.data.get("instagram"))))
                
            
            

            response = self.usecase(
                stu_org_id=request.data.get("stu_org_id"),
                name=request.data.get("name"),
                description=request.data.get("description"),
                creation_date=request.data.get("creation_date"),
                logo=request.data.get("logo"),
                instagram=request.data.get("instagram"),
            )

            viewmodel = UpdateStudentOrganizationViewmodel(
                stu_org_id=response.stu_org_id,
                name=response.name,
                description=response.description,
                creation_date=response.creation_date,
                logo=response.logo,
                instagram=response.instagram,
            )

            return OK(viewmodel.to_dict())
        
        except MissingParameters as error:
            return BadRequest(error.message)
        except WrongTypeParameter as error:
            return BadRequest(error.message)
        except NoItemsFound as error:
            return NotFound(error.message)
        except Exception as error:
            return InternalServerError(str(error))
        