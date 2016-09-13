#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: views.py
#          Desc: 
#        Author: Houston Wong
#         Email: gzhuangzicheng@corp.netease.com
#      HomePage: http://www.163.com
#       Version: 0.0.1
#    LastChange: 2016-09-04 00:56:30
#       History:
# =============================================================================
'''

from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
#from .forms import NameForm
#from .. import db
#from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    #form = NameForm()
    #if form.validate_on_submit():
    #    # ...
    #    return redirect(url_for('.index'))
    #return render_template('index.html',
    #                        form=form, name=session.get('name'),
    #                        known=session.get('known', False),
    #                        current_time=datetime.utcnow())
    return render_template('index.html')
