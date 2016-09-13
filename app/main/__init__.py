#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: __init__.py
#          Desc: 
#        Author: Houston Wong
#         Email: gzhuangzicheng@corp.netease.com
#      HomePage: http://www.163.com
#       Version: 0.0.1
#    LastChange: 2016-09-04 00:47:53
#       History:
# =============================================================================
'''

from flask import Blueprint

main = Blueprint('main',__name__)
from . import views,errors
