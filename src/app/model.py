# Importing necessary libraries
import sys
import subprocess
from typing import Optional
from PIL import Image
import gradio as gr
import spaces
from transformers import AutoProcessor, AutoModelForCausalLM

# Local imports
from src.logger import logging
from src.exception import CustomExceptionHandling


# Install the required dependencies
subprocess.run(
    "pip install flash-attn --no-build-isolation",
    env={"FLASH_ATTENTION_SKIP_CUDA_BUILD": "TRUE"},
    shell=True,
)

# Load model and processor from Hugging Face
model_id = "microsoft/Florence-2-large-ft"
try:
    model = (
        AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
        .to("cuda")
        .eval()
    )
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
    logging.info("Model and processor loaded successfully.")

# Handle exceptions that may occur during the process
except Exception as e:
    # Custom exception handling
    raise CustomExceptionHandling(e, sys) from e


@spaces.GPU
def run_example(
    task_prompt: str, image: Image.Image, text_input: Optional[str] = None
) -> str:
    """
    Runs an example using the given task prompt and image.

    Args:
        - task_prompt (str): The task prompt for the example.
        - image (PIL.Image.Image): The image to be processed.
        - text_input (str, optional): Additional text input to be appended to the task prompt. Defaults to None.
        
    Returns:
        str: The parsed answer generated by the model.
    """
    try:
        # Check if image is None
        if image is None:
            gr.Warning("Please provide an image.")

        # If there is no text input, use the task prompt as the prompt
        prompt = task_prompt if text_input is None else task_prompt + text_input

        # Process the image and text input
        inputs = processor(text=prompt, images=image, return_tensors="pt").to("cuda")

        # Generate the answer using the model
        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=1024,
            early_stopping=False,
            do_sample=False,
            num_beams=3,
        )
        generated_text = processor.batch_decode(
            generated_ids, skip_special_tokens=False
        )[0]
        parsed_answer = processor.post_process_generation(
            generated_text, task=task_prompt, image_size=(image.width, image.height)
        )

        # Return the parsed answer
        return parsed_answer

    # Handle exceptions that may occur during the process
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
