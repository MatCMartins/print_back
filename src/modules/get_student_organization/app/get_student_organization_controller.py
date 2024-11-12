from .get_student_organization_usecase import GetStudentOrganizationUsecase
from .get_student_organization_viewmodel import GetStudentOrganizationViewmodel
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class GetStudentOrganizationController:

    def __init__(self, usecase: GetStudentOrganizationUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('stu_org_id') is None:
                raise MissingParameters("stu_org_id")
            
            if type(request.data.get('stu_org_id')) is not str:
                raise WrongTypeParameter("stu_org_id", str, type(request.data.get('stu_org_id')))
            
            stu_org = self.usecase(request.data.get('stu_org_id'))

            viewmodel = GetStudentOrganizationViewmodel(
                stu_org_id=stu_org.stu_org_id,
                name=stu_org.name,
                description=stu_org.description,
                creation_date=stu_org.creation_date,
                logo=stu_org.logo,
                instagram=stu_org.instagram,
                website_link=stu_org.website_link
            )

            return OK(viewmodel.to_dict())
        except NoItemsFound as e:
            return BadRequest(body=e.message)
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except WrongTypeParameter as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])

