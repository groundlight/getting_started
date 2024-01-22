# This is a simple example of how to use the Groundlight Python SDK. This example should be self contained, but if you would like to learn more, please consider visiting our Getting Started Guide: https://code.groundlight.ai/python-sdk/docs/getting-started or SDK Reference: https://code.groundlight.ai/python-sdk/api-reference-docs/.

# This program will use Groundlight's Python SDK to answer a simple question: "Is the door open?"

import os
from time import sleep

import yaml
from dotenv import load_dotenv
from framegrab import (
    FrameGrabber,  # framegrab is our open-source Python library, which makes it easy to set up cameras for computer vision applications, like Groundlight.
)
from groundlight import Groundlight  # our Python SDK

# loads the contents of the .env file into the environment, including your Groundlight API Token
load_dotenv()

# Check if GROUNDLIGHT_API_TOKEN is set in the .env file and starts with "api_", if not, raise an error.
api_token = os.getenv("GROUNDLIGHT_API_TOKEN")
if not api_token or not api_token.startswith("api_"):
    raise ValueError(
        "The 'GROUNDLIGHT_API_TOKEN' is not set correctly in the .env file. It should start with 'api_'. You can create a token here: https://app.groundlight.ai/reef/my-account/api-tokens."
    )

# Initialize the SDK. We will use the gl object to interact with the Groundlight API.
gl = Groundlight()

# Question you want Groundlight to answer. Consider reading our short article on how to get the best results from Groundlight, which includes how to phrase your query: https://code.groundlight.ai/python-sdk/blog/best-practices
query_text = "Is the door open? This includes if the door is only partially open."

# Create a Groundlight Detector. This is where we will send image queries for answers. You can see the performance of your detectors on our webapp: https://app.groundlight.ai
detector = gl.get_or_create_detector(
    name="door_open_detector",
    query=query_text,
)

# We will use a USB webcam for this example, configured in the camera_config.yaml file. Visit the framegrab repo for more information on using other types of cameras: https://github.com/groundlight/framegrab
config_path = "camera_config.yaml"
with open(config_path, "r") as f:
    camera_config = yaml.safe_load(f)
print(camera_config)


camera = FrameGrabber.create_grabber(camera_config)

while True:
    image = camera.grab()

    # submit the image to Groundlight. This will return a Groundlight ImageQuery object, which will contain the answer to our query.
    image_query = gl.ask_confident(detector=detector, image=image)
    print(f"The answer is {image_query.result}")

    # how long to wait, in seconds, between queries to Groundlight
    sleep(10)

# TODO: put in a try finally block?
# When you are done, you can release the camera, otherwise other programs will not be able to use it.
camera.release()
