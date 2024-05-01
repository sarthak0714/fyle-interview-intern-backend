from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema

principal_assignments_resources = Blueprint("principal_assignments_resources", __name__)


@principal_assignments_resources.route("/assignments", methods=["GET"],strict_slashes=False)
@decorators.authenticate_principal
def list_graded_assignments(p):
    """Return a list of submitted and graded Assignments"""
    assignments_graded = Assignment.get_assignments_by_principal()
    assignment_dump_graded = AssignmentSchema().dump(assignments_graded, many=True)
    return APIResponse.respond(data=assignment_dump_graded)


@principal_assignments_resources.route(
    "/assignments/grade", methods=["POST"], strict_slashes=False
)
@decorators.accept_payload
@decorators.authenticate_principal
def principal_grade_assignment(p, payload):
    """Grade Assigment or Regrade already Graded Assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(payload)

    graded_assignment = Assignment.mark_grade(
            _id=grade_assignment_payload.id,
            grade=grade_assignment_payload.grade,
            auth_principal=p,
        )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
