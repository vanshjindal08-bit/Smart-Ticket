from data.seat_data import seat_inventory, booking_history
import datetime

def book_ticket(category):
    if category not in seat_inventory:
        return False

    if seat_inventory[category]["available"] > 0:
        seat_inventory[category]["available"] -= 1

        booking_history.append({
            "category": category,
            "time": datetime.datetime.now()
        })

        return True
    else:
        return False
