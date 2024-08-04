from prac_09.silver_service_taxi import SilverServiceTaxi

silver_service_taxi1 = SilverServiceTaxi("Mike", 100, 2)
print(silver_service_taxi1.price_per_km)
silver_service_taxi1.drive(18)
print(silver_service_taxi1.get_fare())