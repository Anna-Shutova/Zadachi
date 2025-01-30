car_speed = 150
motorcycle_speed = 150
if car_speed > motorcycle_speed:
    print("Car is faster than motorcycle")
    motorcycle_speed += 50
elif motorcycle_speed > car_speed:
    print("Motorcycle is faster than car")
    motorcycle_speed += 50
else:
    print("Car and motorcycle are equally fast")
    motorcycle_speed += 50
