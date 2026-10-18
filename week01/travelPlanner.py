# Travel Weather Planner from FreeCodeCamp.org
distance_mi = 100
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True
if not distance_mi:
    print(False)
elif distance_mi <= 1 and not is_raining:
    print(True)
elif distance_mi > 1 and distance_mi <= 6:
    if not has_bike and is_raining:
        print(False)
    elif not has_bike and not is_raining:
        print(False)
    elif has_bike and not is_raining:
        print(True)
    elif has_bike and is_raining:
        print(False)
elif distance_mi > 6:
    if has_ride_share_app:
        print(True)
    elif has_car:
        print(True)
    elif not has_car and not has_ride_share_app:
        print(False)
else: 
    print(False)