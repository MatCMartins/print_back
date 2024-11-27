from .create_event_usecase import CreateEventUsecase
from .create_event_viewmodel import CreateEventViewModel
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, Created
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.domain_errors import EntityError

class CreateEventController:
    def __init__(self, usecase: CreateEventUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            params = ["name", "description", "banner", "start_date", "end_date", "rooms", "subscribers"]

            for param in params:
                if request.data.get(param) is None:
                    raise MissingParameters(param)

            event = self.usecase(
                name=request.data.get("name"),
                description=request.data.get("description"),
                banner=request.data.get("banner"),
                start_date=request.data.get("start_date"),
                end_date=request.data.get("end_date"),
                rooms=request.data.get("rooms"),
                subscribers=request.data.get("subscribers")
            )

            viewmodel = CreateEventViewModel(
                event_id=event.event_id,
                name=event.name,
                description=event.description,
                banner=event.banner,
                start_date=event.start_date,
                end_date=event.end_date,
                rooms=event.rooms,
                subscribers=event.subscribers
            )

            return Created(viewmodel.to_dict())
        
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except EntityError as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])
