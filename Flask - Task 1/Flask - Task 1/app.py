from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")

    if name:
        name = name.upper()
    else:
        name = "PROVIDE NAME"

    return render_template("home.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
