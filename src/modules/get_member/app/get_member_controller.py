from .get_member_usecase import GetMemberUsecase
from .get_member_viewmodel import GetMemberViewmodel
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class GetMemberController:

    def __init__(self, usecase: GetMemberUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('member_id') is None:
                raise MissingParameters("member_id")
            
            if type(request.data.get('member_id')) is not str:
                raise WrongTypeParameter("member_id", str, type(request.data.get('member_id')))
            
            member = self.usecase(request.data.get('member_id'))
            
            viewmodel = GetMemberViewmodel(
                member_id=member.member_id,
                name=member.name,
                email=member.email,
                activities=member.activities
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

