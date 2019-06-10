from flask import Flask
from flask_restplus import Api, fields, Resource
import requests
from log import logging
import json
from restCall import calling
import threading

app = Flask(__name__)
api = Api(app)

cbs_model = api.model('Mod', {"amount": fields.Integer})

@api.route('/budget-expense-line')
class Budget(Resource):
    @api.expect(cbs_model)
    def post(self):
        inventory_details = api.payload
        order_number = inventory_details["orderID"]
        order_url = "http://cb-order-service:7070/v4/api/orders/" + \
            order_number + "/detail/internal"
        order_details = requests.request('GET', order_url).json()
        logging.info("order_details")
        logging.info(str(order_details))
        order_amount = order_details["data"]["orderAmount"]
        url = 'https://dev67363.service-now.com/api/now/table/fm_expense_line'
        payload = {
            "short_description":  "---CBSTest---",
            "user": "6816f79cc0a8016401c5a33be04be441",
            "amount": order_amount
        }

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        logging.info(str(payload))
        response = requests.request(
            'POST', url, headers=headers, json=payload, auth=('admin', 'K3w1sTVeDtZl'))
        logging.info(str(response))
        threadVar = threading.Thread(target=calling, args=(arr,))
        threadVar.start()
        return {"result": "expense line added in servicenow"}, 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
