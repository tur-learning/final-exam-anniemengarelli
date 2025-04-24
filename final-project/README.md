## Useful commands

Ciao and welcome to my final exam!

With this code, you will be able to create a 3D model using images you took on your phone!

The config.json file will be your new best friend. In the configuration file, you will find a dictionary that will allow you to manipulate the code. Below I will walk you through each setting, or line of code, so you know exactly how to use my project effectively!

First: "download": true
When set to true, the code will use the download_images function to download images from a google drive folder. If you have already downloaded images into the downloads directory, you can set this to false and that part of the code will not run.

Second: "image_directory": "downloads"
This piece of code sets the image directory as the downloads folder you created by downloading images. It is then used in the preprocess function as an input. You can change the name of the directory!

Third: "output_folder": "preprocessed"
This piece of code sets the output folder as the preprocessed folder that's created when you use the preprocess function. This function removes the background from the images. Output_folder, which is full of images of your object with the background removed, is then used as the input in the mast3r and dust3r functions. You can change the name of the directory!

Fourth: "use_dust3r": true
When set to true, the dust3r function will run. Dust3r will make your preprocessed images into a zip file which will then be sent to a HuggingFace, made into a 3D model, and then saved as model.glb in this codespace. You can set it to false if you don't want to use dust3r.

Fifth: "use mast3r": true
When set to true, the mast3r function will run. Mast3r will send your preprocessed images to the Mast3r HuggingFace model which will use them to create a 3D model. Then it will be saved as model.glb in this codespace. You can set it to false if you don't want to use mast3r.

Sixth: "Preprocess_image": true
When set to true, the preprocess function will run. This will remove the background from images you have downloaded into the codespace. When set to false, this step will be skipped.

Seventh: "Preprocess_model": "u2netp"
This line of code allows you to change the model that's used to preprocess the photos. You can see different model options here: https://huggingface.co/spaces/KenjieDec/RemBG

Ninth: "file_ids":...
This line of code is establishing the photos that will be downloaded from the google drive folder. You can change these photos with whatever ones you'd like from the google drive folder!

Mast3r_Model:
You can also change the settings that are used in making the master 3D model.

To run the code:
    python main.py

To run a python server:
    python -m http.server
    Then click viewer.html to see your completed model!


Thank you for using my code!
Analise