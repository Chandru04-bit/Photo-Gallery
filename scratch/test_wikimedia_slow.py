import urllib.request
import json
import urllib.parse
import time

headers = {'User-Agent': 'UTSAVContractorImageBot/1.1 (https://utsavdecor.com; support@utsavdecor.com)'}

def search_wikimedia(query):
    time.sleep(1.2)  # Avoid 429 rate limit
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(query)}&gsrlimit=3&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                if 'imageinfo' in p and p['imageinfo']:
                    info = p['imageinfo'][0]
                    mime = info.get('mime', '')
                    if 'image/' in mime:
                        title = p.get('title', '').encode('ascii', 'ignore').decode('ascii')
                        print(f"  {title} | {info.get('width')}x{info.get('height')} | {info.get('url')}")
    except Exception as e:
        print(f"  Error: {e}")

queries = [
    "wedding mandap India",
    "birthday balloons decoration",
    "conference keynote stage auditorium",
    "concert stage lighting rig",
    "wedding floral arch flowers"
]

for q in queries:
    print(f"\nQuery: {q}")
    search_wikimedia(q)
