from client import AgenticCheckoutClient
client = AgenticCheckoutClient()
result = client.checkout(
    cart_items=[
        {"name": "Sony WH-1000XM6", "price": 349.99, "qty": 1},
        {"name": "USB-C Cable 2m", "price": 12.99, "qty": 2}
    ],
    payment_method={"type": "stripe_card", "last4": "4242", "shipping_tier": "express"},
    shipping_address={"city": "San Francisco", "state": "CA", "zip": "94102"}
)
print(f"Status: {result['status']}")
print(f"Order ID: {result['order_id']}")
print(f"Total: ${result['total_usd']}")
print(f"ACP Protocol: {result['receipt']['acp_protocol']}")
