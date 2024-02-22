from flask import Blueprint, jsonify
from schemas.task_schema import CreateTask, UpdateTask
from models.tasks import Task
from exceptions.tasks import TaskNotFoundException
from utils.validation import validate_input

# Create a Flask Blueprint
task_bp = Blueprint("task_bp", __name__)


@task_bp.route("/v1/tasks")
def get_tasks():
    try:
        # get all tasks in tasks list
        tasks_list = Task.get_all()

        return jsonify({"result": tasks_list}), 200
    except Exception as e:
        return jsonify({"errors": str(e)}), 500


@task_bp.route("/v1/task", methods=["POST"])
@validate_input(CreateTask)
def create_task(validated_data):
    try:
        # insert a new task into tasks list
        new_task = Task.create(name=validated_data.name)

        return jsonify({"result": new_task}), 201
    except Exception as e:
        return jsonify({"errors": str(e)}), 500


@task_bp.route("/v1/task/<int:id>", methods=["PUT"])
@validate_input(UpdateTask)
def update_task(id, validated_data):
    try:
        # data validation
        if id != validated_data.id:
            return (
                jsonify({"errors": "ID in URL does not match ID in request body."}),
                400,
            )

        # update task
        updated_task = Task.update(id, validated_data.name, validated_data.status)

        return jsonify({"result": updated_task}), 200
    except TaskNotFoundException as e:
        return jsonify({"errors": str(e)}), 400
    except Exception as e:
        return jsonify({"errors": str(e)}), 500


@task_bp.route("/v1/task/<int:id>", methods=["DELETE"])
def delete_task(id):
    try:
        # delete task
        Task.delete(id)

        return jsonify({"message": f"Task #{id} has been deleted"}), 200
    except TaskNotFoundException as e:
        return jsonify({"errors": str(e)}), 400
    except Exception as e:
        return jsonify({"errors": str(e)}), 500
