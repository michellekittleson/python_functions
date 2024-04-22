# Editorial Review: Extract a specific segment from a list in reverse.

# Start with a full list of article titles.
# Use slicing with negative indices to select the last three titles in reverse order.
# Remember that in Python, negative idices count from the end of the list.

articles = ["Article 1", "Article 2", "Article 3", "Article 4", "Article 5"]

recent_articles = articles[-1:-4:-1]
print(recent_articles)