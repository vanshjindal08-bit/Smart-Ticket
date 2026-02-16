from data.seat_data import user_booking_count

def check_fraud(user_id):
    if user_id not in user_booking_count:
        user_booking_count[user_id] = 0

    user_booking_count[user_id] += 1

    if user_booking_count[user_id] > 3:
        return True

    return False
