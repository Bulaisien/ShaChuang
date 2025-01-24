from PIL import Image, ImageDraw, ImageFont

# Define text and font
text = "你好世界"  # Change this to any text
font_path = "simsun.ttc"  # Use a Chinese-supporting font (update path if needed)
font_size = 80
font = ImageFont.truetype(font_path, font_size)

# Create a temporary image to calculate text size
dummy_img = Image.new("RGB", (1, 1), (255, 255, 255))
draw = ImageDraw.Draw(dummy_img)

# Calculate text size
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Add some padding around the text
padding = 20
img_width = text_width + 2 * padding
img_height = text_height + 2 * padding

# Create the final image with correct dimensions
img = Image.new("RGB", (img_width, img_height), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Calculate centered position
text_x = (img_width - text_width) // 2
text_y = (img_height - text_height) // 2

# Draw the text
text_color = (0, 0, 0)  # Black text
draw.text((text_x, text_y), text, font=font, fill=text_color)

# Save and show the image
img.save("adjusted_text_image.png")
img.show()
