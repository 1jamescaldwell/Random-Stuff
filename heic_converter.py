from PIL import Image
import pillow_heif
import os

# Define a function to convert HEIC to PNG and show progress
def convert_heic_to_png(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of all .heic files
    heic_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.heic')]
    total_files = len(heic_files)

    # Loop through and convert files, showing progress
    for i, filename in enumerate(heic_files):
        heic_file = os.path.join(input_folder, filename)
        png_filename = os.path.splitext(filename)[0] + '.png'
        png_file = os.path.join(output_folder, png_filename)

        try:
            # Open HEIC file
            heif_image = pillow_heif.open_heif(heic_file)
            image = Image.frombytes(
                heif_image.mode,
                heif_image.size,
                heif_image.data,
                "raw",
                heif_image.mode,
                0,
                1
            )

            # Save image as PNG
            image.save(png_file, 'PNG')

        except ValueError as e:
            print(f"Error converting {heic_file}: {e}. Skipping...")

        # Calculate and display progress percentage
        percent_complete = ((i + 1) / total_files) * 100
        print(f"{percent_complete:.2f}% complete", end='\r')

# Paths to your folders
input_folder = r''  # Change this to your .heic folder path
output_folder = r''  # Change this to your output folder

# Convert all .heic files in the input folder to .png
convert_heic_to_png(input_folder, output_folder)
