"""
Shared tools package for all stages.
Contains tools for customer support agents.
"""

# Stage 1 tools
from common.tools.order_lookup import get_order_status, OrderDB

__all__ = [
    # Stage 1 tools
    "get_order_status",
    "OrderDB"
]

# Convenient tool collections
STAGE_1_TOOLS = [get_order_status]