from PIL import Image
import os
import json

def extract_metadata(image_path):
    with Image.open(image_path) as img:
        metadata = {
            "filename": os.path.basename(image_path),
            "size": img.size,
            "format": img.format,
            "mode": img.mode,
        }
        return metadata

def save_metadata(metadata, output_path):
    with open(output_path, 'w') as f:
        json.dump(metadata, f, indent=4)

def main():
    images_dir = './images'
    metadata_dir = './metadata'
    os.makedirs(metadata_dir, exist_ok=True)

    for image_name in os.listdir(images_dir):
        image_path = os.path.join(images_dir, image_name)
        metadata = extract_metadata(image_path)
        output_path = os.path.join(metadata_dir, f'{metadata["filename"]}.json')
        save_metadata(metadata, output_path)
        print(f'Metadata for {image_name} saved.')

if __name__ == "__main__":
    main()
