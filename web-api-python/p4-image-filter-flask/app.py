from flask import Flask, request, send_file, jsonify
from werkzeug.wrappers import response
from bin.filters import apply_filter

app = Flask(__name__)

filter_available = [
    "blur",
    "contour",
    "detail",
    "edge_enhance",
    "edge_enhance_more",
    "emboss",
    "find_edges",
    "sharpen",
    "smooth",
    "smooth_more",
]

@app.route("/", methods=["GET", "POST"])
def index():
    """TODO
    1. Return instructions that 
    a) specifies which filters are available,
    b) specifies and the method format
    """
    response = {
        "filters_available": filter_available,
        "usage": { "http_method":"POST", "URL":"/<filter_available>/"}
    }
    return jsonify(response)

@app.post("/<filter>")
def image_filter(filter):
    """
    TODO:
    1. Checks if the provided filter is available, if not, return an error.
    2. Check if a file has been provided in the POST request, if not return an error
    3. Apply the filter using apply_filter() method from bin.filters
    4. Return the filtered image as response
    """
    if filter not in filter_available:
        response={"error":"incorrect filter"}
        return jsonify(response)
    file = request.files["image"]
    if not file:
        response = {"error":"no file provided"}
        return jsonify(response)
    filtered_image = apply_filter(file, filter)
    return send_file(filtered_image, mimetype="image/JPEG")

if __name__ == "__main__":
    app.run()

