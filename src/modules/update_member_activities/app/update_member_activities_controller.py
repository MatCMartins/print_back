from .update_member_activities_usecase import UpdateMemberActivitiesUsecase
from .update_member_activities_viewmodel import UpdateMemberActivitiesViewmodel
from src.shared.domain.entities.event import Event
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class UpdateMemberActivitiesController:
    def __init__(self, usecase: UpdateMemberActivitiesUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get("event_id") is None:
                raise MissingParameters("event_id")
            
            if request.data.get("member_id") is None:
                raise MissingParameters("event_id")
            
            
            if request.data.get("activities") is None:
                raise MissingParameters("activities")
                
            updated_member = self.usecase(
                event_id=request.data.get("event_id"),
                member_id=request.data.get("member_id"),
                activities=request.data.get("activities")
            )

            viewmodel = UpdateMemberActivitiesViewmodel(
                member_id=updated_member.member_id,
                name=updated_member.name,
                email=updated_member.email,
                activities=updated_member.activities
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
