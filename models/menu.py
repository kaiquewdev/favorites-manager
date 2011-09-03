T.force('pt-br')
response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%s <%s>' % (settings.author, settings.author_email)
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
					(T('Home'), False, URL('default','index'))
				]

if not auth.user:
	response.menu += [(T('Bookmarks'), False, URL('bookmark','index'))]

elif auth.user:
	response.menu += [
						(T('My Bookmarks'), False, URL('bookmark','show')),
						(T('Create a new'), False, URL('bookmark','new'))
					 ]

response.menu += [
					(T('About'), False, URL('default','about'))
				 ]