from scholarly import scholarly

# Replace with your name or unique Google Scholar author ID
search_query = scholarly.search_author('Shahadat Hussain')
author = next(search_query)  # Get the first search result
scholarly.fill(author)  # Fill the author details with citation data

# Extract the stats
publications = author['publications']
citations = author['citedby']
h_index = author['hindex']
i10_index = author['i10index']

# Print or save the stats to update your README file
print(f"Total Publications: {len(publications)}")
print(f"Total Citations: {citations}")
print(f"h-index: {h_index}")
print(f"i10-index: {i10_index}")
