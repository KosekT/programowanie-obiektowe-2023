class Car:
    def __init__(self, vin: str, total_charged_kwh: int, max_current_kw: int):
        self.vin = vin
        self.total_charged_kwh = total_charged_kwh
        self.max_current_kw = max_current_kw
