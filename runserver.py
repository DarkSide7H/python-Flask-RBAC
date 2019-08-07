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
    app.run(debug=FLASK_DEBUG)