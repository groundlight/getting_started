# Getting started with Groundlight
Welcome! This is a small "Hello World" example for Groundlight. Please clone this repo, and this readme will walk you through how to get your first Groundlight application up and running! If you have any questions, please reach out to us by filing a GitHub issue, emailing us at support@groundlight.ai or by messaging us via the chat widget in the bottom right hand corner of the [Groundlight web app](https://app.groundlight.ai/).

## Your First Groundlight Application
This example application uses Groundlight to answer the question: "Is the door open?". The application takes a picture from a camera connected to your computer every 10 seconds, and sends it to Groundlight for processing. 

1. Create a free Groundlight account at [https://app.groundlight.ai/](https://app.groundlight.ai/). 
2. Create an API token by clicking on your account name in the top right corner, and then clicking on "API Tokens". Alternatively, you can click [here](https://app.groundlight.ai/reef/my-account/api-tokens) to go to the page directly.
3. Paste your API token into the `GROUNDLIGHT_API_TOKEN` variable in the `.env` file (make sure you do not check this file into version control, as it contains your secret API token). 
4. Ensure your computer has a camera, either a built in webcam or a USB camera. The application will automatically detect your camera. If you are on a Mac, the application might detect your iPhone as your primary webcam. See the notes in `setup.py` for how to change this to your built in webcam, if desired.
5. Install python dependencies by running `pip install -r requirements.txt`.
6. Aim your camera at a door.
7. Run `python main.py` to start the application.
8. Test out the application by opening and closing the door. You should see the application print out whether the door is open or closed every 10 seconds.
9. Explore your results in more depth in the [Groundlight web app](https://app.groundlight.ai/reef/)!

## Learning More - Additional Resources
1. Read over the code in `main.py` and try modifying the query to solve a different problem. It's as simple as changing the `query_text` and `detector_name` variables.
2. Read our guide to Getting Started with Groundlight [here](https://code.groundlight.ai/python-sdk/docs/getting-started).
3. Read our SDK documentation [here](https://code.groundlight.ai/python-sdk/api-reference-docs/).
4. Ask us questions! We would love to help you get started. See how to contact us in the [Getting Started with Groundlight](#getting-started-with-groundlight) section above.

## [Optional] Deploy on Raspberry Pi
If you have a Raspberry Pi with a camera, you can deploy this application on your Raspberry Pi. This is a great way to get started with Groundlight, as you can deploy your application in a low cost, low power environment.
1. Flash your Raspberry Pi with the latest version of our Raspberry Pi Image. You can find instructions [here](https://github.com/groundlight/groundlight-pi-gen?tab=readme-ov-file#groundlight-pi-gen-os-images-for-raspberry-pi-with-groundlight-tools).
2. Clone this repo on your Raspberry Pi.
3. Follow the instructions above, in the [Your First Groundlight Application](#your-first-groundlight-application) section.
