# A frozen set is an immutable version of a set. Once created, its elements cannot be changed.
frozen = frozenset([1, 2, 3])
print(frozen) 

# Membership test
print(2 in frozen) 

# frozen.add(4)  # Raises an error: 'frozenset' object has no attribute 'add'
