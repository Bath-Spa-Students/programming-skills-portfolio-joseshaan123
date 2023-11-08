# Create a list called 'locations' containing four place names.
locations = ['Kerala', 'Karnataka', 'Tamil Nadu', 'Delhi']

# Print the original order of the list.
print("Original order:")
print(locations)

# Print the list in alphabetical order without modifying the original list.
print("\nAlphabetical:")
print(sorted(locations))

# Print the original order of the list (no changes made to the original list).
print("\nOriginal order:")
print(locations)

# Print the list in reverse alphabetical order without modifying the original list.
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

# Print the original order of the list (no changes made to the original list).
print("\nOriginal order:")
print(locations)

# Reverse the order of the list in place.
print("\nReversed:")
locations.reverse()
print(locations)

# Print the original order of the list.
print("\nOriginal order:")
locations.reverse()
print(locations)

# Sort the list in alphabetical order in place.
print("\nAlphabetical:")
locations.sort()
print(locations)

# Sort the list in reverse alphabetical order in place.
print("\nReverse alphabetical:")
locations.sort(reverse=True)
print(locations)
