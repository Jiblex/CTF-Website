from PIL import Image, ImageDraw, ImageFont

# Function to create the flag image
def gen_flag():
    flag_img = Image.new('RGB', (512, 512), color='white')  # White background for flag image
    draw = ImageDraw.Draw(flag_img)

    # Load a font
    font = ImageFont.load_default()  # Change to a suitable font if needed


    text = "CTF{B1T5_4dd3D}"
   
    draw.text((220, 252), text, fill='black', font=font)
    
    return flag_img


flag_image = gen_flag()
flag_image.save('flag.png')
