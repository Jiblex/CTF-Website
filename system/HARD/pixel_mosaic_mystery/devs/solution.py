import cv2 

def bitwise_images(img1_path, img2_path, output_path):
    # Read the key and flag images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Resize to make images match in size
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Subtract/Add the images pixel-wise
    bit_img = cv2.subtract(img2_resized, img1)

    # Save the image
    cv2.imwrite(output_path, bit_img)

bitwise_images('flag.png', 'partial_flag.png', 'sols.png')
