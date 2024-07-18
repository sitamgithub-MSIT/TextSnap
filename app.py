# Importing the requirements
import gradio as gr
from src.task import ocr_task


# Image input for the interface
image = gr.Image(type="pil", label="Image")

# Output for the interface (image and text)
ocr_text_output = gr.Textbox(label="OCR Text", show_label=True, show_copy_button=True)
ocr_image_output = gr.Image(type="pil", label="Output Image")

# Examples for the interface (image paths)
examples = [
    ["images/ocr_image_1.jpg"],
    ["images/ocr_image_2.jpg"],
    ["images/ocr_image_3.jpg"],
    ["images/ocr_image_4.png"],
]

# Title, description, and article for the interface
title = "OCR Text Extraction and Visualization"
description = "Gradio Demo for the Florence-2-large Vision Language Model. This application performs Optical Character Recognition (OCR) on images and provides both extracted text and visualized bounding boxes around detected text regions. To use it, simply upload your image and click 'Submit'. The application will return the detected text and an image with bounding boxes drawn around the detected text regions. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2311.06242' target='_blank'>Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks</a> | <a href='https://huggingface.co/microsoft/Florence-2-large-ft' target='_blank'>Model Page</a></p>"


# Launch the interface
interface = gr.Interface(
    fn=ocr_task,
    inputs=[image],
    outputs=[ocr_image_output, ocr_text_output],
    examples=examples,
    title=title,
    description=description,
    article=article,
    theme="soft",
    allow_flagging="never",
)
interface.launch(debug=False)
