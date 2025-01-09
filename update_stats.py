from scholarly import scholarly

# Fetch the author info from Google Scholar
search_query = scholarly.search_author('Shahadat Hussain')
author = next(search_query)
scholarly.fill(author)

# Extract statistics
publications = author['publications']
citations = author['citedby']
h_index = author['hindex']
i10_index = author['i10index']

# Generate markdown content for the README
readme_content = f"""
## 📊 Research Statistics

| Statistic        | Value |
|------------------|-------|
| **Publications** | {len(publications)}    |
| **Citations**    | {citations}   |
| **h-index**      | {h_index}     |
| **i10-index**    | {i10_index}   |

![Publications](https://img.shields.io/badge/Publications-{len(publications)}-blue?style=for-the-badge)
![Citations](https://img.shields.io/badge/Citations-{citations}-green?style=for-the-badge)
![h-index](https://img.shields.io/badge/h--index-{h_index}-orange?style=for-the-badge)
![i10-index](https://img.shields.io/badge/i10--index-{i10_index}-yellow?style=for-the-badge)
"""

# Write the updated content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
