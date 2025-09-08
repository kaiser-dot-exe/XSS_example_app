from flask import Flask, render_template
import routes_stored

app = Flask(__name__)

# Stored XSS route’larını register et
app.register_blueprint(routes_stored.bp)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)



