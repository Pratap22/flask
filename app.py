from flask import Flask, render_template, jsonify, session, flash, request

app = Flask(
    __name__,
    template_folder="./templates",
    static_folder="./static",
)


@app.after_request
def add_headers(response):
    white_origin = ["http://localhost:3000"]
    if (
        "HTTP_ORIGIN" in request.environ
        and request.environ["HTTP_ORIGIN"] in white_origin
    ):
        response.headers.add("Content-Type", "application/json")
        response.headers.add("Access-Control-Allow-Origin",
                             request.headers["Origin"])
        response.headers.add("Access-Control-Allow-Methods", "GET")
        response.headers.add("Access-Control-Allow-Credentials", "true")
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization"
        )
        response.headers.add(
            "Access-Control-Expose-Headers",
            "Content-Type,Content-Length,Authorization,X-Pagination",
        )
    return response


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/json")
def json_response():
    response = {"name": "Pratap", "age": 29}
    return jsonify([response])


if __name__ == "__main__":
    app.run(debug=True)
