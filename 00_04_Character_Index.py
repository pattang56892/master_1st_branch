# new feature
# characters = ["Krillin", "Goku", "Vegeta", "Gohan", "Piccolo"]

# # enumerate() returns a sequence of (index, item) tuples

# list(enumerate(characters))

# # Use enumerate() in a for loop to get an item and its index

# for index, character in enumerate(characters):
#     character_map = {character: [] for character in set(characters)}
#     character_map[character].append(index)
#     print(index, character)
#     print(character_map)

# Why might you want to use enumerate?
# Example: store index positions of duplicate items

characters = ["Krillin", "Goku", "Goku", "Gohan", "Piccolo",
              "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
              "Piccolo", "Goku", "Vegeta", "Goku", "Piccolo"]

# list(enumerate(characters))

characters_map = {character: [] for character in set(characters)}

for index, characters in enumerate(characters):
    characters_map[characters].append(index)

print(characters_map)
