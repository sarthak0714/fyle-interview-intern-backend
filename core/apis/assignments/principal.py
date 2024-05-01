from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema

principal_assignments_resources = Blueprint("principal_assignments_resources", __name__)


@principal_assignments_resources.route("/assignments", methods=["GET"])
@decorators.authenticate_principal
def list_graded_assignments(p):
    """Return a list of graded Assignments"""
    assignments = Assignment.query.filter(Assignment.state.in_(["GRADED"])).all()
    assignment_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignment_dump)


@principal_assignments_resources.route(
    "/assignments/grade", methods=["POST"], strict_slashes=False
)
@decorators.accept_payload
@decorators.authenticate_principal
def principal_grade_assignment(p, payload):
    grade_assignment_payload = AssignmentGradeSchema().load(payload)

    assignment = Assignment.get_by_id(payload.get("id"))
    if assignment.state != "DRAFTED":
        graded_assignment = Assignment.mark_grade(
            _id=grade_assignment_payload.id,
            grade=grade_assignment_payload.grade,
            auth_principal=p,
        )
        db.session.commit()
        graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
        return APIResponse.respond(data=graded_assignment_dump)
