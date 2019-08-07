#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-08-02 14:04

# 设置返回参数
class Ret:
    SUCCESS = "0"
    FAILURE = "4001"
    DBERR = "4101"
    TOKENERR = "4201"

ERROR_MAP = {
    Ret.SUCCESS: "成功",
    Ret.FAILURE: "失败",
    Ret.DBERR: "数据库错误",
    Ret.TOKENERR: "TOKEN失效"
}