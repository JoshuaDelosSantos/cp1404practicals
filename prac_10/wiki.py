"""
CP1404 prac_10
wiki.py
"""

import wikipedia

try:
    search_phrase = input("Enter a search phrase: ")
    while search_phrase != "":
        wikipedia_page = wikipedia.page(search_phrase)
        print(wikipedia_page.title)
        print(wikipedia_page.summary)
        print(wikipedia_page.url)
        search_phrase = input("Enter a search phrase: ")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)
