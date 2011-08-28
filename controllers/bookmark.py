# -*- coding:utf-8 -*-
'''
Controller para bookmarks onde terao todas as funcoes para trabalhar
com os marcadores
'''
def index():
	redirect(URL('new'))

@auth.requires_login()	
def new():
	return {}
	
@auth.requires_login()
def show():
	return {}
