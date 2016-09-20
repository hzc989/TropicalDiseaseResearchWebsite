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
from ..models import Content

@main.route('/', methods=['GET', 'POST'])
def index():
    newslist = Content.query.filter_by(type="news").order_by(Content.timestamp.desc()).limit(5)
    noticelist = Content.query.filter_by(type="notice").order_by(Content.timestamp.desc()).limit(5)
    return render_template('index.html', newslist=newslist, noticelist=noticelist)

@main.route('/intro/basic', methods=['GET'])
def basic():
    return render_template('intro/basic.html')

@main.route('/content/news/<int:id>', methods=['GET'])
def newsDisplay(id):
    content = Content.query.get_or_404(id)
    return render_template('main/newsContent.html',content=content)
