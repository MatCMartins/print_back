from .update_event_usecase import UpdateEventUsecase
from .update_event_viewmodel import UpdateEventViewModel
from src.shared.domain.entities.event import Event
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class UpdateEventController:
    def __init__(self, usecase: UpdateEventUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get("event_id") is None:
                raise MissingParameters("event_id")
            
            if request.data.get("name") is not None:
                if not Event.validate_string(request.data.get("name")):
                    raise WrongTypeParameter("name", "str", type(request.data.get("name")).__name__)
            
            if request.data.get("description") is not None:
                if not Event.validate_string(request.data.get("description")):
                    raise WrongTypeParameter("description", "str", type(request.data.get("description")).__name__)
            
            if request.data.get("banner") is not None:
                if not Event.validate_string(request.data.get("banner")):
                    raise WrongTypeParameter("banner", "str", type(request.data.get("banner")).__name__)
            
            if request.data.get("start_date") is not None:
                if not Event.validate_date(request.data.get("start_date")):
                    raise WrongTypeParameter("start_date", "int", type(request.data.get("start_date")).__name__)
            
            if request.data.get("end_date") is not None:
                if not Event.validate_date(request.data.get("end_date")):
                    raise WrongTypeParameter("end_date", "int", type(request.data.get("end_date")).__name__)
            
            if request.data.get("rooms") is not None:
                if not Event.validate_rooms(request.data.get("rooms")):
                    raise WrongTypeParameter("rooms", "dict", type(request.data.get("rooms")).__name__)
            
            if request.data.get("subscribers") is not None:
                if not Event.validate_subscribers(request.data.get("subscribers"), request.data.get("rooms", {})):
                    raise WrongTypeParameter("subscribers", "dict", type(request.data.get("subscribers")).__name__)
                
            updated_event = self.usecase(
                event_id=request.data.get("event_id"),
                name=request.data.get("name"),
                description=request.data.get("description"),
                banner=request.data.get("banner"),
                start_date=request.data.get("start_date"),
                end_date=request.data.get("end_date"),
                rooms=request.data.get("rooms"),
                subscribers=request.data.get("subscribers")
            )

            viewmodel = UpdateEventViewModel(
                event_id=updated_event.event_id,
                name=updated_event.name,
                description=updated_event.description,
                banner=updated_event.banner,
                start_date=updated_event.start_date,
                end_date=updated_event.end_date,
                rooms=updated_event.rooms,
                subscribers=updated_event.subscribers
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
