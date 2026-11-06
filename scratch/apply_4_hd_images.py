import os
import shutil
from PIL import Image

brain_dir = r"C:\Users\satha\.gemini\antigravity\brain\610f4546-fb3d-45e1-85e4-9224c2efedfe"
backup_dir = "scratch/backup_original_images"
os.makedirs(backup_dir, exist_ok=True)

tasks = [
    {
        "name": "wedding_stage_decoration",
        "source": os.path.join(brain_dir, "luxury_wedding_stage_hero_png_1793942085945.jpg"),
        "dest": "assets/images/gallery/wedding-stage/stage-1.jpg",
        "extra_dest": "assets/images/gallery/wedding-stage/wedding-stage-hd.jpg",
        "size": (1200, 900)
    },
    {
        "name": "colourful_celebration_confetti",
        "source": os.path.join(brain_dir, "celebration_confetti_teal_1793942086598.jpg"),
        "dest": "assets/images/gallery/birthday/birthday-2.jpg",
        "extra_dest": "assets/images/gallery/birthday/celebration-confetti-hd.jpg",
        "size": (1200, 900)
    },
    {
        "name": "corporate_event_stage",
        "source": os.path.join(brain_dir, "corporate_leadership_summit_stage_1793942254767.jpg"),
        "dest": "assets/images/gallery/corporate/corporate-1.jpg",
        "extra_dest": "assets/images/gallery/corporate/corporate-event-stage-hd.jpg",
        "size": (1200, 900)
    },
    {
        "name": "technology_conference_stage",
        "source": os.path.join(brain_dir, "tech_conference_stage_1793942264113.jpg"),
        "dest": "assets/images/gallery/corporate/corporate-2.jpg",
        "extra_dest": "assets/images/gallery/corporate/tech-conference-stage-hd.jpg",
        "size": (1200, 900)
    }
]

for t in tasks:
    src = t["source"]
    dest = t["dest"]
    extra = t.get("extra_dest")
    tw, th = t["size"]
    
    # Backup existing
    if os.path.exists(dest):
        pname = os.path.basename(os.path.dirname(dest))
        bname = os.path.basename(dest)
        bpath = os.path.join(backup_dir, f"{pname}_{bname}")
        shutil.copy2(dest, bpath)
        print(f"Backed up {dest} -> {bpath}")
        
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
        print(f"Saved {dest} ({tw}x{th})")
        
        if extra:
            img.save(extra, "JPEG", quality=92)
            print(f"Saved HD source {extra} ({sw}x{sh})")

print("All 4 HD images deployed to gallery successfully!")
