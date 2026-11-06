import urllib.request
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_unsplash_ids(query):
    url = f"https://unsplash.com/napi/search/photos?query={urllib.parse.quote(query)}&per_page=15"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            for item in data.get('results', []):
                results.append({
                    'id': item['id'],
                    'desc': item.get('description') or item.get('alt_description') or '',
                    'url': item['urls']['regular'],
                    'raw': item['urls']['raw']
                })
            return results
    except Exception as e:
        print(f"Error querying {query}: {e}")
        return []

queries = [
    "indian wedding mandap",
    "wedding stage decoration",
    "birthday party decoration balloons",
    "corporate conference stage",
    "wedding entrance arch flowers",
    "stage lighting truss",
    "outdoor marquee tent wedding"
]

for q in queries:
    res = search_unsplash_ids(q)
    print(f"\nQuery: '{q}' found {len(res)} results:")
    for r in res[:3]:
        print(f"  ID: {r['id']} | Desc: {r['desc'][:60]} | URL: {r['url'][:70]}...")
