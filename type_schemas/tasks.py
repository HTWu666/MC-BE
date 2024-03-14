from typing import TypedDict


class TaskInTaskDict(TypedDict):
    """
    Represents the structure of a task within the tasks dictionary.

    Attributes:
        name (str): The name of the task.
        status (bool): The current status of the task, where False indicates incomplete.
    """

    name: str
    status: bool


class TaskInResponse(TypedDict):
    """
    Represents the structure of a task used in API responses.

    Attributes:
        id (int): The unique identifier for the task.
        name (str): The name of the task.
        status (bool): The current status of the task, where False indicates incomplete.
    """

    id: int
    name: str
    status: bool
