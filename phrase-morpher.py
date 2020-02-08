"""sentence-morpher.py

Little command-line tool to morph one phrase into another. See the example to 
get an idea of what I mean by this.

Example
-------
$ python sentence-converter.py 'Happiness is cool' 'Happiness is a warm gun'
Happiness is cool
Happiness is coo
Happiness is co
Happiness is c
Happiness is 
Happiness is a
Happiness is a w
Happiness is a wa
Happiness is a war
Happiness is a warm
Happiness is a warm g
Happiness is a warm gu
Happiness is a warm gun
Happiness is a warm gun
"""
import string
import argparse
import sys


def main(phrase1, phrase2):
    """Prints out phrase1, and then begins chopping off the last letter until 
    it is identical to the left side of phrase1, where it then starts adding 
    one letter at a time until it reaches phrase2. See the example below for a
    much better idea of what this does.
    
    Parameters
    ----------
    phrase1, phrase2: str

    Example
    -------
    >>> main('Happiness is cool', 'Happiness is a warm gun')
    Happiness is cool
    Happiness is coo
    Happiness is co
    Happiness is c
    Happiness is 
    Happiness is a
    Happiness is a w
    Happiness is a wa
    Happiness is a war
    Happiness is a warm
    Happiness is a warm g
    Happiness is a warm gu
    Happiness is a warm gun
    Happiness is a warm gun
    """
    while True:
        print(phrase1)
        if phrase1.lower() == phrase2.lower():
            return
        
        # If phrase1 is equal to the left side of phrase2, start adding letters
        if phrase1.lower() == phrase2[:len(phrase1)].lower():
            for char in phrase2[len(phrase1):]:
                phrase1 += char
                if char not in (*string.ascii_letters, *string.digits):
                    continue     
                print(phrase1)
            return
        else:
            phrase1 = phrase1[:-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Morph from one phrase into another.')
    parser.add_argument('phrase1', 
        help='The phrase you want to start with. If it requires whitespace, etc. make sure you wrap it in quotation marks.',
    )
    parser.add_argument('phrase2', 
        help='The phrase you want to end with. If it requires whitespace, etc. make sure you wrap it in quotation marks.',
    )

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    main(args.phrase1, args.phrase2)
