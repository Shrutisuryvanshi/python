tuple1=(1,2,3,4,5,4,3,6)
seen_items=set()
repeated_items=set()
for item in tuple1:
    if item in seen_items:
        repeated_items.add (item)
    else:
            seen_items.add(item)
            print("repeated item in the tuple",repeated_items)
