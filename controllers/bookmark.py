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
		form = SQLFORM(Bookmarks, fields=['name','url','note','keywords'])
	    
		if form.accepts(request.vars, session, dbio = False):
			Bookmarks.insert(
								user = auth.user.email,
								author = auth.user.username,
								name = form.vars.name,
								url = form.vars.url,
								note = form.vars.note,
								keywords = form.vars.keywords,
								status = 'public',
								creation = request.now)
			response.flash = T('{0} was created !').format(form.vars.name)
		elif form.errors:
			response.flash = T('Oops, look who\'s wrong !')
	
		return {'form':form}
	
@auth.requires_login()
def show():
		'''
		Mostra os bookmarks
		'''
		mymarks = db().select(Bookmarks.ALL, orderby=Bookmarks.creation)
		return {'marks':mymarks}

@auth.requires_login()
def remove():
		'''
		Remove um bookmark
		'''
		if request.args(0):
			db(Bookmarks.id == request.args(0)).delete()
			redirect(URL('bookmark','show'));
		else:
			redirect(URL('bookmark','show'))
		
@auth.requires_login()
def edit():
		'''
		Edita um bookmark existente
		'''
		rec = Bookmarks(request.args(0)) or redirect(URL('show'))
		form = SQLFORM(Bookmarks, rec, fields=['name','url', 'note'])
		
		if form.accepts(request.vars, session):
			redirect(URL('bookmark','show'))
		elif form.errors:
			response.flash = T('Oops, look whos wrong !')
	
		return {'form':form}

def search():
		'''
		Faz a procura por bookmarks
		'''
		if request.vars.search == '' or request.vars.search == None:
			redirect(URL('default','index'))
		else:
			f = db(Bookmarks.id>0).select()
			#faz a busca da palavra no banco e seleciona tudo o que foi selecionado caso contrario ele retorna None
			f = f.find(lambda s:request.vars.search in s.name.lower() or request.vars.search in s.name and s.status == 'public').sort(lambda s:s.name) or None
			
			if f == None:
				response.flash = T('Try again !')
			
		
		return {'search':f}

