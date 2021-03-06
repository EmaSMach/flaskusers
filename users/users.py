# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from .forms import UserCreationForm


bp = Blueprint('users', __name__, url_prefix='/users')

users = {}


@bp.route('/', methods=['GET', 'POST'])
def show_users():
    """
    A view function to show and add users.
    """
    if request.method == 'POST':
        # If 'post', instantiate the form
        form = UserCreationForm(request.form)
        if form.validate_on_submit():
            local_dict = {}
            for field in User.fields:
                local_dict[field] = form[field].data       # Put the data inside the dict
            users.update({form.user_id.data: local_dict})  # Update users dict with the new created local_dict
            flash(message="Success")
            # Redirect to the list of users
            return redirect(url_for('users.show_users'))
        else:
            # If the data in the form is not valid, show the form again.
            return render_template('users/users.html', form=form)
    # If 'GET', show the list of users
    return render_template('users/users.html', users=users.values())

