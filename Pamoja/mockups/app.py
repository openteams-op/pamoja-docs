from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True  # always run in debug mode (also add --debug to the run command)

SCREENS_DIR = Path(app.root_path) / "templates" / "screens"
SCREENS = sorted(p.stem for p in SCREENS_DIR.glob("*.html"))


@app.get("/")
def gallery():
    return render_template("index.html", screens=SCREENS)


@app.get("/screens/<screen_name>")
def screen(screen_name):
    return render_template(
        f"screens/{screen_name}.html",
        screens=SCREENS,
        screen_name=screen_name,
    )


if __name__ == "__main__":
    app.run(debug=True)