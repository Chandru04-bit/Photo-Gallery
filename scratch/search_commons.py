import urllib.request
import json
import urllib.parse

headers = {'User-Agent': 'UTSAVWebsiteAuditor/1.0 (contact@utsavdecor.com)'}

def search_commons(query, limit=5):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrlimit={limit}&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            results = []
            for pid, p in pages.items():
                if 'imageinfo' in p and p['imageinfo']:
                    info = p['imageinfo'][0]
                    results.append({
                        'title': p.get('title'),
                        'url': info.get('url'),
                        'width': info.get('width'),
                        'height': info.get('height')
                    })
            return results
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

queries = [
    "wedding mandap India",
    "wedding reception stage",
    "corporate conference stage",
    "birthday party decoration",
    "wedding floral arch",
    "stage lighting truss",
    "marquee tent wedding"
]

for q in queries:
    res = search_commons(q, 3)
    print(f"\nQuery '{q}': {len(res)} results")
    for item in res:
        print(f"  {item['title']} | {item['width']}x{item['height']} | {item['url']}")
