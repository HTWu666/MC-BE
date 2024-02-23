from typing import Tuple
from flask import Blueprint, jsonify, Response
from schemas.task_schema import CreateTask, UpdateTask
from models.tasks import Task
from exceptions.tasks import TaskNotFoundException
from utils.validation import validate_input


# Create a Flask Blueprint
task_bp = Blueprint("task_bp", __name__)


@task_bp.route("/v1/tasks")
def get_tasks() -> Tuple[Response, int]:
    """
    Fetches and returns all tasks in JSON format.

    Returns:
        - On success, returns the tasks list with a 200 status code.
        - On unexpected errors, returns a JSON object with an error message and a 500 status code.
    """
    try:
        tasks_list = Task.get_all()

        return jsonify({"result": tasks_list}), 200
    except Exception as e:
        return jsonify({"errors": str(e)}), 500


@task_bp.route("/v1/task", methods=["POST"])
@validate_input(CreateTask)
def create_task(validated_data: CreateTask) -> Tuple[Response, int]:
    """
    Creates a new task based on validated input data and returns it in JSON format.

    Parameters:
        - validated_data (CreateTask): The data validated by the `CreateTask` model. It is automatically
            injected by the `@validate_input(CreateTask)` decorator.

    Returns:
        - On successful creation, returns a JSON object containing the new task and a 201 status code.
        - On validation failure (handled by the decorator), returns a JSON object with error details and a 400 status code.
        - On unexpected errors, returns a JSON object with an error message and a 500 status code.
    """
    try:
        new_task = Task.create(name=validated_data.name)

        return jsonify({"result": new_task}), 201
    except Exception as e:
        return jsonify({"errors": str(e)}), 500


@task_bp.route("/v1/task/<int:id>", methods=["PUT"])
@validate_input(UpdateTask)
def update_task(id: int, validated_data: UpdateTask) -> Tuple[Response, int]:
    """
    Updates an existing task based on the provided ID and validated input data, then returns the updated task in JSON format.

    Parameters:
        - id (int): The ID of the task to be updated, obtained from the URL.
        - validated_data (UpdateTask): The data validated by the `UpdateTask` model, injected by the `@validate_input(UpdateTask)` decorator.

    Returns:
        - On successful update, returns a JSON object containing the updated task and a 200 status code.
        - If the ID in the URL does not match the ID in the request body, returns a 400 status code with an error message.
        - If the task to be updated is not found, returns a 400 status code with an error message.
        - On unexpected errors, returns a JSON object with an error message and a 500 status code.

    Raises:
        - TaskNotFoundException: If no task matches the provided ID.
    """
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
def delete_task(id: int) -> Tuple[Response, int]:
    """
    Deletes a task identified by its ID.

    Parameters:
        - id (int): The ID of the task to be deleted.

    Returns:
        - A JSON response with a message indicating successful deletion and a 200 status code on success.
        - If the task to be deleted is not found, returns a JSON response with an error message and a 400 status code.
        - On unexpected errors, returns a JSON response with an error message and a 500 status code.

    Raises:
        - TaskNotFoundException: If no task with the specified ID exists.
    """
    try:
        Task.delete(id)

        return jsonify({"message": f"Task #{id} has been deleted"}), 200
    except TaskNotFoundException as e:
        return jsonify({"errors": str(e)}), 400
    except Exception as e:
        return jsonify({"errors": str(e)}), 500
