from .get_all_members_usecase import GetAllMembersUsecase
from .get_all_members_viewmodel import GetAllMembersViewmodel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class GetAllMembersController:

    def __init__(self, usecase: GetAllMembersUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            members = self.usecase()

            viewmodel = GetAllMembersViewmodel(
                members=members
            )   

            return OK(viewmodel.to_dict())
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except WrongTypeParameter as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])


