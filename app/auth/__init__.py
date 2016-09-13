#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: __init__.py
#          Desc: auth module
#        Author: Houston Wong
#         Email: gzhuangzicheng@corp.netease.com
#      HomePage: http://www.163.com
#       Version: 0.0.1
#    LastChange: 2016-09-04 17:24:07
#       History:
# =============================================================================
'''

from flask import Blueprint
auth = Blueprint('auth', __name__)
from . import views

