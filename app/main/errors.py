#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: error.py
#          Desc: errors handler
#        Author: Houston Wong
#         Email: gzhuangzicheng@corp.netease.com
#      HomePage: http://www.163.com
#       Version: 0.0.1
#    LastChange: 2016-09-04 00:53:59
#       History:
# =============================================================================
'''

from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
