import urllib.request
import json
import urllib.parse
import time
from PIL import Image
import io
import os

headers = {'User-Agent': 'UTSAVWebsiteAuditor/1.2 (support@utsavdecor.com)'}

def fetch_commons_image(search_term, min_w=1200, min_h=700):
    time.sleep(1.2)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(search_term)}&gsrlimit=6&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, p in pages.items():
                if 'imageinfo' in p and p['imageinfo']:
                    info = p['imageinfo'][0]
                    mime = info.get('mime', '')
                    w = info.get('width', 0)
                    h = info.get('height', 0)
                    img_url = info.get('url', '')
                    if ('jpeg' in mime or 'jpg' in mime or 'png' in mime) and w >= min_w and h >= min_h:
                        return img_url, p.get('title'), w, h
    except Exception as e:
        print(f"Error searching '{search_term}': {e}")
    return None, None, 0, 0

def download_and_crop(img_url, dest_path, target_w=1200, target_h=675):
    req = urllib.request.Request(img_url, headers=headers)
    with urllib.request.urlopen(req, timeout=25) as resp:
        data = resp.read()
    
    img = Image.open(io.BytesIO(data))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Crop to aspect ratio target_w / target_h
    orig_w, orig_h = img.size
    target_aspect = target_w / target_h
    orig_aspect = orig_w / orig_h
    
    if orig_aspect > target_aspect:
        # Image is wider: crop sides
        new_w = int(orig_h * target_aspect)
        offset = (orig_w - new_w) // 2
        img = img.crop((offset, 0, offset + new_w, orig_h))
    else:
        # Image is taller: crop top/bottom
        new_h = int(orig_w / target_aspect)
        offset = (orig_h - new_h) // 2
        img = img.crop((0, offset, orig_w, offset + new_h))
    
    img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    img.save(dest_path, "JPEG", quality=90)
    print(f"Saved {dest_path} ({target_w}x{target_h}, {os.path.getsize(dest_path)/1024:.1f} KB)")

# Let's test with the birthday image first
url, title, w, h = fetch_commons_image("Birthday party decoration", 1200, 700)
print(f"Found Birthday: {title} ({w}x{h}) -> {url}")
if url:
    download_and_crop(url, "assets/images/services/birthday-decoration.jpg", 1200, 675)
