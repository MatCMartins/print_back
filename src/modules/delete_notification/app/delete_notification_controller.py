from .delete_notification_usecase import DeleteNotificationsUsecase
from .delete_notification_viewmodel import DeleteNotificationViewmodel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class DeleteNotificationController:

    def __init__(self, usecase: DeleteNotificationsUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('notification_id') is None:
                raise MissingParameters("notification_id")
            
            if type(request.data.get('notification_id')) is not str:
                raise WrongTypeParameter("notification_id", str, type(request.data.get('notification_id')))
            notification = self.usecase(request.data.get('notification_id'))

            viewmodel = DeleteNotificationViewmodel(
                notification_id=notification.notification_id,
                title=notification.title,
                description=notification.description,
                creation_date=notification.creation_date,
                has_seen=notification.has_seen
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

