import os
import shutil
from PIL import Image

brain_dir = r"C:\Users\satha\.gemini\antigravity\brain\610f4546-fb3d-45e1-85e4-9224c2efedfe"
backup_dir = "scratch/backup_original_images"
os.makedirs(backup_dir, exist_ok=True)

mappings = [
    {
        "source": os.path.join(brain_dir, "royal_mandap_stage_1793941132593.jpg"),
        "dest": "assets/images/gallery/wedding-stage/stage-2.jpg",
        "target_size": (1200, 900)
    },
    {
        "source": os.path.join(brain_dir, "test_pandal_1793941034742.jpg"),
        "dest": "assets/images/gallery/traditional-pandal/pandal-2.jpg",
        "target_size": (1200, 900)
    },
    {
        "source": os.path.join(brain_dir, "grand_wedding_reception_stage_1793941137339.jpg"),
        "dest": "assets/images/gallery/reception/reception-2.jpg",
        "target_size": (1200, 900)
    },
    {
        "source": os.path.join(brain_dir, "indian_engagement_floral_stage_1793941114316.jpg"),
        "dest": "assets/images/gallery/engagement/engagement-2.jpg",
        "target_size": (1200, 900)
    },
    {
        "source": os.path.join(brain_dir, "enchanted_garden_birthday_stage_1793941121693.jpg"),
        "dest": "assets/images/gallery/birthday/birthday-1.jpg",
        "target_size": (1200, 900)
    },
    {
        "source": os.path.join(brain_dir, "corporate_summit_stage_rig_1793941128269.jpg"),
        "dest": "assets/images/gallery/corporate/corporate-2.jpg",
        "target_size": (1200, 900)
    }
]

for item in mappings:
    src = item["source"]
    dest = item["dest"]
    tw, th = item["target_size"]
    
    # 1. Backup if exists
    if os.path.exists(dest):
        bname = os.path.basename(dest)
        pname = os.path.basename(os.path.dirname(dest))
        bfile = os.path.join(backup_dir, f"{pname}_{bname}")
        shutil.copy2(dest, bfile)
        print(f"Backed up {dest} -> {bfile}")
    
    # 2. Open and crop to target aspect ratio (center crop)
    with Image.open(src) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        sw, sh = img.size
        target_aspect = tw / th
        src_aspect = sw / sh
        
        if src_aspect > target_aspect:
            crop_w = int(sh * target_aspect)
            offset = (sw - crop_w) // 2
            img_cropped = img.crop((offset, 0, offset + crop_w, sh))
        else:
            crop_h = int(sw / target_aspect)
            offset = (sh - crop_h) // 2
            img_cropped = img.crop((0, offset, sw, offset + crop_h))
            
        img_resized = img_cropped.resize((tw, th), Image.Resampling.LANCZOS)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        img_resized.save(dest, "JPEG", quality=92)
        print(f"Updated {dest}: ({tw}x{th}) from {os.path.basename(src)}")

print("\nAll 6 images successfully applied!")
