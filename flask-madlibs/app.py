from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story, silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

TEMPLATES = {
    'silly': silly_story,
    'excited': excited_story
}

@app.get('/create-template')
def show_options():
    """make your very own template on this site"""
    return render_template('create-template.html')

@app.get('/home')
def show_home():
    """displays a dropdown of possible templates to choose"""
    #display dropdown menu that selects between silly_story +
    # excited_story

    #check request.args for which checkboxes were chosen
    #then create new story instance based off args
    words = []
    for (key, val) in request.args.items():
        if key != 'story-text':
            words.append(key)
    #add new story to templates
    text = request.args['story-text']
    new_story = Story(words, text)
    TEMPLATES['new'] = new_story

    #madlib_templates = ['silly', 'excited', 'new']

    return render_template('home.html',
                           story_templates = TEMPLATES.keys())

@app.get('/questions')
def load_questions():
    """"load the prompt for madlibs words"""
    choice = request.args['story_template']

    return render_template('questions.html',
                           words=TEMPLATES[choice].prompts,
                           story_template=choice)

@app.get('/results')
def show_story():
    """After getting user's answers to prompt, display story"""
    answers = {}
    for (key, val) in request.args.items():
        if key != 'story_template':
            answers[key] = val

    choice = request.args['story_template']
    full_story = TEMPLATES[choice].get_result_text(answers)
    return render_template('results.html',
                           story = full_story)
