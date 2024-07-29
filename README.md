# TextSnap

[Florence-2](https://huggingface.co/microsoft/Florence-2-large-ft) is an advanced vision foundation model developed by Microsoft, designed to handle a wide range of vision and vision-language tasks using a prompt-based approach. This model can interpret simple text prompts to perform functions like captioning, object detection, and segmentation. Its sequence-to-sequence architecture enables outstanding performance in zero-shot and fine-tuned settings, making it a highly competitive vision foundation model. This project utilizes [Florence-2](https://huggingface.co/microsoft/Florence-2-large-ft) to demonstrate robust OCR (Optical Character Recognition) capabilities, offering both text extraction and enhanced visualization of recognized text regions in images.

## Project Structure

The project is structured as follows:

- `src\`: The source code directory containing the project's main files.

  - `model.py`: The file that contains the Florence-2 vision foundation model for generating responses.
  - `task.py`: The file that contains the code for adapting the model to the OCR task.
  - `utils.py`: The file containing the project's utility functions.

- `app.py`: The main file that contains the Gradio application for the OCR task.
- `requirements.txt`: The file that contains the required dependencies for the project.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `assets`: The folder that contains the screenshots for working on the application.
- `images`: The folder that contains the images for testing the application.

## Tech Stack

- Python (for the programming language)
- Hugging Face Transformers Library (for the vision large language model)
- Gradio (for the web application)
- Hugging Face Spaces (for hosting the gradio application)

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/TextSnap.git`
2. Change the directory: `cd TextSnap`
3. Create a virtual environment: `python -m venv tutorial-env`
4. Activate the virtual environment: `tutorial-env\Scripts\activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the Gradio application: `python app.py`

Now, open up your local host and you should see the web application running. If you would like more information, please refer to the Gradio documentation [here](https://www.gradio.app/docs/interface). Also, a live version of the application can be found [here](https://huggingface.co/spaces/sitammeur/TextSnap).

## Usage

The web application allows you to upload an image, and the OCR models will extract text from it, providing two main functionalities: text extraction and text visualization. Text extraction cleans and formats the extracted text, ensuring proper spacing between words and after punctuation marks. Text visualization draws bounding boxes around recognized text regions on the image, offering a clear and enhanced visual representation. This application can assist in document digitization, automated data entry, and improved accessibility for visually impaired individuals by recognizing text from images.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you want to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
