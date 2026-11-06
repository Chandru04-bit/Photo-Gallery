import urllib.request
import json
import urllib.parse
from PIL import Image
import os
import io

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) UTSAVDecor/1.0'}

targets = {
    "services/birthday-decoration.jpg": {
        "query": "birthday decoration party balloons stage",
        "crop": (1200, 675)
    },
    "services/corporate-events.jpg": {
        "query": "conference stage presentation auditorium",
        "crop": (1200, 675)
    },
    "services/entrance-arch.jpg": {
        "query": "wedding entrance floral arch",
        "crop": (1200, 675)
    },
    "services/exhibition-stall.jpg": {
        "query": "trade show exhibition booth pavilion",
        "crop": (1200, 675)
    },
    "services/lighting-stage.jpg": {
        "query": "stage lighting concert spotlights truss",
        "crop": (1200, 675)
    },
    "services/religious-cultural.jpg": {
        "query": "puja mandap temple ceremony flowers",
        "crop": (1200, 675)
    },
    "blog/blog-1.jpg": {
        "query": "Hindu wedding mandap stage",
        "crop": (1200, 675)
    },
    "blog/blog-2.jpg": {
        "query": "traditional marriage pandal tent India",
        "crop": (1200, 675)
    },
    "blog/blog-3.jpg": {
        "query": "outdoor marquee wedding tent evening",
        "crop": (1200, 675)
    },
    "blog/blog-4.jpg": {
        "query": "wedding floral arrangement flower wall roses",
        "crop": (1200, 675)
    },
    "blog/blog-5.jpg": {
        "query": "stage lighting moving heads beams concert",
        "crop": (1200, 675)
    },
    "blog/blog-6.jpg": {
        "query": "event production banquet hall setup wedding",
        "crop": (1200, 675)
    },
    "about/about-story.jpg": {
        "query": "florist arranging flowers wedding decoration",
        "crop": (1200, 800)
    },
    "gallery/wedding-stage/stage-2.jpg": {
        "query": "wedding stage floral decoration India",
        "crop": (1200, 900)
    },
    "gallery/wedding-stage/stage-3.jpg": {
        "query": "mandap flowers ceremony gold wedding",
        "crop": (1200, 900)
    },
    "gallery/engagement/engagement-2.jpg": {
        "query": "engagement stage decoration flowers",
        "crop": (1200, 900)
    },
    "gallery/reception/reception-2.jpg": {
        "query": "luxury wedding reception stage chandelier",
        "crop": (1200, 900)
    },
    "gallery/reception/reception-3.jpg": {
        "query": "wedding banquet stage lighting hall",
        "crop": (1200, 900)
    },
    "gallery/traditional-pandal/pandal-2.jpg": {
        "query": "pandal decoration festival canopy fabric",
        "crop": (1200, 900)
    },
    "gallery/traditional-pandal/pandal-3.jpg": {
        "query": "Durga puja pandal interior decoration",
        "crop": (1200, 900)
    },
    "gallery/outdoor-events/outdoor-2.jpg": {
        "query": "marquee tent event structure canopy",
        "crop": (1200, 900)
    }
}

def search_image(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(query)}&gsrlimit=6&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            candidates = []
            for pid, p in pages.items():
                if 'imageinfo' in p and p['imageinfo']:
                    info = p['imageinfo'][0]
                    mime = info.get('mime', '')
                    w = info.get('width', 0)
                    h = info.get('height', 0)
                    if ('jpeg' in mime or 'jpg' in mime or 'png' in mime) and w >= 800 and h >= 500:
                        candidates.append((w * h, info.get('url'), p.get('title'), w, h))
            candidates.sort(reverse=True)
            return candidates
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

print(f"Searching images for {len(targets)} targets...")
for rel_path, cfg in targets.items():
    candidates = search_image(cfg["query"])
    print(f"\nTarget: {rel_path} (Query: '{cfg['query']}')")
    if candidates:
        for score, img_url, title, w, h in candidates[:2]:
            clean_title = title.encode('ascii', 'ignore').decode('ascii')
            print(f"   Found: {clean_title} ({w}x{h})")
    else:
        print("   NO SUITABLE CANDIDATES FOUND")
