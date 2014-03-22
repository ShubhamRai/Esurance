# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import datetime
import time
import gluon.contrib.simplejson
import re
import random
def index():
	session.compare=[]
	if auth.user:
		if auth.user.r_type=='customer':
			print 'customer incoming'
			redirect(URL(r=request,f='home'))
		elif auth.user.r_type=='agent':
			print 'agent incoming'
			redirect(URL(r=request,f='agent_home'))
		elif auth.user.r_type=='manager':
			print 'manager incoming'
			redirect(URL(r=request,f='manager_home'))
	else:
		redirect(URL(r=request,f='home'))
    	return dict()

def approve_agent():
	b=db(db.company.mgr_id==auth.user.id).select()[0]
	a=db((db.works_for.company_id==b['id'])).select()
	name=[]
	fin=[]
	for i in range(0,len(a)):
		if a[i]['approve']==0:
			fin.append(a[i])
			c=db(db.auth_user.id==a[i]['user_id']).select()
			name.append(c[0])
	return dict(a=fin,name=name)

def approve_agentconfirm():
	inp=request.args(0)
	db(db.works_for.user_id==inp).update(approve=1)
	session.msg="Agent Confirmation Done!"
	redirect(URL('index'))

#manager_home
def manager_home():
	if session.msg:
		response.flash=session.msg
		session.msg=''
	a=db(db.company.mgr_id==auth.user.id).select()
	if len(a)==0:
		redirect(URL('AddCompany'))
	
	return dict()
def AddCompany():
	response.flash=T("Add Company Details")
	db.company.mgr_id.writable=False
	db.company.mgr_id.readable=False	
	form=SQLFORM.factory(db.company)
	if form.process().accepted:
		a=db.BuyInsurance._filter_fields(form.vars)
		a['mgr_id']=auth.user.id
		db.company.insert(**a)
		redirect(URL('index'))

	return dict(form=form)

def add_new_policy():
	return dict()

def add_pol():
	inp=int(request.args(0))
	db.Insurance.max_cover.requires=IS_INT_IN_RANGE(0,10000000)
	db.Insurance.min_cover.requires=IS_INT_IN_RANGE(0,10000000)
	db.Insurance.type_policy.readable=False
	db.Insurance.type_policy.writable=False
	db.Insurance.company_id.writable=False
	db.Insurance.company_id.readable=False
	db.Insurance.premium.readable=False
	
	db.Insurance.heart.writable=False
	db.Insurance.min_age.writable=False
	db.Insurance.max_age.writable=False
	db.Insurance.target_income.writable=False
	db.Insurance.marital_status.writable=False
	db.Insurance.cancer.writable=False
	db.Insurance.tobbaco.writable=False
	db.Insurance.critical.writable=False
	db.Insurance.min_members.writable=False
	db.Insurance.max_members.writable=False
	db.Insurance.year_build.writable=False
	db.Insurance.no_of_wheels.writable=False
	db.Insurance.min_price.writable=False
	db.Insurance.max_price.writable=False
	db.Insurance.min_year.writable=False
	db.Insurance.travel_type.writable=False
	db.Insurance.premium.writable=False
	db.Insurance.max_limit.writable=False
	
	
	
	db.Insurance.heart.readable=False
	db.Insurance.min_age.readable=False
	db.Insurance.max_age.readable=False
	db.Insurance.min_year.readable=False
	db.Insurance.target_income.readable=False
	db.Insurance.marital_status.readable=False
	db.Insurance.cancer.readable=False
	db.Insurance.tobbaco.readable=False
	db.Insurance.critical.readable=False
	db.Insurance.min_members.readable=False
	db.Insurance.max_members.readable=False
	db.Insurance.year_build.readable=False
	db.Insurance.no_of_wheels.readable=False
	db.Insurance.min_price.readable=False
	db.Insurance.max_price.readable=False
	db.Insurance.travel_type.readable=False
	db.Insurance.max_limit.readable=False
	
	print inp	
	if inp==1:
		#term insurance
		print 'enter'
		db.Insurance.min_age.writable=True
		db.Insurance.max_age.writable=True
		db.Insurance.target_income.writable=True
		db.Insurance.marital_status.writable=True
		db.Insurance.min_age.readable=True
		db.Insurance.max_age.readable=True
		db.Insurance.target_income.readable=True
		db.Insurance.marital_status.readable=True
	elif inp==2:
		#retirement plans
		db.Insurance.min_duration.writable=False
		db.Insurance.max_duration.writable=False
		db.Insurance.min_duration.readable=False
		db.Insurance.max_duration.readable=False
		db.Insurance.min_age.writable=True
		db.Insurance.max_age.writable=True
		db.Insurance.target_income.writable=True
		db.Insurance.marital_status.writable=True
		db.Insurance.min_age.readable=True
		db.Insurance.max_age.readable=True
		db.Insurance.target_income.readable=True
		db.Insurance.marital_status.readable=True
	elif inp==3:
		#child plans
		db.Insurance.target_income.writable=True
		db.Insurance.target_income.readable=True
		db.Insurance.max_age.writable=True
		db.Insurance.max_age.readable=True
	elif inp==4:
		#Health plan
		db.Insurance.heart.writable=True
		db.Insurance.min_age.writable=True
		db.Insurance.max_age.writable=True
		db.Insurance.target_income.writable=True
		db.Insurance.marital_status.writable=True
		db.Insurance.cancer.writable=True
		db.Insurance.tobbaco.writable=True
		db.Insurance.critical.writable=True
		db.Insurance.heart.readable=True
		db.Insurance.min_age.readable=True
		db.Insurance.max_age.readable=True
		db.Insurance.target_income.readable=True
		db.Insurance.marital_status.readable=True
		db.Insurance.cancer.readable=True
		db.Insurance.tobbaco.readable=True
		db.Insurance.critical.readable=True
	elif inp==5:
		#senior
		db.Insurance.heart.writable=True
		db.Insurance.min_age.writable=True
		db.Insurance.max_age.writable=True
		db.Insurance.target_income.writable=True
		db.Insurance.marital_status.writable=True
		db.Insurance.cancer.writable=True
		db.Insurance.tobbaco.writable=True
		db.Insurance.critical.writable=True
		db.Insurance.heart.readable=True
		db.Insurance.min_age.readable=True
		db.Insurance.max_age.readable=True
		db.Insurance.target_income.readable=True
		db.Insurance.marital_status.readable=True
		db.Insurance.cancer.readable=True
		db.Insurance.tobbaco.readable=True
		db.Insurance.critical.readable=True
	elif inp==6:
		#family plans
		db.Insurance.min_members.writable=True
		db.Insurance.max_members.writable=True
		db.Insurance.min_members.readable=True
		db.Insurance.max_members.readable=True
		db.Insurance.target_income.writable=True
		db.Insurance.target_income.readable=True


	elif inp==7:
		#house
		db.Insurance.target_income.writable=True
		db.Insurance.target_income.readable=True
		db.Insurance.year_build.writable=True
		db.Insurance.year_build.readable=True

	elif inp==8:
		#motor insuranace
		db.Insurance.min_duration.writable=False
		db.Insurance.max_duration.writable=False
		db.Insurance.min_duration.readable=False
		db.Insurance.max_duration.readable=False
		db.Insurance.no_of_wheels.writable=True
		db.Insurance.min_price.writable=True
		db.Insurance.max_price.writable=True
		db.Insurance.no_of_wheels.readable=True
		db.Insurance.min_price.readable=True
		db.Insurance.max_price.readable=True
		db.Insurance.target_income.writable=True
		db.Insurance.target_income.readable=True

	elif inp==9:
		#travel plans
		db.Insurance.travel_type.writable=True
		db.Insurance.max_limit.writable=True
		db.Insurance.target_income.writable=True
		db.Insurance.marital_status.writable=True
		db.Insurance.travel_type.readable=True
		db.Insurance.max_limit.readable=True
		db.Insurance.target_income.readable=True
		db.Insurance.marital_status.readable=True
	form=SQLFORM.factory(db.Insurance)
	if form.process().accepted:
		a=db.Insurance._filter_fields(form.vars)
		a['type_policy']=inp
		sel = db(db.company.mgr_id==auth.user.id).select()[0]
		a['company_id']=sel['id']
		db.Insurance.insert(**a)	
		redirect(URL('home'))
	return dict(form=form)

def register_agent():
	inp=request.args(0)
	print inp
	db.works_for.user_id.readable=False
	db.works_for.approve.readable=False
	db.works_for.approve.writable=False
	db.works_for.user_id.writable=False
	form=SQLFORM.factory(db.works_for)
	if form.process().accepted:
		a=db.works_for._filter_fields(form.vars)
		a['user_id']=inp
		a['approve']=0
		db.works_for.insert(**a)	
		redirect(URL('index'))
	return dict(form=form)
#verify the policies
def approve_confirmpolicy():
	inp=request.args(0)
	inp2=request.args(1)
	db(db.BuyInsurance.id==inp).update(approve=True)
	db.handles.insert(agent_id=auth.user.id,user_id=inp2,policy_id=inp)
	session.msg="Policy Confirmation Done!"
	redirect(URL('index'))
def view_pol():
	i=int(request.args(0))
	a=db(db.BuyInsurance.id==i).select()[0]
	return dict(i=a)
def approve_policies():
	a=db(db.BuyInsurance.approve==False).select()
	name=[]
	for i in range(0,len(a)):
		b=db(db.auth_user.id==a[i]['user_id']).select()[0]
		name.append(b)
	print name
	return dict(a=a,name=name)


#agent_home
def agent_home():
	a=db(db.works_for.user_id==auth.user.id).select()
	if len(a)==0:
		redirect(URL(r=request , f='register_agent' , args=auth.user.id))
	if session.msg:
		response.flash=T(session.msg)
		session.msg=''
	b=db(db.handles.agent_id==auth.user.id).select()
	flag=0
	if a[0]['approve']==0:
		flag=0
	else:
		flag=1
	name=[]
	policy=[]
	for j in range(0,len(b)):
		c=db(db.auth_user.id==b[j]['user_id']).select()
		s=db(db.BuyInsurance.id==b[j]['policy_id']).select()
		if(len(c)!=0):
			name.append(c[0])
		if(len(s)!=0):
			policy.append(s[0])
		print 'adslfjk',b[j]['user_id'],b[j]['policy_id']
	return dict(flag=flag,b=b,name=name,policy=policy)
#main_home
def home():
	b=[]
	a=[]
	if session.msg:
		response.flash=session.msg
		session.msg=''	
	if auth.user:
		if auth.user.r_type!='customer':
			redirect(URL('index'))
		else:
			a=db((db.BuyInsurance.user_id==auth.user.id)).select()
	return dict(a=a)

def AddCompare():
	ID=int(request.args(0))
	if len(session.compare)==0 or ID not in session.compare:
		session.compare.append(ID)
	redirect(URL('ViewCompare'))
def clear():
	session.compare=[]
	redirect(URL('ViewCompare'))
def ViewCompare():
	a=[]
	for i in range(len(session.compare)):
		a.append(db(db.Insurance.id==session.compare[i]).select()[0])
		print  "Session Compare",session.compare[i]
	t=[]
	b=list(a)
	print "b= ",b
	a=[]
	for i in range(len(b)):
		a.append([])
	d=['name','policy_description','min_age','max_age','min_cover','max_cover','min_members','max_members','min_duration','max_duration','no_of_wheels','min_price','max_price','travel_type','heart','cancer','critical']
	e=['Name','Description','Minimum Age','Maximum Age','Minimum Cover','Maximum Cover','Minimum Family Size','Maximum Family Size','Minimum Duration','Maximum Duration','Number of Wheels','Minimum Price','Maximum Price','Travel Type','Heart Patients','Cancer Patients','Critical Patients']
	c=[]
	if len(b)!=0:
		for k in range(len(d)):
			j=d[k]
			flag=False
			for i in range(len(b)):
				if b[i][j]=='' or b[i][j]=='None' or b[i][j]=='Not Applicable' or b[i][j]==None:
					flag=flag
				else:
					flag=True
			if flag==True and j!='update_record' and j!='id' and j!= 'company_id' and j!='delete_record' and j!='type_policy':
			 	for i in range(len(b)):
					print b[i][j]
					if b[i][j]=='None' or b[i][j]==None or b[i][j]=='':
						a[i].append('Not Applicable')
					else:
						a[i].append(b[i][j])
				c.append(e[k])
	return dict(b=a,c=c)
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


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

def life_policy_details():
	return dict()

	
def term_policy():

	term_policy=db(db.Insurance.type_policy==1).select()

	return dict(t=term_policy)

def retirement_policy():

	retirement_policy=db(db.Insurance.type_policy==2).select()

	return dict(t=retirement_policy)

def child_policy():

	child_policy=db(db.Insurance.type_policy==3).select()

	return dict(t=child_policy)



def health_policy_details():
	return dict()


def health_policy():

	health_policy=db(db.Insurance.type_policy==4).select()

	return dict(t=health_policy)
	
def seniorhealth_policy():

	seniorhealth_policy=db(db.Insurance.type_policy==5).select()

	return dict(t=seniorhealth_policy)
	
def family_policy():

	family_policy=db(db.Insurance.type_policy==6).select()

	return dict(t=family_policy)
	


def other_policy_details():
	return dict()


def home_policy():

	home_policy=db(db.Insurance.type_policy==7).select()
	
	return dict(t=home_policy)

def motor_policy():

	motor_policy=db(db.Insurance.type_policy==8).select()
	
	return dict(t=motor_policy)

def travel_policy():

	travel_policy=db(db.Insurance.type_policy==9).select()
	
	return dict(t=travel_policy)
@auth.requires_login()
def buy_policy():
	rID=int(request.args(0))
	ID=int(request.args(1))
	sel=db(db.Insurance.id==ID).select()[0]
	ID=rID
	db.BuyInsurance.cover.requires=IS_INT_IN_RANGE(sel['min_cover'],sel['max_cover'])
	db.BuyInsurance.duration.requires=IS_INT_IN_RANGE(sel['min_duration'],sel['max_duration'])
	db.BuyInsurance.age.requires=IS_INT_IN_RANGE(sel['min_age'],sel['max_age'])
	#db.BuyInsurance.premium.requires=IS_INT_IN_RANGE(10,10000)
	db.BuyInsurance.company_id.writable=False
	db.BuyInsurance.user_id.writable=False
	db.BuyInsurance.type_policy.writable=False
	db.BuyInsurance.name.writable=False
	db.BuyInsurance.logo.writable=False
	db.BuyInsurance.policy_description.writable=False
	db.BuyInsurance.extra_benefits.writable=False
	db.BuyInsurance.heart.writable=False
	db.BuyInsurance.cancer.writable=False
	db.BuyInsurance.tobbaco.writable=False
	db.BuyInsurance.critical.writable=False
	db.BuyInsurance.members.writable=False
	db.BuyInsurance.year_build.writable=False
	db.BuyInsurance.no_of_wheels.writable=False
	db.BuyInsurance.approve.writable=False
	db.BuyInsurance.price.writable=False
	db.BuyInsurance.travel_type.writable=False
	
	db.BuyInsurance.premium.readable=False
	db.BuyInsurance.premium.writable=False
	db.BuyInsurance.company_id.readable=False
	db.BuyInsurance.approve.readable=False
	db.BuyInsurance.user_id.readable=False
	db.BuyInsurance.type_policy.readable=False
	db.BuyInsurance.name.readable=False
	db.BuyInsurance.logo.readable=False
	db.BuyInsurance.policy_description.readable=False
	db.BuyInsurance.extra_benefits.readable=False
	db.BuyInsurance.heart.readable=False
	db.BuyInsurance.cancer.readable=False
	db.BuyInsurance.tobbaco.readable=False
	db.BuyInsurance.critical.readable=False
	db.BuyInsurance.members.readable=False
	db.BuyInsurance.year_build.readable=False
	db.BuyInsurance.no_of_wheels.readable=False
	db.BuyInsurance.price.readable=False
	db.BuyInsurance.travel_type.readable=False	
	if ID==1 or ID==2 or ID==3:
		a=1

		
	elif ID==4 or ID==5:
		db.BuyInsurance.heart.readable=True
		db.BuyInsurance.cancer.readable=True
		db.BuyInsurance.tobbaco.readable=True
		db.BuyInsurance.critical.readable=True
		
		db.BuyInsurance.heart.writable=True
		db.BuyInsurance.cancer.writable=True
		db.BuyInsurance.tobbaco.writable=True
		db.BuyInsurance.critical.writable=True
		
	elif ID==6:
		
		db.BuyInsurance.members.readable=True
		db.BuyInsurance.members.writable=True

	elif ID==7:
		
		db.BuyInsurance.year_build.readable=False
		db.BuyInsurance.year_build.writable=False

	elif ID==8:
		
		db.BuyInsurance.no_of_wheels.readable=True
		db.BuyInsurance.price.readable=True
		db.BuyInsurance.no_of_wheels.writable=True
		db.BuyInsurance.price.writable=True

	elif ID==9:
	
		db.BuyInsurance.travel_type.writable=True
		db.BuyInsurance.travel_type.readable=True
		db.BuyInsurance.duration.label='Travel Duration'
	form=SQLFORM.factory(db.BuyInsurance)
	if form.process().accepted:
		a=db.BuyInsurance._filter_fields(form.vars)
		a['user_id']=auth.user.id
		a['type_policy']=sel['type_policy']
		a['company_id']=sel['company_id']
		a['name']=sel['name']
		a['logo']=sel['logo']
		a['premium']=(random.randint(10000,20000)/a['duration'])*a['cover']
		a['policy_description']=sel['policy_description']
		print a
		db.BuyInsurance.insert(**a)	
		session.msg="You have successfully booked the policy"
		#		Inserting For scheduler
		a={}
		a=[auth.user.email,form.vars.name,str(datetime.date.today()+datetime.timedelta(30))]
		db.scheduler_task.insert(
		application_name='Project/appadmin',
		task_name=str(form.vars.id)+'+'+str(auth.user.email),
		group_name='main',
		start_time=request.now+datetime.timedelta(-1),
		stop_time=request.now+datetime.timedelta(1000),
		status='QUEUED',
		repeats=20,
		function_name='f',
		enabled=True,
		period=2592000,
		args=gluon.contrib.simplejson.dumps(a))
		redirect(URL('home'))

	return dict(form=form)
def FilterPolicy():
	a=[]
	p=db(db.company.id>0).select()
	for i in range(len(p)):
		a.append(p[i]['name'])
	a.append('All')
	form=SQLFORM.factory(
			Field('Type',requires=IS_IN_SET(('Term Insurance','Retirement Plan','Child Plan','Health Insurance','Senior Citizen','Family Medicalim Insurance','Home Insurance','Automobile Insurance','Travel Insurance','All')),default='All'),
			Field('Duration','integer'),
			Field('Company','string',requires=IS_IN_SET(a),default='All'),
			Field('Age','integer'),
			Field('Cover','integer'),
			Field('Income','integer',requires=IS_IN_SET(('upto 3 lakhs','3-5 lakhs','5-10 lakhs','10+ lakhs','Any')),default='Any'))
	if form.process().accepted:
		print form.vars
		
		redirect(URL(r=request,f='ViewFilter',args=(form.vars.Type,form.vars.Duration,form.vars.Company,form.vars.Age,form.vars.Cover,form.vars.Income)))
	return dict(form=form)
def ViewFilter():
	a=[]
	a.append(request.args(0))
	a.append(request.args(1))
	a.append(request.args(2))
	a.append(request.args(3))
	a.append(request.args(4))
	a.append(request.args(5))
	TYPE=0
	a[2]=a[2].replace("_"," ")
	if a[0]=='Term_Insurance':
		TYPE=1	
	elif a[0]=='Retirement_Plan':
		TYPE=2
	elif a[0]=='Child_Plan':
		TYPE=3
	elif a[0]=='Health_Insurance':
		TYPE=4
	elif a[0]=='Senior_Citizen':
		TYPE=5
	elif a[0]=='Family_Medicalim_Insurance':
		TYPE=6
	elif a[0]=='Home_Insurance':
		TYPE=7
	elif a[0]=='Automobile_Insurance':
		TYPE=8
	elif a[0]=='Travel_Insurance':
		TYPE=9
	print a ,"Type Of Policy = ", TYPE
	if TYPE!=0:
		sel=db(db.Insurance.type_policy==TYPE).select()
		b=sel
		c=[]
		print sel
	else :
		sel=db(db.Insurance.id>0).select()
		b=sel
		c=[]
		print sel
	if a[1]=='None':
		b=b	
	else:
		sel=db(db.Insurance.min_duration<=int(a[1]) and db.Insurance.max_duration>=int(a[1])).select()
		sel=list(sel)
		for i in sel:
			if( i in b):
				c.append(i)
		b=c
		c=[]
	print b , "A[1]"
	if a[2]=='All':
	   	b=b
	else:
	   	sel=db(db.company.name==a[2]).select()[0]
	   	sel=db(db.Insurance.company_id==int(sel['id'])).select()
		sel=list(sel)
	   	for i in sel:
			if( i in b):
				c.append(i)
		b=c
		c=[]
	print b , "A[2]"
	if a[3]=='None':
	   	b=b
	else:
	   	sel=db(db.Insurance.min_age<=int(a[3]) and db.Insurance.max_age>=int(a[3])).select()
		sel=list(sel)
		for i in sel:
			if( i in b):
				c.append(i)
		b=c
		c=[]
	print b , "A[3]",a[3]
	if a[4]=='None':
	   	b=b
	else:
	   	sel=db(db.Insurance.min_cover<=int(a[4]) and db.Insurance.max_cover>=int(a[4])).select()
		for i in sel:
			if( i in b):
				c.append(i)
		b=c
		c=[]
	if a[5]=='Any':
	   	b=b
	else:
	   	a[5].replace("_"," ")
	   	sel=db(db.Insurance.target_income==a[5]).select()
		for i in sel:
			if( i in b):
				c.append(i)
		b=c
		c=[]
	a=[]
	c=[]
	b=list(b)
	return dict(b=b)
