new_customers = [101, 102, 103, 104, 105, 106]
repeat_customers = [103, 104, 105, 107, 108, 109]

# Convert lists to sets
set_new = set(new_customers)
set_repeat = set(repeat_customers)

# Find all unique customers
all_customers = set_new.union(set_repeat)

# Find customers who appear in both sets
shared_customers = set_new.intersection(set_repeat)

# Find new customers who are not repeat buyers
exclusive_new = set_new.difference(set_repeat)

# Print results
print(f"All customers: {all_customers}")
print(f"Shared customers: {shared_customers}")
print(f"Exclusive new customers: {exclusive_new}")