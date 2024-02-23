from typing import Tuple
from flask import Flask, jsonify, Response
from flasgger import Swagger
from blueprints.tasks import task_bp

app = Flask(__name__)
swagger = Swagger(app, template_file="docs/swagger.yml")

app.register_blueprint(task_bp, url_prefix="/api")


# page not found
@app.errorhandler(404)
def page_not_found(error) -> Tuple[Response, int]:
    """
    Handle 404 errors by returning an error response.

    Parameters:
        - error: The error object provided by Flask.

    Returns:
        - A tuple containing a Flask jsonify response and the HTTP status code.
    """
    return jsonify({"errors": str(error)}), 404


@app.route("/test/error")
def test_error_handler():
    """
    Test endpoint to demonstrate global exception handling by raising an exception.
    """
    raise Exception("Test exception for error handling.")


# Global exception handler
@app.errorhandler(Exception)
def handle_exception(error) -> Tuple[Response, int]:
    """
    Handle general exceptions by returning an error response.

    Parameters:
        - error: The error object provided by Flask.

    Returns:
        - On unexpected errors, returns a JSON object with an error message and a 500 status code.
    """
    return jsonify({"errors": str(error)}), 500


# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
