def ArrayChallenge(strArr):
    number_gas_stations = int(strArr[0])
    strArr.pop(0)
    gas_stations_amount = [int(gas.split(":")[1]) for gas in strArr]

    for routes in range(number_gas_stations):
        starting_gallons = 0
        gas_station_pos = routes

        for _ in range(number_gas_stations):
            if gas_station_pos > number_gas_stations - 1:
                gas_station_pos = 0

            starting_gallons += int(strArr[gas_station_pos].split(":")[0])

            if gas_stations_amount[gas_station_pos] > starting_gallons:
                break

            starting_gallons -= gas_stations_amount[gas_station_pos]

            gas_station_pos += 1

        else:
            return routes + 1

    return "impossible"


print(ArrayChallenge(["4", "0:1", "2:2", "1:2", "3:1"]))