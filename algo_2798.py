howmany_cards, max_num = map(int, input().split())
all_cards = list(map(int, input().split()))
store_list = []

for i in range(howmany_cards):
    for j in range(i+1,howmany_cards):
        for k in range(j+1, howmany_cards):
            sum_num = all_cards[i] + all_cards[j] + all_cards[k]
            store_list.append(sum_num)
            if howmany_cards ==3:
                break

#store_list = set(store_list)
store_list2 = []

for i in store_list:
    if max_num >=i:
        store_list2.append(i)


num_max = 0
for i in store_list2:
    if num_max < i:
        num_max = i
 
print(num_max)
