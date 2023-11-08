def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')
#Make a large shirt with the default message.
make_shirt()
#Make a medium shirt with the default message
make_shirt(size='medium')
#Make a shirt of any  size with a different message
make_shirt('small', 'Day and Night.')
