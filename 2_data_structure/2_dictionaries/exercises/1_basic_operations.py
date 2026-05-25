# Creating a Dictionary
person = {
    "Name": "Hamid",
    "Age": 21,
    "City": "Pasrur"
}
print(f"Original: {person}")

# Access Values
print(f"Name: {person['Name']}")

# Add new Pair
person["Course"] = 'Python'
print(f"Added Course: {person}")

# Change value
person['Name'] = 'Ali'
print(f"Updated Name: {person}")

# Delete a Pair
if 'Name' in person:
    del person['Name']
print(f"Deleted Name: {person}")

# Loop in Dictionary
print("\nIterating:")
for key, value in person.items():
    print(f'{key}: {value}')

# Count frequency of words
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(f"\nWord Frequency: {freq}")

# Check key
print(f"Is 'Age' in person? {'Age' in person}")

# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(f"\nMerged: {dict1}")

# Create Dictionary from Tuples
keys = ["name", "age", "city"]
values = ["Hamid", 21, "Multan"]

my_dict = dict(zip(keys, values))
print(f"From Tuples: {my_dict}")
