# This is a simple example of how to use the Groundlight Python SDK. This example should be self contained, but if you would like to learn more, please consider visiting our Getting Started Guide: https://code.groundlight.ai/python-sdk/docs/getting-started or SDK Reference: https://code.groundlight.ai/python-sdk/api-reference-docs/.

# This program will use Groundlight's Python SDK to answer a simple question: "Is the door open?"

# our Python SDK
from groundlight import Groundlight

# framegrab is our open-source Python library, which makes it easy to set up cameras for computer vision applications, like Groundlight.
from framegrab import FrameGrabber
from time import sleep

# Initialize the SDK. We will use the gl object to interact with the Groundlight API.
gl = Groundlight()


# Question you want Groundlight to answer. Consider reading our short article on how to get the best results from Groundlight, which includes how to phrase your query: https://code.groundlight.ai/python-sdk/blog/best-practices
query_text = "Is the door open? This includes if the door is only partially open."

# Create a Groundlight Detector. This is where we will send image queries for answers. You can see the performance of your detectors on our webapp: https://app.groundlight.ai
detector = gl.get_or_create_detector(
    name="door_open_detector",
    query=query_text,
)


# We will use a USB webcam for this example. Visit the framegrab repo for more information on using other types of cameras: https://github.com/groundlight/framegrab
camera_config = {
    "input_type": "generic_usb",
}
camera = FrameGrabber.create_grabber(camera_config)


while True:
    image = camera.grab()

    # submit the image to Groundlight. This will return a Groundlight ImageQuery object, which will contain the answer to our question.
    image_query = gl.ask_confident(detector=detector, image=image)
    print(f"The answer is {image_query.result}")

    # how long to wait, in seconds, between queries to Groundlight
    sleep(10)

# When you are done, you can release the camera, otherwise other programs will not be able to use it.
camera.release()
