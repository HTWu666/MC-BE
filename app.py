from typing import Tuple
from flask import Flask, jsonify, Response
from flasgger import Swagger
from blueprints.tasks import task_bp

app = Flask(__name__)
swagger = Swagger(app, template_file="docs/swagger.yml")

app.register_blueprint(task_bp)


@app.errorhandler(404)
def page_not_found(error) -> Tuple[Response, int]:
    """
    Handle 404 errors by returning a custom JSON response.

    Parameters:
        - error: The error object provided by Flask.

    Returns:
        - A tuple containing a Flask jsonify response and the HTTP status code.
    """
    return jsonify({"errors": str(error)}), 404


@app.route("/test/error")
def test_error_handler():
    raise Exception("Test exception for error handling.")


# Global exception handler
@app.errorhandler(Exception)
def handle_exception(error) -> Tuple[jsonify, int]:
    """
    Handle general exceptions by returning a custom JSON response.

    Parameters:
        - error: The error object provided by Flask.

    Returns:
        - On unexpected errors, returns a JSON object with an error message and a 500 status code.
    """
    return jsonify({"message": "An error occurred", "error": str(error)}), 500


# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
