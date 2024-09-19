from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def select_story():
    return render_template("app.html", stories = stories.values())

@app.route("/questions")
def questions():
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts

    return render_template("questions.html", story_id=story_id, title=story.title, prompts=prompts)



@app.route("/story")
def story_gen():
    story_id = request.args["story_id"]
    story = stories[story_id]
    text = story.generate(request.args)

    return render_template("story.html", title=story.title, text=text)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
