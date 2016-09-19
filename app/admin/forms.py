#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: forms.py
#          Desc: form used for admin
#        Author: Houston Wong
#         Email: gzhuangzicheng@corp.netease.com
#      HomePage: http://www.163.com
#       Version: 0.0.1
#    LastChange: 2016-09-15 06:07:03
#       History:
# =============================================================================
'''
from flask import current_app
from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired
from .fields import TagField
from wtforms.validators import Required

class ContentForm(Form):
    type = SelectField(u'栏目',choices=[ ('news',u'新闻动态'), 
                                        ('notice',u'通知公告'),
                                        ('datatools',u'数据工具')])
    title = StringField(u'标题', validators=[Required()])
    body = TextAreaField(u'正文', validators=[Required()])
    addons = FileField(u'附件', validators=[FileRequired()],
                                render_kw={'multiple':True},)
    submit = SubmitField('Submit')

