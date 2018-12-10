# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from .forms import UserCreationForm


bp = Blueprint('users', __name__, url_prefix='/users')

users = {}


@bp.route('/', methods=['GET', 'POST'])
def show_users():   
    return render_template('users/users.html', users=users.values())


@bp.route('/new/', methods=['GET', 'POST'])
def new():
    """
    A view to add new user data to de users dict.
    """
    # Instantiate the form
    form = UserCreationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        local_dict = {}
        for field in User.fields:
            local_dict[field] = form[field].data        # Put the data inside the dict
        users.update({form.user_id.data: local_dict})   # Update users dict with the new created local_dict
        flash(message="Success")
        return redirect(url_for('users.new'))
    else:
        return render_template('users/new.html', form=form)
