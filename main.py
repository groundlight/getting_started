# This is a simple example of how to use the Groundlight Python SDK. This example should be self contained, but if you would like to learn more, please consider visiting our Getting Started Guide: https://code.groundlight.ai/python-sdk/docs/getting-started or SDK Reference: https://code.groundlight.ai/python-sdk/api-reference-docs/.

# This program will use Groundlight's Python SDK to answer a simple question: "Is the door open?"

from time import sleep

from groundlight import Groundlight  # our Python SDK

from setup import load_and_validate_api_key, setup_camera

# load your Groundlight API Token from the .env file, and validate that it is set correctly.
load_and_validate_api_key()

# set up the camera using framegrab, our open-source Python library. You can learn more about it in setup.py.
camera = setup_camera()

# Initialize the SDK. We will use the gl object to interact with the Groundlight API.
gl = Groundlight()

# Question you want Groundlight to answer. Consider reading our short article on how to get the best results from Groundlight, which includes how to phrase your query: https://code.groundlight.ai/python-sdk/blog/best-practices
query_text = "Is the door open? This includes if the door is only partially open."

# Create a Groundlight Detector. This is where we will send image queries for answers. You can see the performance of your detectors on our webapp: https://app.groundlight.ai
detector_name = "door_open_detector"

detector = gl.get_or_create_detector(
    name=detector_name,
    query=query_text,
)


try:
    while True:
        image = camera.grab()

        # submit the image to Groundlight. This will return a Groundlight ImageQuery object, which will contain the answer to our query.
        # if you prefer Groundlight's most confident answer, consider using the ask_confident method instead. This method will be slower in cases where the detector's ML model is not confident in its answer, as we will escalate the query to a human.
        # Read more about all of the ways to query Groundlight here: https://code.groundlight.ai/python-sdk/api-reference-docs/models.html
        image_query = gl.ask_ml(detector=detector, image=image)
        print(f"The answer to the query is {image_query.result.label.value}")

        # how long to wait, in seconds, between queries to Groundlight
        sleep(10)
finally:
    # When done, release the camera, otherwise other programs will not be able to use it.
    camera.release()
