# This is a simple example of how to use the Groundlight Python SDK. This example should be self contained, but if you would like to learn more, please consider visiting our Getting Started Guide: https://code.groundlight.ai/python-sdk/docs/getting-started or SDK Reference: https://code.groundlight.ai/python-sdk/api-reference-docs/.

# This program will use Groundlight's Python SDK to answer a simple question: "Is the door open?"

import os
from time import sleep

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
detector_name = "door_open_detector"
# Create a Groundlight Detector. This is where we will send image queries for answers. You can see the performance of your detectors on our webapp: https://app.groundlight.ai
detector = gl.get_or_create_detector(
    name=detector_name,
    query=query_text,
)

# Next we have to set up the camera we will use for this application. Framegrab automatically detects all cameras connected to your computer, and this app uses the first one it finds (unless you change the camera_index variable below).
# If you would like more sophisticated configuration of your camera, visit the framegrab repo for more information on how to automatically crop, zoom, set resolution, or add motion detection: https://github.com/groundlight/framegrab
cameras = FrameGrabber.autodiscover()
camera_index = 0  # NOTE: If on a Mac, framegrab might consider your iPhone as the first valid camera, so you might need to change this index to use your computer's webcam.

if len(cameras) == 0:
    raise ValueError("No cameras found. Please connect a camera and try again.")
elif len(cameras) > 1:
    print(f"Found {len(cameras)} cameras. Here are the configs for each camera:")
    for camera in cameras.values():
        print(camera.config)
    print(
        f'Using camera number {camera_index+1} from the list. If you would like to use a different camera, change the "camera_index" variable in main.py'
    )

camera = list(cameras.values())[camera_index]

try:
    while True:
        image = camera.grab()

        # submit the image to Groundlight. This will return a Groundlight ImageQuery object, which will contain the answer to our query.
        image_query = gl.ask_confident(detector=detector, image=image)
        print(f"The answer is {image_query.result}")

        # how long to wait, in seconds, between queries to Groundlight
        sleep(10)
finally:
    # When done, release the camera, otherwise other programs will not be able to use it.
    camera.release()
