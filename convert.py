import gradio as gr
import imageio.v2 as imageio  # Use imageio version 2 explicitly
from PIL import Image
import tempfile

# Updated function to include format selection
def convert_image(input_file, output_format):
    # Use imageio to read the input file
    input_image = imageio.imread(input_file)
    
    # Convert the image to PIL Image for further processing if necessary
    pil_image = Image.fromarray(input_image)
    
    # Create a temporary file to save the converted image
    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{output_format}') as tmpfile:
        pil_image.save(tmpfile, format=output_format.upper())
        # The function now returns the path to the temporary file
        return tmpfile.name

# Interface with format selection
iface = gr.Interface(
    fn=convert_image,
    inputs=[
        gr.File(label='Upload Image'),
        gr.Dropdown(label='Select Output Format', choices=['jpeg', 'png', 'bmp', 'tiff'], value='jpeg')
    ],
    outputs=gr.File(label='Download Converted Image'),
    title="Image Format Converter",
    description="Upload an image and select a format to convert it to. You can then download the converted image."
)

# Launch the Gradio app with public sharing
if __name__ == "__main__":
    iface.launch()
