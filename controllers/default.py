# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request, db)
def call():
        session.forget()
        return service()
### end requires

def index():
    	bookmarks = db(db.bookmarks.status == 'public').select()
    	search = FORM(T('Search:'), INPUT(_name='search', _type='text', requires=IS_NOT_EMPTY()), INPUT(_value=T('Go'), _type='submit'), _action=URL('bookmark', 'search'), _method='post')
        session.search = search         
    	return {'marks':bookmarks, 'search':search}

def about():return {}
def error():return {}

