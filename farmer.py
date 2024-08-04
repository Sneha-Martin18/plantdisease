from  flask import *
from database import *
import uuid
from newcnn import *
from keras import backend as K

farmer=Blueprint('farmer',__name__)

@farmer.route('/farmhome')
def farmhome():
	return render_template('farmhome.html')


@farmer.route('/Fcomplaint',methods=['get','post'])
def Fcomplaint():
	if 'submit' in request.form:					
		compl=request.form['comp'] 

		s="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['farid'],compl)
		insert(s)
	return render_template('Fcomplaint.html')



@farmer.route('/fertilizer')
def fertilizer():
	data={}
	s="select * from fertilizer"
	data['cview']=select(s)
	print("dddddd",data['cview'])
	return render_template('fertilizer.html',data=data)


@farmer.route('/Fupload',methods=['get','post'])
def Fupload():
	K.clear_session()
	if 'submit' in request.form:
		s=request.files['ufile']
		path="static/images/"+str(uuid.uuid4())+s.filename
		s.save(path)
		out=predictcnn(path)
		val=""
		fertilizer=""
		if out ==0:
			val="Apple___Apple_scab"
			fertilizer="nitrate and ammonium fertilizers and the nitrogen stabilizer"

		elif out==1:
			val="Cherry_(including_sour)___Powdery_mildew"
			fertilizer="Phosphorus-based fertilizers "
		elif out ==2:
			val="Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot"
			fertilizer="Micronutrient fertilizers"
		elif out ==3:
			val="Peach___Bacterial_spot"
			fertilizer="Calcium-based fertilizers"
		elif out ==4:
			val="Potato___Early_blight"
			fertilizer="Nitrogen (N): Ammonium nitrate, urea, ammonium sulfates"
		elif out ==5:
			val="Tomato___Tomato_mosaic_virus"
			fertilizer="Espoma Tomato-tone Organic Fertilizer: A slow-release organic fertilizer"
		ins="insert into images values(null,'%s','%s',curdate(),'%s','%s')"%(session['farid'],path,val,fertilizer)
		insert(ins)
	data={}
	q="select * from images where fid='%s'"%(session['farid'])
	res=select(q)
	data['view']=res
	return render_template('Fupload.html',data=data)

