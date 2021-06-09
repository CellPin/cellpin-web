from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
from CPE_classifier import model_build, prediction_base
from TCID50_calculator import TCID50_Calculator

import tensorflow as tf
import os

model = model_build()
app = Flask(__name__, template_folder="./templates/", static_url_path="/images", static_folder="images")

'''
File upload
'''
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/TCID50', methods=['GET', 'POST']) 
def TCID50(): 
    return render_template('TCID50.html')

# @app.route("/select_box", methods = ['POST'])
# def select_box():
#     selectVirusCell = request.form.get('virus_cell') 
#     if selectVirusCell == 'PRRSV_MARC':
#         model = model_build()


@app.route("/image", methods = ['POST'])
def get_result():   
    if request.method == "POST":
        selectVirusCell = request.form.get('virus_cell')
        if selectVirusCell == 'PRRSV_MARC':      
            try:
                file = request.files['source']
                filename = secure_filename(file.filename)
                os.makedirs("../images/", exist_ok=True)
                file.save(os.path.join("../images/", filename))
                result = prediction_base(model, os.path.join("../images/", filename))
            except Exception as e:
                # print("error : %s" % e)
                return Response("fail", status=400)
            return str(f'{filename}은 {result}')
        else: 
            return str('옵션을 선택해주세요.')
    # return str(f'{filename}은 {result}')



@app.route("/TCID50_calculator", methods=['POST'])
def TCID50_calculator():
    if request.method == "POST":
       try:
            w = request.form.get('well')
            t1 = request.form.get('dilution_1')
            t2 = request.form.get('dilution_2')
            t3 = request.form.get('dilution_3')
            t4 = request.form.get('dilution_4')
            t5 = request.form.get('dilution_5')
            t6 = request.form.get('dilution_6')
            t7 = request.form.get('dilution_7')
            t8 = request.form.get('dilution_8')
            result = TCID50_Calculator(w, t1, t2, t3, t4, t5, t6, t7, t8)
       except Exception as e:
           print("error : %s" % e)
           return Response("fail", status=400)    
    return str(f'TCID50의 값은 10^{result}입니다.')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 80))