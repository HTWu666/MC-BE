import time
from typing import Tuple
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, Response, request
from flasgger import Swagger
from blueprints.tasks import task_bp

app = Flask(__name__)
swagger = Swagger(app, template_file="docs/swagger.yml")

# Configure logging
handler = RotatingFileHandler("./logs/app.log", maxBytes=10000, backupCount=3)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.before_request
def before_request():
    """
    Log request details before processing it.

    Captures and logs the HTTP method, path, headers, and query parameters
    of the incoming request. Also, records the start time for calculating
    the request's response time.
    """
    request.start_time = time.time()
    headers = dict(request.headers)
    query_params = request.args
    logger.info(
        "Request: %s %s, Headers: %s, Query Params: %s",
        request.method,
        request.path,
        headers,
        query_params,
    )


@app.after_request
def after_request(response):
    """
    Log response details after processing the request.

    Logs the HTTP status code, request path, response time (in milliseconds),
    user-agent, and the IP address of the client. If the response time cannot
    be calculated, logs 'Unknown' as the response time.

    Parameters:
    - response: The Flask response object to be returned to the client.

    Returns:
    - The unmodified response object, to comply with Flask's after_request requirements.
    """
    if hasattr(request, "start_time"):
        response_time = (time.time() - request.start_time) * 1000
        response_time_str = f"{response_time:.2f} ms"
    else:
        response_time_str = "Unknown"

    logger.info(
        "Response: %s, Route: %s, Response Time: %s, User-Agent: %s, IP: %s",
        response.status_code,
        request.path,
        response_time_str,
        request.headers.get("User-Agent"),
        request.remote_addr,
    )

    return response


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
    app.run(host="0.0.0.0", port=5000, debug=True)
