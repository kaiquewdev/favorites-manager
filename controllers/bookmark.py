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
		db(db.bookmarks).update(user = auth.user.email, creation = request.now)
		response.flash = T('New bookmark was created !')
	elif form.errors:
		response.flash = T('Oops, look whos wrong !')

	return {'form':form}
	
@auth.requires_login()
def show():
	mymarks = db(db.bookmarks).select()
	return {'marks':mymarks}

@auth.requires_login()
def remove():
	if request.args(0):
		db(db.bookmarks.id == request.args(0)).delete()
		redirect(URL('bookmark','show'));
	else:
		redirect(URL('bookmark','show'))

def edit():
	rec = db.bookmarks(request.args(0)) or redirect(URL('show'))
	form = SQLFORM(db.bookmarks, rec, fields=['name','url'])
	
	if form.accepts(request.vars, session):
		redirect(URL('bookmark','show'))
	elif form.errors:
		response.flash = T('Oops, look whos wrong !')

	return {'form':form}
