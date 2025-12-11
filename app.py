from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Dummy data store (replace this with your DB lookup)
# Key = RRN, Value = expected amount
TRANSACTIONS = {
    "123456789012": 1000.00,
    "987654321098": 250.50,
    "111122223333": 500.00,
}

@app.route("/validate", methods=["GET"])
def validate_get():
    rrn = request.args.get("rrn")
    amount = request.args.get("amount")

    # Basic checks
    if not rrn or not amount:
        return jsonify({
            "valid": False,
            "reason": "Please provide rrn and amount in query string"
        }), 400

    # Dummy DB
    TRANSACTIONS = {
        "123456789012": 1000.00,
        "987654321098": 250.50,
        "111122223333": 500.00,
    }

    # Validate RRN format
    if not rrn.isdigit() or len(rrn) != 12:
        return jsonify({
            "valid": False,
            "reason": "RRN format is invalid"
        }), 400

    # Check if RRN exists
    if rrn not in TRANSACTIONS:
        return jsonify({
            "valid": False,
            "reason": "RRN not found"
        }), 404

    expected_amount = TRANSACTIONS[rrn]

    # Compare amounts
    if float(amount) == float(expected_amount):
        return jsonify({
            "valid": True,
            "reason": "RRN and amount match",
            "rrn": rrn,
            "amount": float(amount)
        }), 200
    else:
        return jsonify({
            "valid": False,
            "reason": "Amount mismatch",
            "expected_amount": float(expected_amount),
            "provided_amount": float(amount)
        }), 200
if __name__ == "__main__":
    # Run the Flask dev server
    app.run(host="0.0.0.0", port=5000, debug=True)