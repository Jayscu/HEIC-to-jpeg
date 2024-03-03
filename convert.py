import gradio as gr
import imageio.v2 as imageio
import tempfile
from PIL import Image

# Function to convert HEIC to JPEG
def convert_heic_to_jpeg(heic_file):
    # Use imageio to read HEIC file
    heic_image = imageio.imread(heic_file)
    
    # Convert the image to PIL Image for further processing if necessary
    pil_image = Image.fromarray(heic_image)
    
    # Create a temporary file to save the JPEG
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpeg') as tmpfile:
        pil_image.save(tmpfile, format='JPEG')
        # Return the name of the temporary file instead of the BytesIO object
        return tmpfile.name

# Gradio interface using the updated API
iface = gr.Interface(fn=convert_heic_to_jpeg,
                     inputs=gr.File(label='Upload HEIC Image'),
                     outputs=gr.File(label='Download JPEG Image'),
                     title="HEIC to JPEG Converter",
                     description="Upload a HEIC image file to convert it to JPEG format. You can then download the converted JPEG.")

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
