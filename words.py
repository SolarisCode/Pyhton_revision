"""Retrive and print words from a URL.

Usage:
    python3 words.py <URL>
"""

from sys import argv
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of UTF-8 text document.

    Return:
        A list of strings contains the all the words in the URL.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        story_words.extend(line.decode("utf-8").split())
    story.close()
    return (story_words)


def print_items(items):
    """Print items one per line.

    Args:
        items: An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of UTF-8 text document.
    """
    print(url)
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    main(argv[1])    #The 0th item would be the moudle name.
