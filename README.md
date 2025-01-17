**LLM Integration via REST API**

This project demonstrates how to connect and interact with a locally installed Large Language Model (LLM) on Anaconda AI Navigator using a REST API. It includes Python code for sending prompts and receiving responses from the LLM.

Features:

1. Connect to a locally hosted LLM using REST API.
2. Send prompts for text generation tasks.
3. Use API key authentication for secure communication.

Installation:

1. Set up Anaconda AI Navigator:
   Install Anaconda AI Navigator.
   On the 'models' tab explore available models and download one as per memory allocated. This code was tested on TinyLlama-1.1B-Chat-v1.0 model for text generation.
2. Clone the Repository:
   git clone https://github.com/SoumyaGupta06/LLM-API-Integration.git
   cd LLM-API-Integration
3. Install Dependencies: Ensure Python and requests library are installed.
   pip install requests

Usage:

1. Run the LLM:
   Launch the LLM on Anaconda AI Navigator and note the base URL and API key.
2. Configure the Script:
   Update BASE_URL and API_KEY in the script. Keep the Endpoint as is.
3. Run the Script:
   Execute the script to receive the response for the prompt encoded.

Example Output:
Model Response:
{
  "response": "The weather in Delhi is sunny and warm."
}

Future Enhancements
1. Add support for advanced LLM features.
2. Integrate with a web UI or application for improved accessibility and usage.

