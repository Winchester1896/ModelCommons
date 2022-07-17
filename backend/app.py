from re import L
from flask import Flask, jsonify, request,Response
from flask_cors import CORS
import helper
import pandas as pd
from datetime import date
import ruamel.yaml as yaml


# configuration
DEBUG = True
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/runModel', methods=['POST'])
def runModel():
    print('dddd')
    command = request.get_json()['command']
    data = request.get_json()['data']
    if command == 'defonet' and data == "leafdefo":
        helper.run_docker_image()
        msg = "running"
        code = 200
    else:
        msg = "error: no matching"
        code = 404
    return jsonify({"msg": msg, "status": code})

@app.route('/addNewModel', methods=['POST'])
def addNewModel():
    name = request.get_json()['name']
    command = request.get_json()['command']

    temp_df = pd.DataFrame({
        'name': [name],
        'command':[command]
    })

    old_df = helper.readCSV('data/model.csv')
    new_df = helper.appendToDF(old_df, temp_df)
    helper.saveDfToFile(new_df, 'data/model.csv')
    return jsonify({'status': 200, 'msg': 'yes'})

@app.route('/getModel', methods=['GET'])
def getModel():
    df = helper.readCSV('data/model.csv')

    df_json = df.to_dict(orient="records")

    output = {}
    for ele in df_json:
        output[ele['name']] = ele['command']
    return jsonify(output)

# add new dataset ---------------------------------------------------------------------------------------------
@app.route('/addNewDataset', methods=['POST'])
def addNewDataset():
    name = request.get_json()['name'] 
    # we name the yaml file, not using the original file name. Given a dataset, text: 'Soybean leaf disease', value: 'soybeanleafdisease'
    # then the yaml file name will be 'data/soybeanleafdisease-20220708-v0.yml'
    # read the yaml file, save the name ('data/soybeandefo.20220708.v0.yml') to csv file, save the yaml file to a folder ('data/')
    yamlfile = request.get_json()['input'] # from uploading a yaml file 

    temp_df = pd.DataFrame({
        'name': [name],
        'yaml':[yamlfile]
    })

    old_df = helper.readCSV('data/dataset.csv')
    new_df = helper.appendToDF(old_df, temp_df)
    helper.saveDfToFile(new_df, 'data/dataset.csv')
    return jsonify({'status': 200, 'msg': 'yes'})

# get dataset --------------------------------------------------------------------------------------------------
@app.route('/getDataset', methods=['GET'])
def getDataset():
    df = helper.readCSV('data/dataset.csv')
    df_json = df.to_dict(orient="records")

    output = {}
    for ele in df_json:
        output[ele['name']] = ele['yaml']
    return jsonify(output)

# The whole process about data set. 1) add new: read yaml file as input
# 2) update yaml file, owner level: to entire file, user level: to partial 

@app.route('/showInfo', methods=['POST'])
# when choosing a data set, display the necessary info needed to use it 
def showDatasetKeyInfo():
    selected_dataset = 'file.yml'
    yf = helper.readYAML(selected_dataset)
    selected_part = yf['physical properties']
    return selected_part

# add new contents to yaml file -> create new yaml file. 
# need to update 'dataset.csv'
@app.route('/updateYAML', methods=['GET'])
def updateYAML():
    # create new yaml filename and update 'data/dataset.csv'
    name = request.get_json()['name'] # dataset name
    model_name = request.get_json()['modelname'] # new model name
    model_value = request.get_json()['modelvalue']
    df = helper.readCSV('data/dataset.csv')
    df_json = df.to_dict(orient="records")
    for ele in df_json:
        if ele['name'] == name:
            oldyaml = ele['yaml']
            temp = oldyaml.split('.')
            ver_no = temp[-2][1:]
            ver_no = 'v' + str(int(ver_no) + 1)
            temp_date = date.today()
            temp_date0 = temp_date.strftime("%Y%m%d")
            newyaml = temp[0] + temp_date0 + ver_no + '.yml'
            ele['yaml'] = newyaml
    new_df = pd.DataFrame.from_dict(df_json)
    helper.saveDfToFile(new_df, 'data/dataset.csv')
    # then create new yaml file
    yaml_file = helper.readYAML(oldyaml)
    yaml_file['model properties'][model_name] = model_value

'''
1. build user login system, user database
2. standardize dataset yaml file content 
3. add backend support for add new dataset
4. add table for 'add new model'
5.  
'''    

if __name__ == '__main__':
    app.run(host='0.0.0.0')