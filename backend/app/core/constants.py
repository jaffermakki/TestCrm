from enum import Enum


class UserRole(str, Enum):

    ADMIN = "ADMIN"

    MANAGER = "MANAGER"

    TECHNICIAN = "TECHNICIAN"

    CASHIER = "CASHIER"

    INVENTORY = "INVENTORY"

    SALES = "SALES"

    RECEPTION = "RECEPTION"

    VIEWER = "VIEWER"
