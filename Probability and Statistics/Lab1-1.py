import random
total_flips = 10000
heads = 0
tails = 0
for i in range(total_flips):
    coin = round(random.random())
    if coin == 0:
        heads = heads + 1
    else:
        tails = tails + 1

print("number of heads: ", heads)
