from .get_all_notifications_usecase import GetAllNotificationsUsecase
from .get_all_notifications_viewmodel import GetAllNotificationsViewmodel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class GetAllNotificationsController:

    def __init__(self, usecase: GetAllNotificationsUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            notifications = self.usecase()

            viewmodel = GetAllNotificationsViewmodel(
                notifications=notifications
            )   

            return OK(viewmodel.to_dict())
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except WrongTypeParameter as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])


