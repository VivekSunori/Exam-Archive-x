import os
import subprocess
from PIL import Image
import pytesseract

# Install required libraries
subprocess.run(["pip", "install", "pytesseract", "pillow"])

def crop_and_convert_to_text(input_folder, output_folder, start_y, end_y):
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Loop through all images in the input folder
        for image_file in os.listdir(input_folder):
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Build the full path to the image file
                image_path = os.path.join(input_folder, image_file)

                # Open the image file
                image = Image.open(image_path)

                # Crop the image based on the provided Y coordinates
                cropped_image = image.crop((0, start_y, image.width, end_y))

                # Use pytesseract to do OCR on the cropped image
                text = pytesseract.image_to_string(cropped_image)

                # Build the output text file path
                output_text_file = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}_cropped.txt")

                # Save the extracted text to the text file
                with open(output_text_file, 'w') as text_file:
                    text_file.write(text)

                print(f"Text saved for {image_file} (cropped).")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Provide the path to the input image folder, the output text folder,
    # and the Y coordinates for cropping
    input_folder = "D:\Exam-Archive-x\image2\images"
    output_folder = "D:\Exam-Archive-x\image2\output"
    start_y = 600  # Adjust as needed
    end_y = 1500    # Adjust as needed

    # Call the function to crop images, convert to text, and save in separate text files
    crop_and_convert_to_text(input_folder, output_folder, start_y, end_y)
