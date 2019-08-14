#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-19 12:02

import logging.config

from app import app
from config.settings import FLASK_DEBUG

logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.info('Starting server')
    # 指定host，防止docker无法打开
    app.run(host='0.0.0.0', debug=FLASK_DEBUG)