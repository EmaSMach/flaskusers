# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Address
from .forms import AddressForm

bp = Blueprint('address', __name__, url_prefix='/address')

users = {}

a1 = Address("Address1").to_addresses()
a2 = Address("Address2").to_addresses()


@bp.route('/', methods=['GET', 'POST'])
def address():
    form = AddressForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(message="Success")
            Address.addresses['addresses'].append(form.address.data)
            return redirect(url_for('address.address'))
        else:
            return render_template('address/address.html', form=form)
    elif request.method == 'GET':
        addresses_lists = Address.addresses.values()
        return render_template('address/address.html', addresses_lists=addresses_lists)

