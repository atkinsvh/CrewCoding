import base64
from IPython.display import display, HTML

def display_images(image_paths):
    """
    Display images given their file paths.
    
    :param image_paths: List of file paths to the images
    """
    image_html = ""
    for path in image_paths:
        with open(path, "rb") as file:
            image_data = file.read()
            image_base64 = base64.b64encode(image_data).decode("utf-8")
            image_html += f'<img src="data:image/jpeg;base64,{image_base64}" /><br>'
    
    display(HTML(image_html))

# List of file paths to the images
image_paths = ["selfcare.jpg", "bluehairtori.jpg", "julytori.jpg"]

# Display the images
display_images(image_paths)
