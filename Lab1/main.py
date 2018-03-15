import hash_module


table = hash_module.HashTable()
with open('test_data.txt', 'r') as file:
    read_data = file.read().split(';')
sum_coll = 0
coll_elem_count = 0
for word in read_data:
    if (len(word) >= 3):
        coll_count = table.put_element(word)
        if (coll_count != -1):
            print("Element '%s' added! Collision count: %d" % (word, coll_count))
            coll_elem_count += 1
            sum_coll += coll_count
        else:
            print("Failed to add element '%s'." % (word))
    else:
        print("Failed to add element '%s': string contains < 3 symbols." % (word))
print("Average collisions: ", sum_coll/coll_elem_count)

table.print_table()

print(table.find_element("rifnur"))
print(table.find_element("sdsdsds"))
print(table.find_element("12321334"))




