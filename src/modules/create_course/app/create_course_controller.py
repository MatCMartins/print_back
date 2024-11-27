from .create_course_usecase import CreateCourseUsecase
from .create_course_viewmodel import CreateCourseViewModel
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, Created
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.domain_errors import EntityError

class CreateCourseController:
    def __init__(self, usecase: CreateCourseUsecase):
        self.usecase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            params = ["name", "course_photo", "coordinator", "coordinator_photo", "description", "link"]

            for param in params:
                if request.data.get(param) is None:
                    raise MissingParameters(param)

            stu_org = self.usecase(
                name=request.data["name"],
                course_photo=request.data["course_photo"],
                coordinator=request.data["coordinator"],
                coordinator_photo=request.data["coordinator_photo"],
                description=request.data["description"],
                link=request.data.get("link")
            )

            viewmodel = CreateCourseViewModel(
                course_id=stu_org.course_id,
                name=stu_org.name,
                course_photo=stu_org.course_photo,
                coordinator=stu_org.coordinator,
                coordinator_photo=stu_org.coordinator_photo,
                description=stu_org.description,
                link=stu_org.link
            )

            return Created(viewmodel.to_dict())
        
        except MissingParameters as e:
            return BadRequest(body=e.message)
        except EntityError as e:
            return BadRequest(body=e.message)
        except Exception as e:
            return InternalServerError(body=e.args[0])
    
