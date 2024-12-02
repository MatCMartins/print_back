from .get_all_events_usecase import GetAllEventsUsecase
from .get_all_events_viewmodel import GetAllEventsViewModel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError

class GetAllEventsController:

    def __init__(self, usecase: GetAllEventsUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            events = self.usecase()

            viewmodel = GetAllEventsViewModel(events=events)

            return OK(viewmodel.to_dict())

        except MissingParameters as e:
            return BadRequest(body=e.message)
        except WrongTypeParameter as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])
