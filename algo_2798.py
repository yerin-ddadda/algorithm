howmany_cards, max_num = map(int, input().split())
cards = list(map(int, input().split()))
print_num = 0
lst = []

for i in range(3):
    lst[i] = cards[i]

if sum(lst) < 21:
    for i in range(3):
        

print(max_num)