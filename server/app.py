#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
    ]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)


@app.get("/contract/<int:contract_id>")
def get_contract(contract_id):
    """
    200: Contract found — return contract information.
    404: Contract not found.
    """
    for contract in contracts:
        if contract["id"] == contract_id:
            return make_response(contract["contract_information"], 200)
    return make_response("Contract not found", 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
