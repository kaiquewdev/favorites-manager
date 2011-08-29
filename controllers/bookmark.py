# -*- coding:utf-8 -*-
'''
Controller para bookmarks onde terao todas as funcoes para trabalhar
com os marcadores
'''
def index():
	redirect(URL('new'))

@auth.requires_login()	
def new():
	form = SQLFORM(db.bookmarks, fields=['name','url'])

	if form.accepts(request.vars, session):
		response.flash = T('The new bookmark was created!')
	elif form.errors:
		redirect(URL('new'))

	return {'form':form}
	
@auth.requires_login()
def show():
	mymarks = db(db.bookmarks).select()
	return {'marks':mymarks}

def edit():
	return {}
