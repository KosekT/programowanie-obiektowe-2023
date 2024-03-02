from enum import Enum
import unittest
from chargin_station import *

class TestChargingService(unittest.TestCase):
    def setUp(self):
        self.charger1 = Charger(10, 50, ChargerStatus.FREE)
        self.charger2 = Charger(15, 60, ChargerStatus.FREE)
        self.charger3 = Charger(20, 70, ChargerStatus.FREE)

        self.chargers = [self.charger1, self.charger2, self.charger3]

        self.charging_service = ChargingService(self.chargers, 1.0)

    def test_start_charging(self):
        charging_session = ChargingSession(1, "ABC123", 1, 1, ChargingStatus.FINISHED, 0, 0)
        self.charger1.status = ChargingStatus.FINISHED

        self.assertTrue(self.charging_service.start_charging(1, "ABC123", 50, 10, 0))
        self.assertEqual(self.charger1.status, ChargingStatus.OPEN)

    def test_stop_charging(self):
        charging_session = ChargingSession(1, "ABC123", 1, 1, ChargingStatus.OPEN, 0, 0)
        self.charger1.status = ChargingStatus.OPEN

        self.assertTrue(self.charging_service.stop_charging(1, "ABC123"))
        self.assertEqual(self.charger1.status, ChargingStatus.FINISHED)

    def test_attach_charger(self):
        charger4 = Charger(25, 80, ChargerStatus.FREE)
        self.charging_service.attach_charger(charger4)
        self.assertIn(charger4, self.chargers)

    def test_disable_charger(self):
        self.charging_service.disable_charger(0)
        self.assertEqual(self.charger1.status, ChargingStatus.ERROR)

    def test_enable_charger(self):
        self.charging_service.disable_charger(0)
        self.charging_service.enable_charger(0)
        self.assertEqual(self.charger1.status, ChargingStatus.OPEN)

    def test_remove_charger(self):
        self.charging_service.remove_charger(self.charger1)
        self.assertNotIn(self.charger1, self.chargers)

if __name__ == '__main__':
    unittest.main()
