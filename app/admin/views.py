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

import os
from datetime import datetime
from flask import request, current_app, render_template, session, redirect, \
         url_for, flash
from flask_login import login_required, current_user
from werkzeug import secure_filename
from . import admin
from .. import addons, db
from ..models import Content
from .forms import ContentForm

@admin.route('/index', methods=['GET'])
@login_required
def index():
    if current_user.role == "user":
        flash("you're not allowed to the admin pages.")
        return render_template('index.html')
    else:
        flash("welcome back! %s" %current_user.truename)
        return redirect(url_for('admin.content_edit'))

@admin.route('/content_edit', methods=['GET', 'POST'])
@login_required
def content_edit():
    form = ContentForm()
    if form.validate_on_submit():
        addons_uri_dict = {}
        if request.method == 'POST' and 'addons' in request.files:
            Files = request.files.get('addons')
            if Files:
                for addon in request.files.getlist('addons'):
                    addons.save(addon)
                    addons_uri_dict[addon.filename] = addons.url(addon.filename)
                content = Content(  title=form.title.data,
                            addons_uri = str(addons_uri_dict),
                            content=form.body.data,
                            type=form.type.data,
                            poster_uid=current_user.id,
                        )
                flashmsg = "content and addons saved."
            else:
                content = Content(  title=form.title.data,
                            content=form.body.data,
                            type=form.type.data,
                            poster_uid=current_user.id,
                        )
                flashmsg = "content saved."
        db.session.add(content)
        db.session.commit()
        flash(flashmsg)
    return render_template('admin/content_editor.html',
                            form=form, 
                            current_time=datetime.utcnow())
