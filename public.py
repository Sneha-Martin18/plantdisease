from flask import *
from database import *
public=Blueprint('public',__name__)


@public.route('/')
def home():
	return render_template('home.html')



@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:	
		usname=request.form['uname']
		passwd=request.form['pwd']
		s="select * from login where username='%s' and password='%s'"%(usname,passwd)
		res=select(s)
		session['loginid']=res[0]['logid']		
		if res:													
			if res[0]['usertype']=='farmer':
				s="select * from farmer where logid='%s'"%(session['loginid'])
				res=select(s)
				if res:
					session['farid']=res[0]['fid']
					return redirect(url_for('farmer.farmhome'))

			elif res[0]['usertype']=='admin':
				return redirect(url_for('admin.adminhome'))
	return render_template('login.html')


@public.route('/register',methods=['get','post'])
def register():
	if 'submit' in request.form:					
		ftname=request.form['fname']  
		ltname=request.form['lname']
		plce=request.form['place']
		ph=request.form['phno']
		emailid=request.form['email']
		usname=request.form['uname']
		passwd=request.form['pwd']

		q="insert into login values(null,'%s','%s','farmer')"%(usname,passwd)	
		res=insert(q)
		s="insert into farmer values(null,'%s','%s','%s','%s','%s','%s')"%(res,ftname,ltname,plce,ph,emailid)
		insert(s)
		return redirect(url_for('public.login'))
	return render_template('register.html')


