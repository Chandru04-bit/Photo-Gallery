import urllib.request
import json
import urllib.parse

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) UTSAVDecor/1.0'}

def search(q):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(q)}&gsrlimit=5&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                if 'imageinfo' in p and p['imageinfo']:
                    info = p['imageinfo'][0]
                    t = p.get('title', '')
                    w = info.get('width', 0)
                    h = info.get('height', 0)
                    u = info.get('url', '')
                    print(f"  [{t}] {w}x{h} => {u}")
    except Exception as e:
        print(f"Error: {e}")

queries = [
    'wedding pandal decoration',
    'marriage pandal',
    'engagement stage decoration',
    'birthday stage decoration',
    'conference stage presentation',
    'auditorium stage presentation keynote',
    'mandap decoration flowers stage'
]

for q in queries:
    print(f"\n=== Query: {q} ===")
    search(q)
