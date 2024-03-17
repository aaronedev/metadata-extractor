import os
import json
import pyexifinfo as pex

def extract_metadata_with_exiftool(image_path):
    metadata = pex.get_json(image_path)
    return metadata

def save_metadata(metadata, output_path):
    with open(output_path, 'w') as f:
        json.dump(metadata, f, indent=4)

def main():
    images_dir = './images'
    metadata_dir = './metadata'
    os.makedirs(metadata_dir, exist_ok=True)

    for image_name in os.listdir(images_dir):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
            image_path = os.path.join(images_dir, image_name)
            metadata = extract_metadata_with_exiftool(image_path)
            output_filename = f'{os.path.splitext(image_name)[0]}.json'
            output_path = os.path.join(metadata_dir, output_filename)
            save_metadata(metadata, output_path)
            print(f'Metadata for {image_name} saved.')

if __name__ == "__main__":
    main()