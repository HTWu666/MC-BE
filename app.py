from flask import Flask, jsonify
from blueprints.tasks import task_bp

# Initialize a Flask application instance.
app = Flask(__name__)


# Register the 'task_bp' blueprint
app.register_blueprint(task_bp, url_prefix="/api")


# page not found
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message": "This page does not exist", "error": str(error)}), 404


# global error handler
@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({"message": "An error occurred", "error": str(error)}), 500


# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
