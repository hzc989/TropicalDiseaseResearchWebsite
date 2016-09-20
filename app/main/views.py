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
from flask import render_template, session, redirect, url_for, request
from . import main
#from .forms import NameForm
#from .. import db
from ..models import Content

@main.route('/', methods=['GET', 'POST'])
def index():
    newslist = Content.query.filter_by(type="news").order_by(Content.timestamp.desc()).limit(5)
    noticelist = Content.query.filter_by(type="notice").order_by(Content.timestamp.desc()).limit(5)
    return render_template('index.html', newslist=newslist, noticelist=noticelist)

@main.route('/intro/basic', methods=['GET'])
def basic():
    return render_template('intro/basic.html')

@main.route('/content/<type>', methods=['GET'])
def contentList(type):
    page = request.args.get('page', 1, type=int)
    pagination = Content.query.filter_by(type=type).order_by(Content.timestamp.desc()).paginate(
        page, per_page=10, error_out=False)
    contents = pagination.items
    return render_template('main/contentList.html', contents=contents, 
            type=type, pagination=pagination)

@main.route('/content/<type>/<int:id>', methods=['GET'])
def contentDisplay(id,type):
    content = Content.query.get_or_404(id)
    if content.addons_uri:
        addons_uri = eval(content.addons_uri)
        return render_template('main/contentDisplay.html',content=content, addons_uri=addons_uri)
    else:
        return render_template('main/contentDisplay.html',content=content)

