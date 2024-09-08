from PIL import Image
import random

def randomize_pixels_pattern(image_path, output_path):
    # Open the input image
    img = Image.open(image_path)
    
    # Convert the image to black and white
    bw_img = img.convert('1')
    
    # Get the dimensions of the image
    width, height = bw_img.size
    
    # Create a new image with the same size as the original
    randomized_img = Image.new('1', (width, height))
    
    # Define the pattern size (e.g., 10x10 pixels)
    pattern_size = 1
    
    # Iterate over each pattern in the image and assign random pixel values
    for x in range(0, width, pattern_size):
        for y in range(0, height, pattern_size):
            # Generate a random pixel value for each pattern
            pixel_value = random.choice([0, 255])
            
            # Fill the pattern with the random pixel value
            for i in range(pattern_size):
                for j in range(pattern_size):
                    # Make sure not to exceed image boundaries
                    if x + i < width and y + j < height:
                        randomized_img.putpixel((x + i, y + j), pixel_value)
    
    # Save the randomized image
    randomized_img.save(output_path)

randomize_pixels_pattern("flag.png", "key.png")
