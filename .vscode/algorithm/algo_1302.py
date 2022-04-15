number = int(input())
book_list = {}
for i in range(number):
    book = input()
    if book in book_list:
        book_list[book] += 1
    else:
        book_list[book] =1
print(book_list)

order_book = []
for i in book_list:
    order_book.append((i, book_list[i]))
    print(order_book)
order_book = sorted(order_book, key=lambda x:(-x[1], x[0]))
print(order_book)