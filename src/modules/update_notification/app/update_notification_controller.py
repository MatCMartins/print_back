from .update_notification_usecase import UpdateNotificationUsecase
from .update_notification_viewmodel import UpdateNotificationViewmodel
from src.shared.domain.entities.notification import Notification
from src.shared.domain.repositories.notification_repository_interface import INotificationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class UpdateNotificationController:
    def __init__(self, usecase: UpdateNotificationUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get("notification_id") is None:
                raise MissingParameters("notification_id")
            
            if request.data.get("title") is not None:
                if Notification.validate_parameters(request.data.get("title")) is False:
                    raise WrongTypeParameter("title", str, str(type(request.data.get("title"))))
            
            if request.data.get("description") is not None:
                if Notification.validate_parameters(request.data.get("description")) is False:
                    raise WrongTypeParameter("description", str, str(type(request.data.get("description"))))
            
            if request.data.get("creation_date") is not None:
                if Notification.validate_creation_date(request.data.get("creation_date")) is False:
                    raise WrongTypeParameter("creation_date", int, str(type(request.data.get("creation_date"))))
            
            if request.data.get("has_seen") is not None:
                if Notification.validate_creation_has_seen(request.data.get("has_seen")) is False:
                    raise WrongTypeParameter("has_seen", list, str(type(request.data.get("has_seen"))))
                
            
            
            viewmodel = UpdateNotificationViewmodel(
                notification_id=request.data.get("notification_id"),
                title=request.data.get("title"),
                description=request.data.get("description"),
                creation_date=request.data.get("creation_date"),
                has_seen=request.data.get("has_seen"),
            )

            response = self.usecase(
                notification_id=request.data.get("notification_id"),
                title=request.data.get("title"),
                description=request.data.get("description"),
                creation_date=request.data.get("creation_date"),
                has_seen=request.data.get("has_seen"),
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
        