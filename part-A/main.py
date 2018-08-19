"""
The following code is modified from 
https://jamesooi.bitbucket.io/UEEN3123/lectures/UEEN3123-Lecture-04-ii.html
"""

import sqlite3
from flask import Flask, jsonify, request, abort
from argparse import ArgumentParser


DB = 'stationsdb.sqlite'


def get_row_as_dict(row):
    row_dict = {
        'id':   row[0],
        'code': row[1],
        'name': row[2],
        'type': row[3],
    }
    return row_dict


app = Flask(__name__)

# 1. GET /api/stations
@app.route('/api/stations', methods=['GET'])
def retrieve_station():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stations;')
    rows = cursor.fetchall()
    db.close()

    result = [get_row_as_dict(x) for x in rows]

    return jsonify(result), 200

# 2. GET /api/stations/<int:id>
@app.route('/api/stations/<int:id>', methods=['GET'])
def retrieve_specific_station(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stations WHERE id=?', (id,))
    row = cursor.fetchone()
    db.close()
    return jsonify(get_row_as_dict(row) if row else None), 200

# 3. POST /api/stations
@app.route('/api/stations', methods=['POST'])
def create_station():
    if not request.json:
        abort(404)

    new_station = (
        request.json['code'],
        request.json['name'],
        request.json['type']
    )

    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO stations(code,name,type)
        VALUES(?,?,?);
    ''', new_station)

    member_id = cursor.lastrowid
    db.commit()
    response = {
        'id': member_id,
        'affected': db.total_changes,
    }

    db.close()
    return jsonify(response), 201

# 4. PUT /api/stations
@app.route('/api/stations/<string:code>', methods=['PUT'])
def update_station(code):
    if not request.json:
        abort(400)

    if 'code' not in request.json:
        abort(400)

    if request.json['code'] != code:
        abort(400)
    
    db = sqlite3.connect(DB)
    cursor = db.cursor()

    cursor.execute('''
        UPDATE stations SET
            name=coalesce(?,name),
            type=coalesce(?,type)
        WHERE code=?
    ''', (dict.get(request.json, 'name'), dict.get(request.json, 'type'), code))

    db.commit()

    response = {
        'code': code,
        'affected': db.total_changes,
    }

    db.close()

    return jsonify(response), 201

# 5. DELETE /api/stations/<int:id>
@app.route('/api/stations/<int:id>', methods=['DELETE'])
def delete(id):
    if not request.json:
        abort(400)

    if 'id' not in request.json:
        abort(400)

    if int(request.json['id']) != id:
        abort(400)

    db = sqlite3.connect(DB)
    cursor = db.cursor()

    cursor.execute('DELETE FROM stations WHERE id=?', ((id),))

    db.commit()

    response = {
        'id': id,
        'affected': db.total_changes,
    }

    db.close()

    return jsonify(response), 201


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
