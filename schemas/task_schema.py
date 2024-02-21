from pydantic import BaseModel, Field


class CreateTask(BaseModel):
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
