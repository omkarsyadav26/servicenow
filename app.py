from flask import Flask
from flask_restplus import Api, fields, Resource
import requests
import json


app = Flask(__name__)
api = Api(app)

cbs_model = api.model('Mod', {"amount": fields.Integer('12302313')})


@api.route('/budget-expense-line')
class Budget(Resource):
    def get(self):
        return "hello"


    # The below POST method takes input from CBS and creates new expense line in servicenow
    @api.expect(cbs_model)
    def post(self):
        val_list = []
        val_list.append(api.payload)
        url = 'https://dev67363.service-now.com/api/now/table/fm_expense_line'
        p = val_list[0]
        print(type(p))
        p["short_description"] = "---CBSTest---"
        p["user"] = "6816f79cc0a8016401c5a33be04be441"
        p = json.dumps(p)
        #
        print(p)
        payload = p
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.request('POST', url, headers=headers, data=payload, allow_redirects=False,
                                    auth=('admin', 'K3w1sTVeDtZl'))
        print(response)
        return {"result" : "expense line added in servicenow"}, 201



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
