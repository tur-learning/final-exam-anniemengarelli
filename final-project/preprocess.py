from gradio_client import Client, handle_file
import os, shutil
from pathlib import Path
from utils import convert_png_to_jpg

def preprocess(root_directory, preprocess_model, output_folder):
    root = root_directory
    images_path = os.listdir(root)

    print(f"Using Model: {preprocess_model}")
    
    # Visit this page to view the possible models that can be used:
    # # https://huggingface.co/spaces/KenjieDec/RemBG
    client = Client("KenjieDec/RemBG")
    preprocessed_dir = Path(output_folder).resolve()
    # Initially removes dir
    shutil.rmtree(preprocessed_dir, ignore_errors = True)
    Path.mkdir(preprocessed_dir)
    

    for image in images_path:
        result = client.predict(
            file=handle_file(os.path.join(root, image)),
            mask="Default",
            model = preprocess_model,
            x=3,
            y=3,
            api_name="/inference"
        )
        result = Path(result)
        print(result)
        print(f"Copying preprocessed image to {output_folder} directory")
        shutil.copyfile(result, os.path.join(output_folder, result.parent.name+result.suffix))
    # Images are converted to jpg for integration with dust3r model
    convert_png_to_jpg(preprocessed_dir)
    print("success!")
    return preprocessed_dir