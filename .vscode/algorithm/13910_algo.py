wok, wok_count = map(int, input().split())

wok_size = input().split()

wok_size = sorted(wok_size)

while True:
    if wok%wok_size[0]==0:
        print(wok//wok_size[0])
        break