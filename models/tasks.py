from typing import List, TypedDict, Dict
from exceptions.tasks import TaskNotFoundException


class TaskDict(TypedDict):
    """
    Represents the structure of a task dictionary in tasks list.

    Attributes:
        - id (int): The unique identifier of the task.
        - name (str): The name of the task.
        - status (bool): The status of the task.
    """

    id: int
    name: str
    status: bool


class Task:
    """
    Represents a task model with basic CRUD operations.

    Attributes:
        - tasks_list (List[TaskDict]): A list containing dictionaries representing tasks.
        - last_task_id (int): The last ID used for auto-incrementing new task id.

    Methods:
        - get_all(cls) -> List[TaskDict]: Retrieves all tasks from the tasks list.
        - create(cls, name: str, status: bool = False) -> TaskDict: Inserts a new task.
        - update(cls, task_id: int, name: str, status: bool) -> TaskDict: Updates an existing task.
        - delete(cls, task_id: int) -> bool: Deletes a task.
    """

    # Mock the collection in database
    task = Dict[str, str]
    tasks_dict: Dict[int, task] = {}
    last_task_id: int = 0  # For auto increment

    @classmethod
    def get_all(cls) -> List[TaskDict]:
        """
        Retrieves all tasks from the list.

        Returns:
            - List[TaskDict]: A list of all task dictionaries.
        """
        tasks_list = []
        for k, v in cls.tasks_dict.items():
            tasks_list.append({"id": k, "name": v["name"], "status": v["status"]})

        return tasks_list

    @classmethod
    def create(cls, name: str, status: bool = False) -> TaskDict:
        """
        Inserts a new task into the tasks list with an auto-incremented ID.

        Parameters:
            - name (str): The name of the task.
            - status (bool): The status of the task, False by default.

        Returns:
            - TaskDict: The created task dictionary.
        """
        cls.last_task_id += 1
        cls.tasks_dict[cls.last_task_id] = {"name": name, "status": status}
        new_task = {"id": cls.last_task_id, "name": name, "status": status}

        return new_task

    @classmethod
    def update(cls, task_id: int, name: str, status: bool) -> TaskDict:
        """
        Updates a task identified by its ID.

        Parameters:
            - task_id (int): The ID of the task to update.
            - name (str): The new name of the task.
            - status (bool): The new status of the task.

        Returns:
            - TaskDict: The updated task dictionary.

        Raises:
            - TaskNotFoundException: If no task with the specified ID exists.
        """
        if task_id not in cls.tasks_dict:
            raise TaskNotFoundException(f"Task with ID {task_id} does not exist.")

        cls.tasks_dict[task_id] = {"name": name, "status": status}

        return {"id": task_id, "name": name, "status": status}

    @classmethod
    def delete(cls, task_id: int) -> bool:
        """
        Deletes a task identified by its ID.

        Parameters:
            - task_id (int): The ID of the task to delete.

        Returns:
            - bool: True if the task was successfully deleted.

        Raises:
            - TaskNotFoundException: If no task with the specified ID exists.
        """
        if task_id not in cls.tasks_dict:
            raise TaskNotFoundException(f"Task with ID {task_id} does not exist.")

        del cls.tasks_dict[task_id]

        return True
