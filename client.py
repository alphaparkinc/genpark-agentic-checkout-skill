import hashlib, time

class AgenticCheckoutClient:
    TAX_RATE = 0.08
    SHIPPING_RATES = {"standard": 5.99, "express": 14.99, "free": 0.0}

    def checkout(self, cart_items: list, payment_method: dict, shipping_address: dict) -> dict:
        # Validate inputs
        if not cart_items:
            return {"order_id": "", "total_usd": 0, "status": "FAILED: Empty cart", "receipt": {}}
        if not payment_method.get("type"):
            return {"order_id": "", "total_usd": 0, "status": "FAILED: No payment method", "receipt": {}}

        subtotal = sum(item.get("price", 0) * item.get("qty", 1) for item in cart_items)
        shipping_type = payment_method.get("shipping_tier", "standard")
        shipping_cost = self.SHIPPING_RATES.get(shipping_type, 5.99)
        tax = round(subtotal * self.TAX_RATE, 2)
        total = round(subtotal + shipping_cost + tax, 2)

        # Generate order
        order_id = "ORD-" + hashlib.md5(f"{time.time()}{subtotal}".encode()).hexdigest()[:8].upper()
        receipt = {
            "order_id": order_id,
            "items": [{"name": i.get("name"), "qty": i.get("qty", 1), "price": i.get("price")} for i in cart_items],
            "subtotal": round(subtotal, 2),
            "tax": tax,
            "shipping": shipping_cost,
            "total": total,
            "payment_type": payment_method.get("type"),
            "ship_to": shipping_address.get("city", "N/A"),
            "acp_protocol": "v1.0",
            "timestamp": int(time.time())
        }
        return {"order_id": order_id, "total_usd": total, "status": "SUCCESS", "receipt": receipt}
