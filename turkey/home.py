from flask import render_template, request, flash
from flask.ext.login import current_user
from turkey import app
from turkey.models import Goal, Task, CompletedTask, TaskBreak
import datetime
import calendar
from turkey.utils import get_tasks_history, render_turkey, int_or_null
from wtforms import Form, SelectField
from questions import get_package


def get_question():
     return {
        'question': 'Who is foo bar',
        'answers': ['Newton', 'Lincoln'],
        'correct_answer': 0
    }

class AnswerForm(Form):
    answer = SelectField(
        'Answer',
        coerce=int_or_null,
    )

previous_answer = None
previous_options = []

def home_view():
    form = AnswerForm(request.form)
    global previous_options
    form.answer.choices = previous_options
    global previous_answer


    if request.method == 'POST' and form.validate():
        if form.answer.data == previous_answer:
            flash('You got it right!', 'success')
        else:
            flash('Sorry, that was wrong.', 'danger')
        
    quiz_question = get_package()
    answers = [(quiz_question['answers'].index(value), value) for value in quiz_question['answers']]
    form.answer.choices = answers
    question = quiz_question['question']
    previous_answer = quiz_question['correct_answer']
    previous_options = answers
    return render_template("home.html", question=question, form=form)
