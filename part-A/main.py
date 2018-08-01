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


@app.route('/api/stations', methods=['GET'])
def retrieve_station():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stations;')
    rows = cursor.fetchall()
    db.close()

    rows_as_dict = []
    for row in rows:
        row_as_dict = get_row_as_dict(row)
        rows_as_dict.append(row_as_dict)

    return jsonify(rows_as_dict), 200

@app.route('/api/stations/<int:id>', methods=['GET'])
def retrieve_specific_station(id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stations WHERE id=?', (id,))
    rows = cursor.fetchall()
    db.close()

    rows_as_dict = []
    for row in rows:
        row_as_dict = get_row_as_dict(row)
        rows_as_dict.append(row_as_dict)

    return jsonify(rows_as_dict), 200


@app.route('/api/members/<int:member>', methods=['GET'])
def show(member):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM members WHERE id=?', (str(member),))
    row = cursor.fetchone()
    db.close()

    if row:
        row_as_dict = get_row_as_dict(row)
        return jsonify(row_as_dict), 200
    else:
        return jsonify(None), 200


@app.route('/api/members', methods=['POST'])
def store():
    if not request.json:
        abort(404)

    new_member = (
        request.json['name'],
        request.json['email'],
        request.json['phone'],
        request.json['address'],
        request.json['postcode'],
        request.json['city'],
        request.json['state'],
    )

    db = sqlite3.connect(DB)
    cursor = db.cursor()

    cursor.execute('''
        INSERT INTO members(name,email,phone,address,postcode,city,state)
        VALUES(?,?,?,?,?,?,?)
    ''', new_member)

    member_id = cursor.lastrowid

    db.commit()

    response = {
        'id': member_id,
        'affected': db.total_changes,
    }

    db.close()

    return jsonify(response), 201


@app.route('/api/members/<int:member>', methods=['PUT'])
def update(member):
    if not request.json:
        abort(400)

    if 'id' not in request.json:
        abort(400)

    if int(request.json['id']) != member:
        abort(400)

    update_member = (
        request.json['name'],
        request.json['email'],
        request.json['phone'],
        request.json['address'],
        request.json['postcode'],
        request.json['city'],
        request.json['state'],
        str(member),
    )

    db = sqlite3.connect(DB)
    cursor = db.cursor()

    cursor.execute('''
        UPDATE members SET
            name=?,email=?,phone=?,address=?,postcode=?,city=?,state=?
        WHERE id=?
    ''', update_member)

    db.commit()

    response = {
        'id': member,
        'affected': db.total_changes,
    }

    db.close()

    return jsonify(response), 201


@app.route('/api/members/<int:member>', methods=['DELETE'])
def delete(member):
    if not request.json:
        abort(400)

    if 'id' not in request.json:
        abort(400)

    if int(request.json['id']) != member:
        abort(400)

    db = sqlite3.connect(DB)
    cursor = db.cursor()

    cursor.execute('DELETE FROM members WHERE id=?', (str(member),))

    db.commit()

    response = {
        'id': member,
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
