from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.modules.create_member.app.create_member_viewmodel import CreateMemberViewmodel
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, Created
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.domain_errors import EntityError

class CreateMemberController:
    def __init__(self, usecase: CreateMemberUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            params = ["member_id", "name", "email", "activities"]

            for param in params:
                if request.data.get(param) is None:
                    raise MissingParameters(param)

            member = self.usecase(
                member_id=request.data.get("member_id"),
                name=request.data.get("name"),
                email=request.data.get("email"),
                activities=request.data.get("activities")
            )

            viewmodel = CreateMemberViewmodel(
                member_id=member.member_id,
                name=member.name,
                email=member.email,
                activities=member.activities
            )

            return Created(viewmodel.to_dict())
        
        except DuplicatedItem as e:
            return BadRequest(body=e.message)
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except EntityError as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])
    
