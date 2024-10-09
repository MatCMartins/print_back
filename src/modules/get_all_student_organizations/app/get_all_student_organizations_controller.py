from .get_all_student_organizations_usecase import GetAllStudentOrganizationsUsecase
from .get_all_student_organizations_viewmodel import GetAllStudentOrganizationsViewmodel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class GetAllStudentOrganizationsController:

    def __init__(self, usecase: GetAllStudentOrganizationsUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            stu_orgs = self.usecase()

            viewmodel = GetAllStudentOrganizationsViewmodel(
                student_organizations=stu_orgs
            )   

            return OK(viewmodel.to_dict())
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except WrongTypeParameter as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])


