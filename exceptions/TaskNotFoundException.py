class TaskNotFoundException(Exception):
    """
    Exception raised when a task is not found.

    Attributes:
        - message (str): The error message describing the exception.
    """

    def __init__(self, message="Task not found", error_code=400):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
