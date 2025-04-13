# Necessary imports
import sys
import re
from PIL import Image
import supervision as sv

# Local imports
from src.logger import logging
from src.exception import CustomExceptionHandling


# Text cleaning function
def clean_text(text: str) -> str:
    """
    Cleans the given text by removing unwanted tokens, extra spaces,
    and ensures proper spacing between words and after punctuation marks.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned and properly formatted text.
    """
    try:
        # Remove unwanted tokens
        text = text.replace("<pad>", "").replace("</s>", "").strip()

        # Split the text into lines and clean each line
        lines = text.split("\n")
        cleaned_lines = [line.strip() for line in lines if line.strip()]

        # Join the cleaned lines into a single string with a space between each line
        cleaned_text = " ".join(cleaned_lines)

        # Ensure proper spacing using regex
        cleaned_text = re.sub(
            r"\s+", " ", cleaned_text
        )  # Replace multiple spaces with a single space
        cleaned_text = re.sub(
            r"(?<=[.,!?])(?=[^\s])", r" ", cleaned_text
        )  # Add space after punctuation if not followed by a space
        cleaned_text = re.sub(
            r"(?<=[a-z])(?=[A-Z])", r" ", cleaned_text
        )  # Add space between joined words where a lowercase letter is followed by an uppercase letter
        cleaned_text = re.sub(
            r"(\w)([A-Z][a-z])", r"\1 \2", cleaned_text
        )  # Add space between camel case words

        # Log the successful text cleaning
        logging.info("Text cleaned successfully.")

        # Return the cleaned text
        return cleaned_text

    # Handle exceptions that may occur during the process
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e


# Draw OCR bounding boxes with enhanced visual elements
def draw_ocr_bboxes(image: Image.Image, detections: sv.Detections) -> Image.Image:
    """
    Draws bounding boxes and labels on the input image based on the OCR detections.

    Args:
        - image (PIL.Image.Image): The input image on which to draw the bounding boxes and labels.
        - detections (sv.Detections): The OCR detections containing the bounding box coordinates and labels.

    Returns:
        PIL.Image.Image: The annotated image with bounding boxes and labels.
    """
    try:
        # Copy the input image to avoid modifying the original image
        annotated_image = image.copy()

        # Calculate the optimal line thickness and text scale based on the image resolution
        thickness = sv.calculate_optimal_line_thickness(resolution_wh=image.size)
        text_scale = sv.calculate_optimal_text_scale(resolution_wh=image.size)

        # Initialize the bounding box and label annotators
        bounding_box_annotator = sv.BoxAnnotator(
            color_lookup=sv.ColorLookup.INDEX, thickness=thickness
        )
        label_annotator = sv.LabelAnnotator(
            color_lookup=sv.ColorLookup.INDEX,
            text_scale=text_scale,
            text_thickness=thickness,
        )

        # Annotate the image with bounding boxes and labels
        annotated_image = bounding_box_annotator.annotate(annotated_image, detections)
        annotated_image = label_annotator.annotate(annotated_image, detections)

        # Log the successful annotation
        logging.info("Bounding boxes and labels drawn successfully.")

        # Return the annotated image
        return annotated_image

    # Handle exceptions that may occur during the process
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
