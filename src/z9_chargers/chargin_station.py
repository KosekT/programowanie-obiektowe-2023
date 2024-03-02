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
        
class ChargingStatus(Enum):
    OPEN = "Open"
    ERROR = "Error"
    FINISHED = "Finished"

class ChargingSession:
    def __init__(self, csid: int, car_vin: str, charger_id: int, client_id: int, status: ChargingStatus, current_kw: int, total_kwh: int):
        self.csid = csid
        self.car_vin = car_vin
        self.charger_id = charger_id
        self.client_id = client_id
        self.status = status
        self.current_kw = current_kw
        self.total_kwh = total_kwh

    def __str__(self):
        return f"Charging Session with ID {self.csid}, car VIN: {self.car_vin}, charger ID: {self.charger_id}, client ID: {self.client_id}, status: {self.status.value}, current kW: {self.current_kw}, total kWh: {self.total_kwh}"

class ChargingService:
    def __init__(self, chargers: list, time_modifier: float):
        self.chargers = chargers
        self.time_modifier = time_modifier

    def start_charging(self, client_id, vin, kwh, desired_current_kw, charger_position: int):
        # check if charger available and supports such desired_current
        charger = self.chargers[charger_position]
        if charger.status == ChargingStatus.FINISHED:
            charger.status = ChargingStatus.OPEN
            charger.current_kw = desired_current_kw
            charger.total_kwh = kwh
            return True
        return False

    def stop_charging(self, client_id, vin):
        for charger in self.chargers:
            if charger.status == ChargingStatus.OPEN and charger.car_vin == vin:
                charger.status = ChargingStatus.FINISHED
                return True
        return False

    def attach_charger(self, charger):
        self.chargers.append(charger)

    def disable_charger(self, charger_position: int):
        self.chargers[charger_position].status = ChargingStatus.ERROR

    def enable_charger(self, charger_position: int):
        self.chargers[charger_position].status = ChargingStatus.OPEN

    def remove_charger(self, charger):
        self.chargers.remove(charger)
