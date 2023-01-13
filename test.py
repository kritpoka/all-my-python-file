import webbrowser
search_terms = [1]

# ... construct your list of search terms ...

for term in search_terms:
    url = "https://www.google.com.tr/search?q=youtube".format(term)
    webbrowser.open_new_tab(url)
