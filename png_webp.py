import os
from PIL import Image

def batch_convert_png_to_webp(png_paths, quality=80):
    # Create output folder if it doesn't exist
    output_folder = "out_webp"
    os.makedirs(output_folder, exist_ok=True)
    
    for png_path in png_paths:
        # Extract the image filename and create WebP output path
        image_name = os.path.splitext(os.path.basename(png_path))[0]
        webp_path = os.path.join(output_folder, f"{image_name}.webp")
        
        # Open, convert, and save the image as WebP
        with Image.open(png_path) as img:
            img.save(webp_path, "webp", quality=quality)

png_paths = [""]
batch_convert_png_to_webp(png_paths, quality=80)
