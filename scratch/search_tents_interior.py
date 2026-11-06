import urllib.request
import json
import urllib.parse

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) UTSAVDecor/1.0'}

def search_commons(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(query)}&gsrlimit=6&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                if 'imageinfo' in p and p['imageinfo']:
                    info = p['imageinfo'][0]
                    mime = info.get('mime', '')
                    if 'jpeg' in mime or 'jpg' in mime:
                        w = info.get('width', 0)
                        h = info.get('height', 0)
                        if w > 1200 and h > 800:
                            print(f"[{p.get('title')}] {w}x{h} => {info.get('url')}")
    except Exception as e:
        print(f"Error: {e}")

for q in [
    'wedding marquee interior',
    'marquee tent interior banquet',
    'wedding tent chandelier interior',
    'marquee wedding banquet',
    'garden marquee wedding'
]:
    print(f"\n=== {q} ===")
    search_commons(q)
