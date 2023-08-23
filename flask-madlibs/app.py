from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/home')
def show_home():
    #display dropdown menu that selects between silly_story +
    # excited_story
    madlib_templates = [silly_story, excited_story]

    return render_template('home.html',
                           story_templates = madlib_templates)

@app.get('/questions')
def load_questions():
    """"load the prompt for madlibs words"""
    return render_template('questions.html',
                           words=silly_story.prompts)

@app.get('/results')
def show_story():
    """After getting user's answers to prompt, display story"""
    #grab data from form submission
    answers = request.args
    #set answers in render_template to result of get_result_text()
    full_story = silly_story.get_result_text(answers)
    return render_template('results.html',
                           story = full_story)
