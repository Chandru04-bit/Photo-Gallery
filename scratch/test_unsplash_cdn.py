import urllib.request
from PIL import Image
import io

test_url = "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

req = urllib.request.Request(test_url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = resp.read()
        img = Image.open(io.BytesIO(data))
        print("SUCCESS! Downloaded image:", img.size, img.format, len(data))
except Exception as e:
    print("FAILED:", e)
