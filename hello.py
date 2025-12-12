from flask import Flask

app = Flask(__name__)  # __name__ -> hello.py // app - master variable


@app.route(
    "/"
)  # endpoint . when user visits "/" represents home page -> the following will return
def hello():
    return "Hello there"


# to run -> flask --app hello run


@app.route("/ping")
def ping():
    return {"Message": "Why are you pinging me ?"}


if __name__ == "__main__":  # to run auto reloded server on code changes
    app.run(debug=True)

# if you dont want to push this file into github use the following code
# mlops_env/ --> add this into gitignore
