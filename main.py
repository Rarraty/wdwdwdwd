from flask import Flask, request, render_template

app = Flask(__name__)

messages = []

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        username = request.form["username"]
        message = request.form["message"]
        messages.append((username, message))
    return render_template("airpods.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
