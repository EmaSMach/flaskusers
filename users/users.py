# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from flask import Blueprint, render_template, request, flash, redirect
from .models import User
from .forms import UserCreationForm


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['GET', 'POST'])
def show_users():
    users = {
        1: User(1, 'emanuel', 'sandoval',   'emanuel@gmail.com',  True, 'emanuel', 25).to_dict(),
        2: User(2, 'clarisa', 'sandoval',   'clarisa@gmail.com',  True, 'clarisa').to_dict(),
        3: User(3, 'juan',    'aquino',     'juan@gmail.com',     True, 'juanaquino').to_dict(),
        4: User(4, 'gabriel', 'cánepa',     'gabinepa@gmail.com', True, 'gabinepa').to_dict(),
        5: User(5, 'rosario', 'tijeras',    'rtijeras@gmail.com', True, 'rtijeras').to_dict(),
        6: User(6, 'lauraro', 'martínez',   'lauta@gmail.com',    True, 'lautaro').to_dict(),
        7: User(7, 'pedro',   'monetengro', 'pedrom@gmail.com',   True, 'pedro').to_dict(),
    }
    return render_template('users/users.html', users=users.values())


@bp.route('/new/', methods=['GET', 'POST'])
def new():
    users = {
        # 1: User(1, 'emanuel', 'sandoval', 'emanuel@gmail.com', True, 'emanuel', 25).to_dict(),
        # 2: User(2, 'clarisa', 'sandoval', 'clarisa@gmail.com', True, 'clarisa').to_dict(),
        # 3: User(3, 'juan', 'aquino', 'juan@gmail.com', True, 'juanaquino').to_dict(),
        # 4: User(4, 'gabriel', 'cánepa', 'gabinepa@gmail.com', True, 'gabinepa').to_dict(),
        # 5: User(5, 'rosario', 'tijeras', 'rtijeras@gmail.com', True, 'rtijeras').to_dict(),
        # 6: User(6, 'lauraro', 'martínez', 'lauta@gmail.com', True, 'lautaro').to_dict(),
        # 7: User(7, 'pedro', 'monetengro', 'pedrom@gmail.com', True, 'pedro').to_dict(),
    }
    form = UserCreationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.user_id.data)
            print(form.first_name.data)
            print(form.last_name.data)
            print(form.email.data)
            print(form.username.data)
            print(form.active.data)
            form = UserCreationForm()
            return render_template('users/new.html', form=form)
        return render_template('users/new.html', form=form)
    else:
        print("GETTTT")
        return render_template('users/new.html', form=form)

