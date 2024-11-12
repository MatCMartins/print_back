from .delete_course_usecase import DeleteCourseUsecase
from .delete_course_viewmodel import DeleteCourseViewmodel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class DeleteCourseController:

    def __init__(self, usecase: DeleteCourseUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('course_id') is None:
                raise MissingParameters("course_id")
            
            if type(request.data.get('course_id')) is not str:
                raise WrongTypeParameter("course_id", str, type(request.data.get('course_id')))
            
            course = self.usecase(request.data.get('course_id'))

            viewmodel = DeleteCourseViewmodel(
                course_id=course.course_id,
                name=course.name,
                course_photo=course.course_photo,
                coordinator=course.coordinator,
                coordinator_photo=course.coordinator_photo,
                description=course.description,
                link=course.link
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

