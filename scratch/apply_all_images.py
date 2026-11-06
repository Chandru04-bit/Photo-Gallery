import urllib.request
import os
import io
import time
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) UTSAVWebsiteAuditor/1.2 (support@utsavdecor.com)'}

items = [
    # Services
    {
        "path": "assets/images/services/corporate-events.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/27/Gustavo-Borges-main-stage-speaker-2026.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/services/entrance-arch.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Floral_decor.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/services/exhibition-stall.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Sega_booth%2C_Taipei_Game_Show_20190127a.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/services/lighting-stage.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/58/Inauguracja_Sosnowieckiego_Dziedzi%C5%84ca_Sztuki.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/services/religious-cultural.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Devotion_and_Divinity_-_A_Moment_of_Prayer.jpg",
        "size": (1200, 675)
    },
    # Blog Thumbnails
    {
        "path": "assets/images/blog/blog-1.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Indian_Wedding_Mandap_Decoration.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/blog/blog-2.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/88/Chalta_Bagan_Durga_Puja_2019.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/blog/blog-3.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Tendoni_del_palco.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/blog/blog-4.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Photo_of_a_flower_arrangement_we_received_on_our_60th_wedding_anniversary.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/blog/blog-5.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7c/IJahman_Levi%2C_Red_Stage%2C_Ostr%C3%B3da_Reggae_Festiwal%2C_2025%2C_SOULinPIX%2C_KsP_354.jpg",
        "size": (1200, 675)
    },
    {
        "path": "assets/images/blog/blog-6.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/55/Elegant_banquet_setup_for_wedding_reception_with_beautifully_arranged_tables_in_soft_lighting.jpg",
        "size": (1200, 675)
    },
    # About Story
    {
        "path": "assets/images/about/about-story.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Flowers_ready_to_be_prepared_by_florist.jpg",
        "size": (1200, 800)
    },
    # Gallery Unique Images
    {
        "path": "assets/images/gallery/wedding-stage/stage-2.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/64/Wedding_stage_decoration_in_thrissur_kerala.jpg",
        "size": (1200, 900)
    },
    {
        "path": "assets/images/gallery/wedding-stage/stage-3.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Wedding_Mandap_with_Tikri_Art.jpg",
        "size": (1200, 900)
    },
    {
        "path": "assets/images/gallery/engagement/engagement-2.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Indian_engagement_ceremony_07.jpg",
        "size": (1200, 900)
    },
    {
        "path": "assets/images/gallery/reception/reception-2.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Wedding_reception_stage%2C_decorations%2C_Kochi.jpg",
        "size": (1200, 900)
    },
    {
        "path": "assets/images/gallery/reception/reception-3.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Indoor_wedding_stage_decoration_in_Kerala.jpg",
        "size": (1200, 900)
    },
    {
        "path": "assets/images/gallery/traditional-pandal/pandal-2.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Navratri_Pandal_with_Festive_Decorations_03.jpg",
        "size": (1200, 900)
    },
    {
        "path": "assets/images/gallery/traditional-pandal/pandal-3.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/06/Kolkata_Durga_Puja_Pandal_Interior.jpg",
        "size": (1200, 900)
    },
    {
        "path": "assets/images/gallery/outdoor-events/outdoor-2.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Event_Tent.JPG",
        "size": (1200, 900)
    }
]

def process_item(item):
    dest_path = item["path"]
    img_url = item["url"]
    target_w, target_h = item["size"]
    
    print(f"\nProcessing {dest_path}...")
    try:
        time.sleep(1.2)  # courteous delay between requests
        req = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        
        img = Image.open(io.BytesIO(data))
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        orig_w, orig_h = img.size
        target_aspect = target_w / target_h
        orig_aspect = orig_w / orig_h
        
        if orig_aspect > target_aspect:
            new_w = int(orig_h * target_aspect)
            offset = (orig_w - new_w) // 2
            img = img.crop((offset, 0, offset + new_w, orig_h))
        else:
            new_h = int(orig_w / target_aspect)
            offset = (orig_h - new_h) // 2
            img = img.crop((0, offset, orig_w, offset + new_h))
        
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        img.save(dest_path, "JPEG", quality=90)
        size_kb = os.path.getsize(dest_path) / 1024
        print(f"  SUCCESS: {dest_path} ({target_w}x{target_h}, {size_kb:.1f} KB)")
        return True
    except Exception as e:
        print(f"  FAILED {dest_path}: {e}")
        return False

success_count = 0
for it in items:
    if process_item(it):
        success_count += 1

print(f"\nCompleted {success_count} / {len(items)} image downloads and replacements.")
