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
	return {'marks':bookmarks}

def about():return {}
def error():return {}

