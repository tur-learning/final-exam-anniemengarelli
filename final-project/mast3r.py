import os
import requests
from gradio_client import Client, handle_file
import shutil
from pathlib import Path

# Step 1: setup directory where images are stored 
def mast3r_function(input, config):
    image_dir = input
    local_paths = os.listdir(image_dir)
    local_paths = [Path.cwd()/image_dir/file for file in local_paths]

    # Step 2: Convert local files to gradio-compatible uploads
    filelist = [handle_file(path) for path in local_paths]
    print(filelist)

    # Step 3: Use gradio_client to call the endpoint
    HF_TOKEN = "*************************"

    if HF_TOKEN is None:
        raise ValueError("ERROR: YOU MUST INPUT YOUR HUGGINGFACE TOKEN")

    # Initialize the client with the Space name
    client = Client("tur-learning/MASt3R", hf_token=f"{HF_TOKEN}")

    # Make the API call
    result = client.predict(
        filelist=filelist,
        min_conf_thr=config["min_conf_thr"],
        matching_conf_thr=config["matching_conf_thr"],
        as_pointcloud=config["as_pointcloud"],
        cam_size=config["cam_size"],
        shared_intrinsics=config["shared_intrinsics"],
        api_name="/local_get_reconstructed_scene"
    )

    print("3D model output path:", result)

    print("Copying model to model.glb file")
    shutil.copyfile(result, "model.glb")

