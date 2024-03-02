from enum import Enum

class Car:
    def __init__(self, vin: str, total_charged_kwh: int, max_current_kw: int):
        self.vin = vin
        self.total_charged_kwh = total_charged_kwh
        self.max_current_kw = max_current_kw

class ClientAccount:
    def __init__(self, id: int, name: str, funds: float):
        self.id = id
        self.name = name
        self.funds = funds
        
class ChargerStatus(Enum):
    FREE = "Free"
    CHARGING = "Charging"
    ERROR = "Error"

class Charger:
    def __init__(self, max_current_kw: int, total_charged_kw: int, status: ChargerStatus):
        self.max_current_kw = max_current_kw
        self.total_charged_kw = total_charged_kw
        self.status = status
