glossary = {
    'string': 'A series of characters.',
    'comment': 'the lines in the code that are ignored by the interpreter during the execution of the program.',
    'list': 'a data structure in Python that is a mutable, or changeable.',
    'loop': 'repeating something over and over until a particular condition is satisfied..',
    'dictionary': " It consists of a collection of key-value pairs.",
    'key': 'Keys are immutable datatype.',
    'value': 'They are numbers or words that are needed for programing.',
    'conditional test': 'It shows us the differece between 2 values.',
    'float': 'It converts any value in fractional and decimal number.',
    'boolean expression': 'They are expressions that analyze whther it is true or false.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")