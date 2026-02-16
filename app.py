from flask import Flask, render_template, request
from services.booking_service import book_ticket
from services.fraud_service import check_fraud
from services.marketing_service import generate_offer
from data.seat_data import seat_inventory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", seats=seat_inventory)


@app.route("/book", methods=["POST"])
def book():
    category = request.form.get("category")
    user_id = request.form.get("user_id")

    # Fraud check
    if check_fraud(user_id):
        return render_template("error.html", message="Suspicious booking activity detected!")

    success = book_ticket(category)

    if success:
        offer = generate_offer(category)
        return render_template("success.html", category=category, offer=offer)
    else:
        return render_template("error.html", message="Seat not available!")

if __name__ == "__main__":
    app.run(debug=True)



