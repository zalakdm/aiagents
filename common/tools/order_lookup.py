"""
Order lookup tool with mock database for customer support agent.
Simulates order status checking for an online retailer like amazon.
"""
from typing import Dict, List, Optional
from langchain_core.tools import tool
from common.data.orders import SAMPLE_ORDERS

class OrderDB:
    """
    Mock order database for demonstration purposes.
    In production, this would connect to a real database or API.
    """
    def __init__(self):
        """Initialize the mock order database with sample orders."""
        self._orders = SAMPLE_ORDERS
    
    def get_order(self, order_id: str) -> Optional[Dict]:
        """
        Retrieve order details by order ID.
        
        Args:
            order_id: The order ID to look up
            
        Returns:
            Order dictionary if found, None otherwise
        """
        order = self._orders.get(order_id)
        
        if order:
            return  order #f"Order found: {order_id}, status: {order['status']}"
        else:
            return None #f"Order not found: {order_id}"
    
    def list_orders(self) -> List[str]:
        """
        List all order IDs in the database.
        
        Returns:
            List of order IDs
        """
        return list(self._orders.keys())

# Global order database instance
_order_db = OrderDB()


def get_order_database() -> OrderDB:
    """
    Get the global order database instance.
    
    Returns:
        OrderDatabase instance
    """
    return _order_db

@tool
def get_order_status(order_id: str) -> str:
    """
    Look up the status and details of a customer order.
    
    Use this tool when a customer asks about their order status, delivery date,
    tracking information, or order details. Provide the order ID to get complete
    information including items ordered, shipping status, and delivery estimates.
    
    Args:
        order_id: The order ID to look up (e.g., "12345")
        
    Returns:
        A formatted string with order details, or an error message if not found
        
    Example:
        >>> get_order_status("12345")
        "Order #12345 Status: Delivered\\n..."
    """
    print(f"Order lookup tool called for order: {order_id}")
    
    try:
        db = get_order_database()
        order = db.get_order(order_id)
        
        if not order:
            return f"Order #{order_id} not found. Please check the order ID and try again."
        
        # Format the order details
        result = f"""Order #{order['order_id']} Details:

                    Status: {order['status']}
                    Order Date: {order['order_date']}
                    Estimated Delivery: {order['estimated_delivery']}
                    """
        
        if order.get('actual_delivery'):
            result += f"Delivered On: {order['actual_delivery']}\n"
        
        if order.get('tracking_number'):
            result += f"Tracking Number: {order['tracking_number']}\n"
        
        result += f"\nItems Ordered:\n"
        for item in order['items']:
            result += f"- {item['title']}: {item['description']} (Qty: {item['quantity']}, ${item['price']:.2f})\n"
        
        result += f"\nTotal: ${order['total']:.2f}"
        result += f"\nShipping Address: {order['shipping_address']}"
        
        print(f"Order lookup success - order: {order_id}, status: {order['status']}, items: {len(order['items'])}")
        
        return result
        
    except Exception as e:
        print(f"Order lookup error for {order_id}: {str(e)}")
        return f"An error occurred while looking up order #{order_id}. Please try again later."