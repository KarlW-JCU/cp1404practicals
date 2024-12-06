"""Wiki API Program"""

import wikipedia

search = input("Enter page title: ")
while search != "":
    try:
        page = wikipedia.page(search, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as error:
        print("We need a more specific title. Try one of the following, or a new search: ")
        print(error.options)
    except wikipedia.exceptions.PageError:
        print(f"Page id '{search}' does not match any pages. Try another id!")
    search = input("Enter page title: ")
print("Thank You.")
