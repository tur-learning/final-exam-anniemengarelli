# 1
# Import necessary modules
import json
from preprocess import preprocess
from download_images import download_images
from dust3r import dust3r_function
from mast3r import mast3r_function

# 2
# input config.json to read configurations

with open("config.json") as f:
    config = json.load(f)

# 3
# implement logic to use different models based on the configured parameters

# This will download the file_ids that were specified in the config.json. It will also place them in the image_directory specified 
# in config.json
if config["download"]:
    download_images(file_ids = config["file_ids"],
                    image_directory = config["image_directory"]) 
    print("The files have been downloaded")

# This will run the preprocessed function (preprocess), using the model and image_directory specified in config.json, and output 
# them in the output_folder specified in config.json
if config["preprocess_image"]:
    print("We are going to preprocess the image to remove the background")
    preprocess(preprocess_model = config["preprocess_model"],
                root_directory = config["image_directory"],
                output_folder = config["output_folder"])

# This will run the dust3r_function using the output_folder specified in config.json
if config["use_dust3r"]:
    print("We are going to use dust3r APIs")
    dust3r_function(input = config["output_folder"])
    
# This will run the mast3r_function specified in config.json. It will use the parameters specified in config.json
if config["use_mast3r"]:
    print("We are going to use mast3r APIs")
    mast3r_function(input = config["output_folder"],
                    config = config["mast3r_model"])

