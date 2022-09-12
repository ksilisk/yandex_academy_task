from flask import Flask, jsonify, request
import helpers.validate as validate
import helpers.errors as e
import helpers.helper as helper
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)
app = Flask('MyService')
logging.info('App created!')


# обработчик post запроса /imports
@app.route('/imports', methods=['POST'])
def import_elems():
    logging.info('/import handled!')
    data = request.get_json()
    logging.info('Data: %s' % data)
    if validate.valid_data(data):
        helper.import_help(data)
        return '', 200
    return jsonify(e.err400), 400


# обработчик delete запроса /delete
# request params: date; elem_id - id файла/папки
@app.route('/delete/<string:elem_id>', methods=['DELETE'])
def delete_elem(elem_id):
    logging.info('/delete handled')
    date = request.args.get('date')
    logging.info('ID: %s, DATE: %s' % (elem_id, date))
    if validate.valid_date(date):
        if validate.valid_id(elem_id):
            helper.delete_help(elem_id, date)
            return '', 200
        return jsonify(e.err404), 404
    return jsonify(e.err400), 400


# обработчик get запроса /nodes/id
# elem_id - id файла/папки
@app.route('/nodes/<string:elem_id>', methods=['GET'])
def nodes(elem_id):
    logging.info('/nodes handled')
    if validate.valid_id(elem_id):
        return jsonify(helper.nodes_help(elem_id)), 200
    return jsonify(e.err404), 404


# обработчик get запроса /updates
# request params: date
@app.route('/updates', methods=['GET'])
def updates():
    logging.info('/updates handled')
    date = request.args.get('date')
    if validate.valid_date(date):
        return jsonify(helper.updates_help(date)), 200
    return jsonify(e.err400), 400


# обработчик get запроса /nodes/id/history
# request params: dateStart, dateEnd; elem_id - id файла/папки
@app.route('/node/<string:elem_id>/history', methods=['GET'])
def elem_history(elem_id):
    return jsonify(''), 200


if __name__ == '__main__':
    logging.info('Run app!')
    app.run()
