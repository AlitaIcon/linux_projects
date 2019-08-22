#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:muji
# datetime:2019/8/1 12:01
import os

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
case_log_path = os.path.join(root_path, 'case_log')
if not os.path.exists(case_log_path):
    os.mkdir(case_log_path)


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:@localhost:3306/dev01_git'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'SFOWS.FSSPWLSD'
    PER_PAGE = 10
    CASE_LOG_PATH = case_log_path


class TestConfig(Config):
    pass


class ProdConfig(Config):
    DEBUG = False


config = ProdConfig
