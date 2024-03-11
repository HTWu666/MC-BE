from functools import wraps
from flask import request, jsonify
from pydantic import ValidationError


def validate_input(validation_model):
    """
    Decorator function for validating input data using a Pydantic model.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.content_type != "application/json":
                return jsonify({"errors": "Invalid or missing JSON"}), 400
            try:
                validated_data = validation_model(**request.json)
                return func(*args, **kwargs, validated_data=validated_data)
            except ValidationError as e:
                return jsonify({"errors": e.errors()[0]["msg"]}), 400

        return wrapper

    return decorator
