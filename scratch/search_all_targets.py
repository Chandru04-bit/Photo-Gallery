import urllib.request
import json
import urllib.parse
import time

headers = {'User-Agent': 'UTSAVWebsiteAuditor/1.2 (support@utsavdecor.com)'}

def search_term(q, min_w=1200, min_h=700):
    time.sleep(1.1)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(q)}&gsrlimit=5&prop=imageinfo&iiprop=url|size|mime&format=json"
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

tasks = {
    "corporate-events": ["keynote stage presentation", "conference presentation hall stage", "auditorium stage lecture"],
    "entrance-arch": ["wedding arch flowers", "floral archway wedding entrance", "wedding floral arch"],
    "exhibition-stall": ["trade show booth", "exhibition booth fair", "convention center stalls"],
    "lighting-stage": ["concert lighting truss stage", "theatre stage lighting fixtures", "stage spotlights illumination"],
    "religious-cultural": ["puja mandap decoration", "temple festival mandap", "Ganesh festival mandap decoration"],
    "blog-1 (wedding stage ideas)": ["Indian wedding mandap decoration", "wedding mandap ceremony", "wedding stage decoration India"],
    "blog-2 (traditional pandal)": ["Durga puja pandal", "pandal festival decoration", "traditional pandal canopy"],
    "blog-3 (outdoor marquee tent)": ["marquee tent wedding", "event tent lawn", "outdoor wedding marquee canopy"],
    "blog-4 (floral decor)": ["wedding flowers arrangement", "flower wall wedding decor", "floral centerpiece roses wedding"],
    "blog-5 (stage lighting)": ["stage moving lights concert", "stage beam lighting", "concert truss illumination"],
    "blog-6 (infrastructure checklist)": ["banquet hall wedding setup", "event venue setup chairs tables", "conference hall setup"],
    "about-story (craftsmanship)": ["florist arranging flowers", "craftsmen decorating wedding", "flower garland making India"],
    "gallery-stage-2": ["mandap decoration flowers", "wedding stage backdrop flowers"],
    "gallery-stage-3": ["Wedding Mandap with Tikri Art", "carved mandap pillars wedding"],
    "gallery-pandal-2": ["pandal canopy decoration", "festival pandal interior"],
    "gallery-pandal-3": ["pandal festival lighting", "Durga Puja pandal interior"],
    "gallery-outdoor-2": ["clear-span tent event", "marquee canopy wedding evening"]
}

for name, queries in tasks.items():
    print(f"\nTarget: {name}")
    found = False
    for q in queries:
        res = search_term(q)
        if res:
            top = res[0]
            print(f"  [Query: '{q}'] => {top[1]} ({top[2]}x{top[3]})")
            print(f"     URL: {top[4]}")
            found = True
            break
    if not found:
        print(f"  NO MATCH FOR: {name}")
