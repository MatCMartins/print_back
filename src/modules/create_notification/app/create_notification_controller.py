from .create_notification_usecase import CreateNotificationUsecase
from .create_notification_viewmodel import CreateNotificationViewModel
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, Created
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.domain_errors import EntityError

class CreateNotificationController:
    def __init__(self, usecase: CreateNotificationUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            params = ["title", "description", "creation_date", "has_seen"]

            for param in params:
                if request.data.get(param) is None:
                    raise MissingParameters(param)

            notification = self.usecase(
                title=request.data.get("title"),
                description=request.data.get("description"),
                creation_date=request.data.get("creation_date"),
                has_seen=request.data.get("has_seen")
            )

            viewmodel = CreateNotificationViewModel(
                notification_id=notification.notification_id,
                title=notification.title,
                description=notification.description,
                creation_date=notification.creation_date,
                has_seen=notification.has_seen
            )

            return Created(viewmodel.to_dict())
        
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except EntityError as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])
    
