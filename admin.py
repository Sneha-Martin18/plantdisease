from  flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')


@admin.route('/farmer')
def farmer():
	data={}
	s="select * from farmer"
	data['cview']=select(s)
	print("dddddd",data['cview'])
	return render_template('farmer.html',data=data)


@admin.route('/fertilizerin',methods=['get','post'])
def fertilizerin():
	data={}
	s="select * from fertilizer"
	res=select(s)
	data['cview']=res
	print("dddddd",data['cview'])

	if 'submit' in request.form:					
		disease=request.form['dis']  
		fertilizer=request.form['ferti']
		description=request.form['des']
		q="insert into fertilizer values(null,'%s','%s','%s')"%(disease,fertilizer,description)	
		insert(q)
		
	if 'action' in request.args:
		action=request.args['action']
		fertid=request.args['fertid']
	else:
		action=None

	if action=='update':
		q="select * from fertilizer where ferid='%s'"%(fertid)
		data['up']=select(q)

	if 'update' in request.form:
		disease=request.form['dis']
		fertilizers=request.form['ferti']
		description=request.form['des']
		q="update fertilizer set  disease= '%s',fertilizers='%s',description='%s'where ferid='%s'"%(disease,fertilizers,description,fertid)
		update(q)
		return redirect(url_for('admin.fertilizerin'))

	if action=='delete':
		q="delete from fertilizer where ferid='%s'"%(fertid)
		delete(q)
		return redirect(url_for('admin.fertilizerin'))

	return render_template('fertilizerin.html',data=data)


@admin.route('/Vcomplaint')
def Vcomplaint():
	data={}
	s="select * from complaint"
	data['cview']=select(s)
	print("dddddd",data['cview'])
	return render_template('Vcomplaint.html',data=data)

@admin.route('/reply', methods=['get','post'])
def reply():
	if 'submit' in request.form:
		replyy=request.form['rep']
		cmid=request.args['cmid']
		i="update complaint set reply='%s' where cmpid='%s'"%(replyy,cmid)
		update(i)
		return redirect(url_for('admin.adminhome'))
	return render_template('reply.html')

@admin.route('/notif', methods=['get','post'])
def notif():
	if 'submit' in request.form:
		notif=request.form['noti']
		nid=request.args['notid']
		k= "insert into notification values(null,'%s',curdate())"%(nid,notif)
		insert(k)
	return render_template('notif.html')






