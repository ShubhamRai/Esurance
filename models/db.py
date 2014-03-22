# -*- coding: utf-8 -*-
import os
#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
auth.settings.extra_fields['auth_user'] = [Field('r_type',writable=True,requires=IS_IN_SET(['customer','agent','manager','admin']),default="customer")]
crud, service, plugins = Crud(db), Service(), PluginManager()

auth.enable_record_versioning(db)
## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
from gluon.tools import Mail
mail=Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'samfisher2394@gmail.com'
mail.settings.login = 'samfisher2394:ani231994'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
#

db.define_table('company',
	Field('name','string'), 
	Field('logo','upload',uploadfolder=os.path.join(request.folder,'uploads')),
	Field('mgr_id','integer'))               



db.define_table('works_for',
	Field('company_id','integer'), 
	Field('user_id','integer'),
	Field('approve','integer'))               

db.define_table('handles',
	Field('agent_id','integer'), 
	Field('policy_id','integer'),             
	Field('user_id','integer'))               

db.define_table('Insurance',
	Field('type_policy','integer'),
	Field('company_id','integer'), 
	Field('name','string'),            
	Field('logo','upload',uploadfolder=os.path.join(request.folder,'uploads')),
	Field('policy_description','text'),	
	Field('min_cover','integer'),
	Field('max_cover','integer'),
	Field('min_duration','integer'),
	Field('premium','integer'),
	Field('max_duration','integer'),
	Field('min_age','integer'),
	Field('max_age','integer'),		
	Field('target_income',requires=IS_IN_SET(['upto 3 lakhs','3-5 lakhs','5-10 lakhs','10+ lakhs','Not Applicable']),default='Not Applicable'),
	Field('marital_status',requires=IS_IN_SET(('Single','Divorced','Married','Widowed','Not Applicable')),default='Not Applicable'),
	Field('extra_benefits','text'),
	Field('heart',requires=IS_IN_SET(['Yes','No','Not Applicable']),default='Not Applicable'),
	Field('cancer',requires=IS_IN_SET(['Yes','No','Not Applicable']),default='Not Applicable'),
	Field('tobbaco',requires=IS_IN_SET(['Yes','No','Not Applicable']),default='Not Applicable'),
	Field('critical',requires=IS_IN_SET(['Yes','No','Not Applicable']),default='Not Applicable'),		
	Field('min_members','integer'),
	Field('max_members','integer'),
	Field('year_build','integer'),
	Field('no_of_wheels','integer'),
	Field('min_price','integer'),
	Field('max_price','integer'),
	Field('min_year','integer'),
	Field('travel_type',requires=IS_IN_SET(['Abroad','Domestic','Not Applicable']),default='Not Applicable'),
	Field('max_limit','integer'))


db.define_table('BuyInsurance',
	Field('approve','boolean',default=False),
	Field('company_id','integer'), 
	Field('user_id','integer'),
	Field('type_policy','integer'),
	Field('name','string'),            
	Field('logo','upload',uploadfolder=os.path.join(request.folder,'uploads')),
	Field('policy_description','text'),	
	Field('cover','integer',requires=IS_NOT_EMPTY()),
	Field('duration','integer',requires=IS_NOT_EMPTY()),
	Field('age','integer',requires=IS_NOT_EMPTY()),
	Field('premium','integer',readable=False,requires=IS_NOT_EMPTY()),
	Field('target_income',requires=IS_IN_SET(('upto 3 lakhs','3-5 lakhs','5-10 lakhs','10+ lakhs','Not Applicable')),default='Not Applicable'),
	Field('marital_status',requires=IS_IN_SET(('Single','Divorced','Married','Widowed','Not Applicable')),default='Not Applicable'),
	Field('extra_benefits','text'),
	Field('heart',requires=IS_IN_SET(['Yes','No','Not Applicable']),default='Not Applicable'),
	Field('cancer',requires=IS_IN_SET(['Yes','No','Not Applicable']),default='Not Applicable'),
	Field('tobbaco',requires=IS_IN_SET(['Yes','No','Not Applicable']),default='Not Applicable'),
	Field('critical',requires=IS_IN_SET(['Yes','No','Not Applicable']),default='Not Applicable'),		
	Field('members','integer'),
	Field('year_build','integer'),
	Field('no_of_wheels','integer'),
	Field('price','integer'),
	Field('travel_type',requires=IS_IN_SET(['Abroad','Domestic','Not Applicable']),default='Not Applicable'))

db.BuyInsurance.company_id.requires=IS_IN_DB(db,'company.id','company.name')
db.Insurance.company_id.requires=IS_IN_DB(db,'company.id','company.name')
db.works_for.company_id.requires=IS_IN_DB(db,'company.id','company.name')
