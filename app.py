from flask import Flask, render_template, Response
import sys
import time
from scripts import extract_competitor_likers, extract_liker_details, filter_likers, send_message

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-all", methods=["GET"])
def run_all_scripts():
    def generate():
        try:
            yield "\n=== Starting All Scripts ===\n"

            yield "\n=== Running Extract Competitor Likers ===\n"
            sys.stdout.flush()
            extract_competitor_likers.run()
            yield "=== Completed Extract Competitor Likers ===\n"

            yield "\n=== Running Extract Liker Details ===\n"
            sys.stdout.flush()
            extract_liker_details.run()
            yield "=== Completed Extract Liker Details ===\n"

            yield "\n=== Running Filter Likers ===\n"
            sys.stdout.flush()
            filter_likers.run()
            yield "=== Completed Filter Likers ===\n"

            yield "\n=== Running Send Message ===\n"
            sys.stdout.flush()
            send_message.run()
            yield "=== Completed Send Message ===\n"

            yield "\n=== All Scripts Completed Successfully ===\n"
        except Exception as e:
            yield f"\nError: {str(e)}\n"

    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
