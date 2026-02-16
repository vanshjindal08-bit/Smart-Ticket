from data.seat_data import seat_inventory

def calculate_demand(category):
    total = seat_inventory[category]["total"]
    available = seat_inventory[category]["available"]

    sold_percentage = ((total - available) / total) * 100

    if sold_percentage > 70:
        return "High"
    elif sold_percentage > 40:
        return "Medium"
    else:
        return "Low"
