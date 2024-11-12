from .get_course_usecase import GetCourseUsecase
from .get_course_viewmodel import GetCourseViewmodel
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class GetCourseController:

    def __init__(self, usecase: GetCourseUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('course_id') is None:
                raise MissingParameters("course_id")
            
            if type(request.data.get('course_id')) is not str:
                raise WrongTypeParameter("course_id", str, type(request.data.get('course_id')))
            
            stu_org = self.usecase(request.data.get('course_id'))
            
            viewmodel = GetCourseViewmodel(
                course_id=stu_org.course_id,
                name=stu_org.name,
                description=stu_org.description,
                coordinator=stu_org.coordinator,
                link=stu_org.link,
                course_photo=stu_org.course_photo,
                coordinator_photo=stu_org.coordinator_photo
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

