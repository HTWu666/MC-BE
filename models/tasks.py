from typing import List, Dict
from exceptions.TaskNotFoundException import TaskNotFoundException
from type_schemas.tasks import TaskInTaskDict, TaskInResponse


class Task:
    """
    A model representing a task, providing basic CRUD (Create, Read, Update, Delete) operations.

    Attributes:
        tasks_dict (Dict[int, TaskInTaskDict]): A dictionary acting as the storage for tasks, keyed by task ID.
        last_task_id (int): Tracks the last used task ID to ensure unique identifiers for new tasks.

    Methods:
        get_all: Retrieves a list of all tasks in the mock storage.
        create: Inserts a new task into the mock storage with a unique ID.
        update: Updates the details of an existing task identified by its ID.
        delete: Removes a task from the mock storage by its ID.
    """

    # Mock the database
    tasks_dict: Dict[int, TaskInTaskDict] = {}  # store data in hash table
    last_task_id: int = 0  # For auto increment

    @classmethod
    def get_all(cls) -> List[TaskInResponse]:
        """
        Retrieves all tasks from the mock storage.

        Returns:
            A list of dictionaries, each representing a task with its ID, name, and status.
        """
        tasks_list = [
            {"id": task_id, "name": task["name"], "status": task["status"]}
            for task_id, task in cls.tasks_dict.items()
        ]

        return tasks_list

    @classmethod
    def create(cls, name: str) -> TaskInResponse:
        """
        Inserts a new task with an auto-incremented ID into the mock storage.

        Parameters:
            name (str): The name of the new task.

        Returns:
            A dictionary representing the newly created task, including its ID, name, and status.
        """
        cls.last_task_id += 1
        cls.tasks_dict[cls.last_task_id] = {"name": name, "status": False}
        new_task = {"id": cls.last_task_id, "name": name, "status": False}

        return new_task

    @classmethod
    def update(cls, task_id: int, name: str, status: bool) -> TaskInResponse:
        """
        Updates an existing task's details in the mock storage.

        Parameters:
            task_id (int): The ID of the task to update.
            name (str): The new name for the task.
            status (bool): The new status for the task.

        Returns:
            A dictionary representing the updated task, including its ID, name, and status.

        Raises:
            TaskNotFoundException: If no task with the specified ID exists in the mock storage.
        """
        if task_id not in cls.tasks_dict:
            raise TaskNotFoundException(f"Task with ID {task_id} does not exist.")

        cls.tasks_dict[task_id] = {"name": name, "status": status}

        return {"id": task_id, "name": name, "status": status}

    @classmethod
    def delete(cls, task_id: int) -> None:
        """
        Removes a task from the mock storage by its ID.

        Parameters:
            task_id (int): The ID of the task to delete.

        Returns:
            True if the task was successfully deleted, otherwise raises an exception.

        Raises:
            TaskNotFoundException: If no task with the specified ID exists in the mock storage.
        """
        if task_id not in cls.tasks_dict:
            raise TaskNotFoundException(f"Task with ID {task_id} does not exist.")

        del cls.tasks_dict[task_id]
