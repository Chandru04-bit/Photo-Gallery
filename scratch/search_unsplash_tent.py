import urllib.request
import json
import urllib.parse
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def search_unsplash(query):
    url = f"https://unsplash.com/napi/search/photos?query={urllib.parse.quote(query)}&per_page=5"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for r in data.get('results', []):
                print(r.get('id'), r.get('description') or r.get('alt_description'), r.get('urls', {}).get('regular'))
    except Exception as e:
        print(f"Error: {e}")

search_unsplash("wedding tent reception lawn evening")
