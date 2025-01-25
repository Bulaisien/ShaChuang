from PIL import Image, ImageDraw, ImageFont
import random

# Define text and font
text = "你好世界"  # Text to display
font_path = "simsun.ttc"  # Font path
font_size = 80
font = ImageFont.truetype(font_path, font_size)

# Create a temporary image to calculate text size
dummy_img = Image.new("RGB", (1, 1), (255, 255, 255))
draw = ImageDraw.Draw(dummy_img)

# Measure a single character size (assuming equal width for simplicity)
char_widths = [draw.textbbox((0, 0), char, font=font)[2] for char in text]
char_height = draw.textbbox((0, 0), text[0], font=font)[3]

# Padding & box settings
padding = 10  # Space around text inside boxes
spacing = 0   # No space between the boxes (to make the vertical edges join)
border_thickness = 5  # Thickness of the box edges

# Calculate total image size
box_widths = [w + 2 * padding for w in char_widths]
box_height = char_height + 2 * padding
img_width = sum(box_widths) + (len(text) - 1) * (spacing - border_thickness)
img_height = box_height

# Create final image
img = Image.new("RGB", (img_width, img_height), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Function to generate a single non-black, non-white color for all boxes
def random_color():
    return (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))

box_color = random_color()  # Set a single box color for all characters

# Draw each character inside its bordered box
x_offset = 0
for i, char in enumerate(text):
    char_width = char_widths[i]
    box_width = box_widths[i]

    # Calculate box coordinates
    box_coords = [x_offset, 0, x_offset + box_width, box_height]

    # Draw the box edges (outline) — avoid double borders between boxes
    draw.rectangle(box_coords, outline=box_color, width=border_thickness)

    # Calculate text position inside the box (centered)
    text_x = x_offset + (box_width - char_width) // 2
    text_y = (box_height - char_height) // 2

    # Draw the text
    draw.text((text_x, text_y), char, font=font, fill=(0, 0, 0))  # Black text

    # Move to the next character position, considering the border thickness
    x_offset += box_width - border_thickness  # No spacing between boxes now

# Save and show the image
img.save("merged_borders_text_image_v2.png")
img.show()
