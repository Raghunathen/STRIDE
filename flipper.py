import os
from PIL import Image
from tqdm import tqdm

def flip_images(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get a list of all files in the input folder
    for filename in tqdm(os.listdir(input_folder)):
        # Construct full file path
        file_path = os.path.join(input_folder, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            try:
                # Open the image
                img = Image.open(file_path)
                # Flip/mirror the image
                flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                # Save the flipped image to the output folder
                flipped_img.save(os.path.join(output_folder, filename))
                #print(f"Flipped and saved: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
        else:
            #print(f"Skipped non-image file: {filename}")
            pass

if __name__ == "__main__":
    input_folder = "ProperDataset/left"  # Change this to your source folder
    output_folder = "ProperDataset/left_to_right"  # Change this to your destination folder
    flip_images(input_folder, output_folder)
    input_folder = "ProperDataset/right"  # Change this to your source folder
    output_folder = "ProperDataset/right_to_left"  # Change this to your destination folder
    flip_images(input_folder, output_folder)
