from openai import function_tool

ORDERS_DB = {
    "123": "Shipped",
    "456": "Processing",
    "789": "Delivered"
}

@function_tool(
    name="get_order_status",
    description="Check the status of a customer's order using order_id",
    is_enabled=lambda query, **kwargs: "order" in query.lower(),
    error_function=lambda order_id: f"Sorry, I couldn't find order ID {order_id}. Please check and try again."
)
def get_order_status(order_id: str) -> str:
    return ORDERS_DB.get(order_id, get_order_status.error_function(order_id))
