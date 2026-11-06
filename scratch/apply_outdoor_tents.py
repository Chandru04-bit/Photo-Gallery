import os
import shutil
from PIL import Image

brain_dir = r"C:\Users\satha\.gemini\antigravity\brain\610f4546-fb3d-45e1-85e4-9224c2efedfe"
b0_dir = r"C:\Users\satha\.gemini\antigravity\brain\b0bc2b41-3e44-464a-93e2-9cfc3588fe48"
backup_dir = "scratch/backup_original_images"
os.makedirs(backup_dir, exist_ok=True)

# 1. Clear-span tent source
clear_span_src = os.path.join(b0_dir, "outdoor_events_1793874671467.jpg")
clear_span_brain_copy = os.path.join(brain_dir, "clear_span_wedding_arena_tent.jpg")
shutil.copy2(clear_span_src, clear_span_brain_copy)
print("Copied clear-span tent to brain dir:", clear_span_brain_copy)

# 2. German AC tent source
german_ac_src = os.path.join(brain_dir, "german_marquee_luxury_tent_1793942745712.jpg")

items = [
    {
        "source": german_ac_src,
        "dest": "assets/images/gallery/outdoor-events/outdoor-2.jpg",
        "size": (1200, 900),
        "title": "Air-Conditioned German Canopy"
    },
    {
        "source": clear_span_brain_copy,
        "dest": "assets/images/gallery/outdoor-events/outdoor-3.jpg",
        "size": (1200, 900),
        "title": "Clear-Span Wedding Arena Tent"
    }
]

for it in items:
    src = it["source"]
    dest = it["dest"]
    tw, th = it["size"]
    
    # Backup existing
    if os.path.exists(dest):
        pname = os.path.basename(os.path.dirname(dest))
        bname = os.path.basename(dest)
        bfile = os.path.join(backup_dir, f"{pname}_{bname}")
        shutil.copy2(dest, bfile)
        print(f"Backed up {dest} -> {bfile}")
        
    with Image.open(src) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        sw, sh = img.size
        target_aspect = tw / th
        src_aspect = sw / sh
        
        if src_aspect > target_aspect:
            crop_w = int(sh * target_aspect)
            offset = (sw - crop_w) // 2
            cropped = img.crop((offset, 0, offset + crop_w, sh))
        else:
            crop_h = int(sw / target_aspect)
            offset = (sh - crop_h) // 2
            cropped = img.crop((0, offset, sw, offset + crop_h))
            
        resized = cropped.resize((tw, th), Image.Resampling.LANCZOS)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        resized.save(dest, "JPEG", quality=92)
        print(f"Saved {it['title']} -> {dest} ({tw}x{th})")

print("Both outdoor tent gallery cards successfully updated!")
