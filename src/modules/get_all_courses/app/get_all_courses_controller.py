from .get_all_courses_usecase import GetAllCoursesUsecase
from .get_all_courses_viewmodel import GetAllCoursesViewmodel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class GetAllCoursesController:

    def __init__(self, usecase: GetAllCoursesUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            courses = self.usecase()

            viewmodel = GetAllCoursesViewmodel(
                courses=courses
            )   

            return OK(viewmodel.to_dict())
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except WrongTypeParameter as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])


