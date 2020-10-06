from flask import Flask, json, request, Response
import pandas as pd
from resources.db_ops import drop_tb, insert_records, read_data_records, create_tb

app = Flask(__name__)
app.config["DEBUG"] = True

# allow to directly create and fill a table from scratch based on csv file
@app.route('/training-db/init/<table_name>', methods=['POST'])
def create_table_init(table_name):
    '''Takes json file where the first key is column names and 
    the rest are the data that are to be inserted'''
    req_data = request.get_json()
    create_tb(table_name, req_data['columns'])
    insert_records(table_name, req_data['data'])
    return json.dumps({'message':'The table {tname} was created'.format(tname=table_name)},
    sort_keys=False, indent=4), 200

# allow to set up table like sql - first create table schema
@app.route('/training-db/<table_name>', methods=['POST'])
def create_table_schema(table_name):
    req_data = request.get_json()
    columns = req_data['columns']
    create_tb(table_name, columns)
    return json.dumps({'message': 'The table {tname} was created'.format(tname=table_name)}, 
    sort_keys=False, indent=4), 200

# add data into existing table
@app.route('/training-db/<table_name>', methods=['PUT'])
def add_data(table_name):
    content = request.get_json()
    insert_records(table_name, content)
    return json.dumps({'message': 'training data were updated'}, sort_keys=False, indent=4), 200

# drop an existing table
@app.route('/training-db/<table_name>', methods=['DELETE'])
def drop_table(table_name):
    drop_tb(table_name)
    return json.dumps({'message': 'The table {tname} was dropped'.format(tname=table_name)},
    sort_keys=False, indent=4), 200


# get table
@app.route('/training-db/<table_name>', methods=['GET'])
def read_data(table_name):
    df = read_data_records(table_name)
    df = df.drop(columns=['id'])
    resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST'
    resp.headers['Access-Control-Max-Age'] = '1000'
    return resp


app.run(host='0.0.0.0', port=5000)
