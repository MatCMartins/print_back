from .subscribe_event_usecase import SubscribeEventUsecase
from .subscribe_event_viewmodel import SubscribeEventViewmodel
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.usecase_errors import UserRegistered
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class SubscribeEventController:

    def __init__(self, usecase: SubscribeEventUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('event_id') is None:
                raise MissingParameters("event_id")
            
            if type(request.data.get('event_id')) is not str:
                raise WrongTypeParameter("event_id", str, type(request.data.get('event_id')))
            
            event = self.usecase(request.data.get('event_id'))

            viewmodel = SubscribeEventViewmodel(
                event_id=event.event_id,
                name=event.name,
                description=event.description,
                banner=event.banner,
                start_date=event.start_date,
                end_date=event.end_date,
                rooms=event.rooms,
                subscribers=event.subscribers
            )


            return OK(viewmodel.to_dict())
        except NoItemsFound as e:
            return BadRequest(body=e.message)
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except WrongTypeParameter as e:
            return BadRequest(body=e.message)
        except UserRegistered as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])

