from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent="geoapiExercises")

c1 = (input("1 place " ) )
c2 = (input("2 place " ) )

l1 = geolocator.geocode(c1)
l2 = geolocator.geocode(c2)

loc1=((l1.latitude,l1.longitude))
loc2=((l2.latitude,l2.longitude))

print(distance.distance(loc1,loc2).km,"Kms")
print("It is approx distance kindly dont take serious :-) ")