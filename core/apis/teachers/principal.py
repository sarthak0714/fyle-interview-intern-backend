from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema

principal_teacher_resources = Blueprint("/principal_teacher_resources", __name__)


@principal_teacher_resources.route("/teachers", methods=["GET"],strict_slashes=False)
@decorators.authenticate_principal
def get_teachers(p):
    """Get List of all Teachers"""
    teachers = Teacher.get_all_teachers()
    teacher_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teacher_dump)


