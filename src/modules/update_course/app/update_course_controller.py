from .update_course_usecase import UpdateCourseUsecase
from .update_course_viewmodel import UpdateCourseViewmodel
from src.shared.domain.entities.course import Course
from src.shared.domain.repositories.course_repository_interface import ICourseRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, NotFound, InternalServerError

class UpdateCourseController:
    def __init__(self, usecase: UpdateCourseUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get("course_id") is None:
                raise MissingParameters("course_id")
            
            if request.data.get("name") is not None:
                if Course.validate_parameters(request.data.get("name")) is False:
                    raise WrongTypeParameter("name", str, str(type(request.data.get("name"))))
            
            if request.data.get("course_photo") is not None:
                if Course.validate_parameters(request.data.get("course_photo")) is False:
                    raise WrongTypeParameter("course_photo", str, str(type(request.data.get("course_photo"))))
            
            if request.data.get("coordinator") is not None:
                if Course.validate_parameters(request.data.get("coordinator")) is False:
                    raise WrongTypeParameter("coordinator", str, str(type(request.data.get("coordinator"))))
            
            if request.data.get("coordinator_photo") is not None:
                if Course.validate_parameters(request.data.get("coordinator_photo")) is False:
                    raise WrongTypeParameter("coordinator_photo", str, str(type(request.data.get("coordinator_photo"))))
            
            if request.data.get("description") is not None:
                if Course.validate_parameters(request.data.get("description")) is False:
                    raise WrongTypeParameter("description", str, str(type(request.data.get("description"))))
            
            if request.data.get("link") is not None:
                if Course.validate_parameters(request.data.get("link")) is False:
                    raise WrongTypeParameter("link", str, str(type(request.data.get("link"))))
                    
                
            
            

            response = self.usecase(
                course_id=request.data.get("course_id"),
                name=request.data.get("name"),
                course_photo=request.data.get("course_photo"),
                coordinator=request.data.get("coordinator"),
                coordinator_photo=request.data.get("coordinator_photo"),
                description=request.data.get("description"),
                link=request.data.get("link")
            )

            viewmodel = UpdateCourseViewmodel(
                course_id=response.course_id,
                name=response.name,
                course_photo=response.course_photo,
                coordinator=response.coordinator,
                coordinator_photo=response.coordinator_photo,
                description=response.description,
                link=response.link
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
        