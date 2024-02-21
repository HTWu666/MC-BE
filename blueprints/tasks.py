from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from schemas.task_schema import CreateTask, UpdateTask
from utils.search import binary_search

task_bp = Blueprint("task_bp", __name__)

# mock a table in database
tasks_list = []


@task_bp.route("/v1/tasks")
def get_tasks():
    try:
        # get all tasks in tasks_list
        tasks = tasks_list

        return jsonify({"result": tasks}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@task_bp.route("/v1/task", methods=["POST"])
def create_task():
    try:
        # data validation
        task_data = CreateTask(**request.json)

        # insert new task into tasks_list
        if tasks_list:
            task_id = tasks_list[-1]["id"] + 1  # id is auto increment
        else:
            task_id = 1  # the first task id
        new_task = {
            "id": task_id,
            "name": task_data.name,
            "status": 0,  # status is false by default
        }
        tasks_list.append(new_task)

        return jsonify({"result": new_task}), 201
    except ValidationError as e:
        return jsonify({"errors": e.errors()[0]["msg"]}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@task_bp.route("/v1/task/<int:id>", methods=["PUT"])
def update_task(id):
    try:
        # data validation
        task_data = UpdateTask(**request.json)
        if id != task_data.id:
            return (
                jsonify({"errors": "ID in URL does not match ID in request body."}),
                400,
            )

        # find the match task and update it
        task_index = binary_search(tasks_list, id)
        if task_index == -1:
            return jsonify({"errors": "The updated task doesn't exist."}), 400
        tasks_list[task_index] = task_data.model_dump()

        return jsonify({"result": task_data.model_dump()}), 200
    except ValidationError as e:
        return jsonify({"errors": e.errors()[0]["msg"]}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@task_bp.route("/v1/task/<int:id>", methods=["DELETE"])
def delete_task(id):
    try:
        # find the match task and delete it
        task_index = binary_search(tasks_list, id)
        if task_index == -1:
            return jsonify({"errors": "The deleted task doesn't exist."}), 400
        del tasks_list[task_index]

        return jsonify({"message": f"Task #{id} has been deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
