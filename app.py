from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story




app = Flask(__name__)
app.config['SECRET_KEY'] = 'yaywhatasecret'
debug = DebugToolbarExtension(app)





@app.route('/')
def form_page():
    """ Routes to the Home Page which is where the user will submit a form """
    prompts = story.prompts

    return render_template('form.html', prompts=prompts)





@app.route('/story')
def show_story():
    """ Puts completed story together for users to be able to view in it's entirety """

    text = story.generate(request.args)

    return render_template('story.html', text=text)


