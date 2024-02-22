from pydantic import BaseModel, Field


class CreateTask(BaseModel):
    """
    Represents the schema for creating a new task.

    Attributes:
        name (str): The name of the task.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        json_schema_extra={
            "error_messages": {
                "min_length": "Name must not be empty.",
                "max_length": "Name must not exceed 50 characters.",
            }
        },
    )


class UpdateTask(BaseModel):
    """
    Represents the schema for updating an existing task.

    Attributes:
        id (int): The ID of the task to be updated.
        name (str): The new name of the task.
        status (bool): The new status of the task.
    """

    id: int = Field(
        ...,
        gt=0,
        json_schema_extra={"error_messages": {"gt": "ID must be a positive integer."}},
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        json_schema_extra={
            "error_messages": {
                "min_length": "Name must not be empty.",
                "max_length": "Name must not exceed 50 characters.",
            }
        },
    )
    status: bool
