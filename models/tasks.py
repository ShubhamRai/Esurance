def ma(*a):
	import datetime
	mail.send(a[0],subject='Your Payment for policy '+a[1]+' is pending!!',message='You Have your payment for '+a[1]+' due on '+a[2]+'.Please pay before due date to avoid penalty.\nYours Sincerely\nPolicy Bazar')
	return
from gluon.scheduler import Scheduler
scheduler=Scheduler(db,dict(f=ma))
