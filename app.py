from flask import Flask, render_template
from scrape_mars import scrape

app = Flask(__name__, template_folder="mars_templates")

@app.route("/")
def index():
    dict_scrape = scrape()

    return render_template("index.html", dict_scrape=dict_scrape)


if __name__ == "__main__":
    app.run(debug=True)