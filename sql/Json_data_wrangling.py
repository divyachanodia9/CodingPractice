# import json

# with open("C:/Users/divya/Projects/CodingPractice/Json_date.json", "r") as file:
#     orders = json.load(file)

# print(orders)

# print(orders[0]["order_id"])  #1st order id
# print(orders[0]["status"]) #1st order's status

# #Id's of delivered orders

# def get_delivered_orders_id(orders):
#     result = []

#     for order in orders:
#         if order["status"] == "delivered":
#             result.append(order["order_id"])
#     return result

# print(get_delivered_orders_id(orders))

import requests

def fetch_and_process_orders(api_url):
    response = requests.get(api_url,time_out = 10)
    orders = response.json()

    result = []
    # 1. Extract each order ID, customer name, and latest status.

    for order in orders:
        order_id = order.get("order_id")

        customer = order.get("customer") or {} #handling missing data.
        customer_name = customer.get("name")

        events = order.get("events") or []

        unique_events = []
        seen_events = set()

        for event in events:
            status = event.get("status")
            timestamp = event.get("timestamp")

            event_key = (status,event_time)
            if event_key in seen_events:
                continue
            seen_events.add(event_key)


        if not status or not timestamp:
            continue