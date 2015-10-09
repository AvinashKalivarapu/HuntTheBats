# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def hunt():
	return dict()

def credits():
	return dict()

def how():
	return dict()

def level1():
	return dict()

def level2():
	return dict()

def scores():
	#db.mytable.truncate()
	#db.mytable.insert(TopScoret="100")	
	if request.vars.score2!=None:
		db.mytable.insert(TopScoret=request.vars.score2)
	myorder = db.mytable.TopScoret.upper()
	row = db(db.mytable.id > 0).select(orderby=myorder)
	a = []
	c = 5
	b = []
	p = 0
	for i in row:
		#print i['TopScoret']
		#print type(i['TopScoret'])
		a.append(i['TopScoret'])
	#print a			
	a.sort()
	#print a
	a.reverse()
	#print a
	while c>0:
	     b.append(a[p])
	     p = p+1
	     c = c-1
	#print b
	#l=len(b)
	#print l		
	return dict(f = b)

def load():
	return dict()

def screenshot():
	return dict()

def story():
	return dict()

def thanku():
	return dict()
def com():
	return dict()
def quit():
	return dict()