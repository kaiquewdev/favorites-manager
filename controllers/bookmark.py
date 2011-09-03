# -*- coding:utf-8 -*-
'''
Controller para bookmarks onde terao todas as funcoes para trabalhar
com os marcadores
'''
def index():
	'''
	Inicio dos bookmarks
	'''
	redirect(URL('new'))

@auth.requires_login()	
def new():
	'''
	Cria um novo bookmark
	'''
	form = SQLFORM(db.bookmarks, fields=['name','url','note','keywords'])
    
	if form.accepts(request.vars, session, dbio=False):
		db(db.bookmarks).update(user = auth.user.email, creation = request.now)
		response.flash = T('New bookmark was created !')
	elif form.errors:
		response.flash = T('Oops, look who\'s wrong !')

	return {'form':form}
	
@auth.requires_login()
def show():
	'''
	Mostra os bookmarks
	'''
	mymarks = db().select(db.bookmarks.ALL, orderby=db.bookmarks.creation)
	return {'marks':mymarks}

@auth.requires_login()
def remove():
	'''
	Remove um bookmark
	'''
	if request.args(0):
		db(db.bookmarks.id == request.args(0)).delete()
		redirect(URL('bookmark','show'));
	else:
		redirect(URL('bookmark','show'))
		
@auth.requires_login()
def edit():
	'''
	Edita um bookmark existente
	'''
	rec = db.bookmarks(request.args(0)) or redirect(URL('show'))
	form = SQLFORM(db.bookmarks, rec, fields=['name','url'])
	
	if form.accepts(request.vars, session):
		redirect(URL('bookmark','show'))
	elif form.errors:
		response.flash = T('Oops, look whos wrong !')

	return {'form':form}

def search():
	'''
	Faz a procura por bookmarks
	'''

