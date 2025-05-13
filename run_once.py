# run_once.py (istersen ayrı dosya yap)

from scraper import scrape_wikipedia
from indexer import create_table, insert_document

keywords = [
    "Python_(programming_language)",
    "Machine_learning",
    "Artificial_intelligence",
    "Web_scraping",
    "Natural_language_processing"
]

create_table()

for keyword in keywords:
    data = scrape_wikipedia(keyword)
    if data:
        insert_document(data['title'], data['url'], data['content'])
        print(f"✅ Eklendi: {data['title']}")
