"""
Flask web application to run LinkedIn automation scripts via a web interface.
Provides endpoints to trigger all scripts and display progress in real-time.
"""
from flask import Flask, render_template, Response
import sys
import time
from scripts import extract_competitor_likers, extract_liker_details, filter_likers, send_message

app = Flask(__name__)

@app.route("/")
def index():
    """Render the main index page."""
    return render_template("index.html")

@app.route("/run-all", methods=["GET"])
def run_all_scripts():
    """
    Run all LinkedIn automation scripts in sequence and stream their output to the client.
    Returns:
        Response: Streaming plain text output of script execution.
    """
    def generate():
        try:
            yield "\n=== Starting All Scripts ===\n"

            # Run Extract Competitor Likers script
            yield "\n=== Running Extract Competitor Likers ===\n"
            sys.stdout.flush()
            extract_competitor_likers.run()
            yield "=== Completed Extract Competitor Likers ===\n"

            # Run Extract Liker Details script
            yield "\n=== Running Extract Liker Details ===\n"
            sys.stdout.flush()
            extract_liker_details.run()
            yield "=== Completed Extract Liker Details ===\n"

            # Run Filter Likers script
            yield "\n=== Running Filter Likers ===\n"
            sys.stdout.flush()
            filter_likers.run()
            yield "=== Completed Filter Likers ===\n"

            # Run Send Message script
            yield "\n=== Running Send Message ===\n"
            sys.stdout.flush()
            send_message.run()
            yield "=== Completed Send Message ===\n"

            yield "\n=== All Scripts Completed Successfully ===\n"
        except Exception as e:
            # Catch and display any errors during script execution
            yield f"\nError: {str(e)}\n"

    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    # Run the Flask app in debug mode on port 5000
    app.run(debug=True, port=5000)
