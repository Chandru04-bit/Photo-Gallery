import urllib.request
import json
import urllib.parse
import time

headers = {'User-Agent': 'UTSAVWebsiteAuditor/1.2 (support@utsavdecor.com)'}

def search_term(q, min_w=1200, min_h=700):
    time.sleep(1.1)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(q)}&gsrlimit=6&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            results = []
            for pid, p in pages.items():
                if 'imageinfo' in p and p['imageinfo']:
                    info = p['imageinfo'][0]
                    mime = info.get('mime', '')
                    w = info.get('width', 0)
                    h = info.get('height', 0)
                    if ('jpeg' in mime or 'jpg' in mime or 'png' in mime) and w >= min_w and h >= min_h:
                        t = p.get('title', '').encode('ascii', 'ignore').decode('ascii')
                        results.append((w * h, t, w, h, info.get('url')))
            results.sort(reverse=True)
            return results
    except Exception as e:
        print(f"Error {q}: {e}")
        return []

r = search_term("wedding stage decorations")
for item in r:
    print(item[1], item[2], item[3], item[4])
