def get_top_n_frequent(items, n):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    items_with_count = []
    for item in unique_items:
        freq = items.count(item)
        items_with_count.append((item, freq))
    print(items_with_count)
    items_with_count.sort
    print(items_with_count)
    part = items_with_count(-n)
    print(part)
    part 


votes = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple', 'grape']
n = 2
get_top_n_frequent(votes, n)

print(result)
print()
 