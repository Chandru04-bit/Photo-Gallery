import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

def get_unsplash_photos(slug):
    url = f"https://unsplash.com/s/photos/{slug}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Look for photo IDs: images.unsplash.com/photo-([0-9a-zA-Z_-]+)
            matches = re.findall(r'images\.unsplash\.com/photo-([0-9a-zA-Z_-]+)', html)
            # Remove query params or trailing tokens
            clean_ids = []
            seen = set()
            for m in matches:
                # photo id is typically digits-alphanumeric, e.g. 1519741497674-611481863552
                pid = m.split('?')[0]
                if pid not in seen and len(pid) > 8:
                    seen.add(pid)
                    clean_ids.append(pid)
            return clean_ids
    except Exception as e:
        print(f"Error fetching {slug}: {e}")
        return []

pids = get_unsplash_photos("conference-stage")
print(f"conference-stage found {len(pids)} photo IDs:")
for pid in pids[:5]:
    print("  photo-" + pid)
