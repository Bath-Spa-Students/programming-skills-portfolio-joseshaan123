# Create a dictionary called 'glossary' with key-value pairs, defining terms and their explanations.
glossary = {
    'string': 'They are a series of characters.',
    'comment': 'The lines in the code that are ignored by the interpreter during the execution of the program.',
    'list': 'A data structure in Python that is mutable, or changeable.',
    'loop': 'Repeating something over and over until a particular condition is satisfied.',
    'dictionary': 'It consists of a collection of key-value pairs.',
}

# Print the explanations for specific terms from the 'glossary' dictionary using their respective keys.
word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")
