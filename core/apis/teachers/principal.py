from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema

principal_teacher_resources = Blueprint("/principal_teacher_resources", __name__)


@principal_teacher_resources.route("/teachers", methods=["GET"])
@decorators.authenticate_principal
def get_teachers(p):
    teachers = Teacher.query.all()
    teacher_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teacher_dump)


