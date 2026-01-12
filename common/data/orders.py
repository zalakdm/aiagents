"""
Sample order data for the mock order database.
Simulates orders for an online retailer like amazaon.
"""

from datetime import datetime, timedelta

# Generate dynamic dates relative to today
today = datetime.now()

SAMPLE_ORDERS = {
    "12345": {
        "order_id": "12345",
        "status": "Delivered",
        "order_date": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
        "estimated_delivery": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
        "actual_delivery": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
        "tracking_number": "TRK123456789",
        "items": [
            {
                "id": "ITEM001",
                "title": "Cotton T-Shirt",
                "description": "100% organic cotton, white, size M",
                "quantity": 2,
                "price": 29.99
            },
            {
                "id": "ITEM002",
                "title": "Flare Jeans",
                "description": "Dark wash denim, size 29",
                "quantity": 1,
                "price": 79.99
            }
        ],
        "total": 139.97,
        "shipping_address": "123 Main St, Sunnyvale, CA 98101"
    },
    "12346": {
        "order_id": "12346",
        "status": "Shipped",
        "order_date": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
        "estimated_delivery": (today + timedelta(days=2)).strftime("%Y-%m-%d"),
        "actual_delivery": None,
        "tracking_number": "TRK987654321",
        "items": [
            {
                "id": "ITEM003",
                "title": "Summer Dress",
                "description": "Floral pattern, cotton blend, size S",
                "quantity": 1,
                "price": 59.99
            }
        ],
        "total": 59.99,
        "shipping_address": "456 Oak Ave, Boston, CA 97201"
    },
    "12347": {
        "order_id": "12347",
        "status": "Processing",
        "order_date": today.strftime("%Y-%m-%d"),
        "estimated_delivery": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
        "actual_delivery": None,
        "tracking_number": None,
        "items": [
            {
                "id": "ITEM004",
                "title": "Leather Jacket",
                "description": "Genuine leather, brown, size M",
                "quantity": 1,
                "price": 209.99
            },
            {
                "id": "ITEM005",
                "title": "Wool Scarf",
                "description": "Merino wool, burgundy",
                "quantity": 1,
                "price": 39.99
            }
        ],
        "total": 249.98,
        "shipping_address": "782 Pine Rd, San Francisco, CA 94086"
    },
    "12348": {
        "order_id": "12348",
        "status": "Shipped",
        "order_date": (today - timedelta(days=5)).strftime("%Y-%m-%d"),
        "estimated_delivery": (today + timedelta(days=1)).strftime("%Y-%m-%d"),
        "actual_delivery": None,
        "tracking_number": "TRK456789123",
        "items": [
            {
                "id": "ITEM006",
                "title": "Running Shoes",
                "description": "Performance athletic shoes, white/blue, size 7",
                "quantity": 1,
                "price": 89.99
            }
        ],
        "total": 89.99,
        "shipping_address": "321 Elm St, New York, NY 78701"
    },
    "12349": {
        "order_id": "12349",
        "status": "Delivered",
        "order_date": (today - timedelta(days=15)).strftime("%Y-%m-%d"),
        "estimated_delivery": (today - timedelta(days=8)).strftime("%Y-%m-%d"),
        "actual_delivery": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
        "tracking_number": "TRK789123456",
        "items": [
            {
                "id": "ITEM007",
                "title": "Cashmere Sweater",
                "description": "Pure cashmere, brown, size M",
                "quantity": 1,
                "price": 149.99
            }
        ],
        "total": 149.99,
        "shipping_address": "654 Maple Dr, Cambridge, MA 02101"
    }
}