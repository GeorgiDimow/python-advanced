numbers = list(map(int, input().split()))

pos_nums = list(filter(lambda x: x > 0, numbers))
neg_nums = list(filter(lambda x: x < 0, numbers))

sum_pos = sum(pos_nums)
sum_neg = sum(neg_nums)

print(sum_neg)
print(sum_pos)
print("The negatives are stronger than the positives" if abs(sum_neg) > sum_pos else "The positives are stronger than the negatives")
