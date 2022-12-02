"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
     
    # Your code goes here
    for item in items:
        frequencies[str(item)]= frequencies.get(str(item), 0)+1
        #Will increment everytime an item is the same 
    return frequencies
