# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call():
    session.forget()
    return service()
### end requires

def index():
	bookmarks = db(db.bookmarks.status == 'public').select()
	search = FORM(T('Search:'), INPUT(_name='search',_type='text'), INPUT(_value='Find', _type='submit'))
	
	return {'marks':bookmarks, 'search':search}

def about():return {}
def error():return {}

