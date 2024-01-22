# Getting started with Groundlight
Welcome! This is a small "Hello World" example for Groundlight. Please clone this repo, and we will walk you through how to get your first Groundlight application up and running! If you have any questions, please reach out to us by filing a GitHub issue, emailing us at support@groundlight.ai or by messaging us via the chat widget in the bottom right hand corner of the [Groundlight web app](https://app.groundlight.ai/).

## Your First Groundlight Application
This example application uses Groundlight to answer the question: "Is the door open?". The application takes a picture from a USB webcam every 10 seconds, and sends it to Groundlight for processing. 

1. Create a Groundlight account at [https://app.groundlight.ai/](https://app.groundlight.ai/). 
2. Create an API token by clicking on your account name in the top right corner, and then clicking on "API Tokens". Alternatively, you can click [here](https://app.groundlight.ai/reef/my-account/api-tokens).
3. Paste your API token into the `GROUNDLIGHT_API_TOKEN` variable in the `.env` file.
4. Plug a USB webcam into your computer. #TODO: do we want this to "just work" on a laptop camera too??
5. Install python dependencies by running `pip install -r requirements.txt` in the root directory of this repo.
6. Run `python main.py` in the root directory of this repo.
7. Check out the results in the [Groundlight web app](https://app.groundlight.ai/reef/)!

## Learning More - Additional Resources
1. Read over the code in `main.py` and try modifying the query to solve a different problem. It's as simple as changing the `query_text` and `detector_name` variables.
2. Read our guide to Getting Started with Groundlight [here](https://code.groundlight.ai/python-sdk/docs/getting-started).
3. Read our SDK documentation [here](https://code.groundlight.ai/python-sdk/api-reference-docs/).

## [Optional] Deploy on Raspberry Pi
1. Flash your Raspberry Pi with the latest version of our Raspberry Pi Image. You can find instructions [here](https://github.com/groundlight/groundlight-pi-gen?tab=readme-ov-file#groundlight-pi-gen-os-images-for-raspberry-pi-with-groundlight-tools).
2. Clone this repo on your Raspberry Pi.
3. Follow the instructions above, in the [Your First Groundlight Application](#your-first-groundlight-application) section.
