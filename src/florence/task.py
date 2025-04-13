# Import necessary libraries
import sys
import copy
from typing import Tuple
from PIL import Image
import supervision as sv

# Local imports
from src.utils.processing import clean_text, draw_ocr_bboxes
from src.florence.model import run_example
from src.logger import logging
from src.exception import CustomExceptionHandling


def ocr_task(image: Image.Image) -> Tuple[Image.Image, str]:
    """
    Perform OCR (Optical Character Recognition) on the given image.

    Args:
        image (PIL.Image.Image): The input image to perform OCR on.

    Returns:
        tuple: A tuple containing the output image with OCR bounding boxes drawn and the cleaned OCR text.
    """
    try:
        # Task prompts
        ocr_prompt = "<OCR>"
        ocr_with_region_prompt = "<OCR_WITH_REGION>"

        # Get OCR text
        ocr_results = run_example(ocr_prompt, image)
        cleaned_text = clean_text(ocr_results["<OCR>"])

        # Log the successful extraction and cleaning of OCR text
        logging.info("OCR text extracted and cleaned successfully.")

        # Get OCR with region
        ocr_with_region_results = run_example(ocr_with_region_prompt, image)
        output_image = copy.deepcopy(image)
        detections = sv.Detections.from_lmm(
            lmm=sv.LMM.FLORENCE_2,
            result=ocr_with_region_results,
            resolution_wh=image.size,
        )
        output_image = draw_ocr_bboxes(image, detections)

        # Log the successful drawing of OCR bounding boxes
        logging.info("OCR bounding boxes drawn successfully.")

        # Return the output image and cleaned OCR text
        return output_image, cleaned_text

    # Handle exceptions that may occur during the process
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
