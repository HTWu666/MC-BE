from typing import List
from models.tasks import Task
from type_schemas.tasks import TaskInTaskDict, TaskInResponse


def get_all_tasks() -> List[TaskInTaskDict]:
    return Task.get_all()


def create_task(name) -> TaskInResponse:
    return Task.create(name)


def update_task(id, name, status) -> TaskInResponse:
    return Task.update(id, name, status)


def delete_task(id) -> None:
    Task.delete(id)
