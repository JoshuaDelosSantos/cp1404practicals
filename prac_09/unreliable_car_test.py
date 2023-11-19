"""
CP1404 prac_09
unreliable_car_test.py
"""

from prac_09.unreliable_car import UnreliableCar

unreliable_car = UnreliableCar(name="Max", fuel=200, reliability=20)
print(unreliable_car)

unreliable_car.drive(30)
print(unreliable_car)
