from collections import deque

DAYS = 7

daily_portion = deque([int(x) for x in input().split(", ")])
daily_stamina = deque([int(x) for x in input().split(", ")])

mountain_peaks = deque([('Vihren', 80), ('Kutelo', 90), ('Banski Suhodol', 100), ('Polezhan', 60), ('Kamenitza', 70)])
mountain_conquered = []

while daily_portion and daily_stamina and mountain_peaks:
    curr_portion = daily_portion.pop()
    curr_stamina = daily_stamina.popleft()
    curr_sum = curr_stamina + curr_portion
    curr_mountain, curr_level = mountain_peaks.popleft()

    if curr_sum < curr_level:
        mountain_peaks.appendleft((curr_mountain, curr_level))
    else:
        mountain_conquered.append(curr_mountain)


if len(mountain_peaks) == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if mountain_conquered:
    print("Conquered peaks:")
    [print(mountain) for mountain in mountain_conquered]