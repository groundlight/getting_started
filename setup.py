import os

from dotenv import load_dotenv
from framegrab import (
    FrameGrabber,  # framegrab is our open-source Python library, which makes it easy to set up cameras for computer vision applications, like Groundlight.
)


def load_and_validate_api_key():
    """
    Loads the contents of the .env file into the environment, including your Groundlight API Token. Validates that the token is set correctly, and raises an error if not.
    """

    # loads the contents of the .env file into the environment, including your Groundlight API Token
    load_dotenv()

    # Check if GROUNDLIGHT_API_TOKEN is set properly, and raise an error if not
    api_token = os.getenv("GROUNDLIGHT_API_TOKEN")
    if not api_token or not api_token.startswith("api_"):
        raise ValueError(
            "The 'GROUNDLIGHT_API_TOKEN' is not set correctly in the .env file. It should start with 'api_'. You can create a token here: https://app.groundlight.ai/reef/my-account/api-tokens."
        )


def setup_camera() -> FrameGrabber:
    """
    Uses framegrab to set up camera
    """
    # Framegrab automatically detects all cameras connected to your computer, and this app uses the first one it finds (unless you change the camera_index variable below).
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
            f'Using camera number {camera_index+1} from the list. If you would like to use a different camera, change the "camera_index" variable in setup.py'
        )

    camera = list(cameras.values())[camera_index]
    return camera
