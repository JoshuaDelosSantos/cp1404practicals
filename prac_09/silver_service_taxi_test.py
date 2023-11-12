"""
CP1404 prac_09
silver_service_taxi_test.py
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi(name="Fancy Boi", fuel=1000, fanciness=2)
print(silver_taxi)

silver_taxi.drive(18)
print(silver_taxi)
print(silver_taxi.get_fare())
