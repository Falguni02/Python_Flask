from flask import Blueprint, render_template, request, flash
from flask_login import login_required, logout_user, current_user
from .models import Note
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            flash('Note added!', category='success')

    return render_template("home.html", user = current_user)



