# Import necessary libraries
import copy
import supervision as sv
from src.utils import clean_text, draw_ocr_bboxes
from src.model import run_example


def ocr_task(image):
    """
    Perform OCR (Optical Character Recognition) on the given image.
    Args:
        image (PIL.Image.Image): The input image to perform OCR on.
    Returns:
        tuple: A tuple containing the output image with OCR bounding boxes drawn and the cleaned OCR text.
    """

    # Task prompts
    ocr_prompt = "<OCR>"
    ocr_with_region_prompt = "<OCR_WITH_REGION>"

    # Get OCR text
    ocr_results = run_example(ocr_prompt, image)
    cleaned_text = clean_text(ocr_results["<OCR>"])

    # Get OCR with region
    ocr_with_region_results = run_example(ocr_with_region_prompt, image)
    output_image = copy.deepcopy(image)
    detections = sv.Detections.from_lmm(
        lmm=sv.LMM.FLORENCE_2, result=ocr_with_region_results, resolution_wh=image.size
    )
    output_image = draw_ocr_bboxes(image, detections)

    # Return the output image and cleaned OCR text
    return output_image, cleaned_text
