from services.demand_service import calculate_demand

def generate_offer(category):
    demand = calculate_demand(category)

    if demand == "Low":
        return "Special discount available!"
    else:
        return None
