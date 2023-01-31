from collections import deque

green_light = int(input())
free_window = int(input())
cars_queue = deque()
info = input()
total_cars = 0

while info != "END":

    if info == "green":
        curr_green = green_light
        curr_window = free_window

        while curr_green > 0 and cars_queue:
            car = cars_queue.popleft()
            time = curr_window + curr_green
            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            curr_green -= len(car)
            total_cars += 1
    else:
        cars_queue.append(info)

    info = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
