import requests

# Replace with your Azure OpenAI details
API_KEY = "key"  # Enter your API key
ENDPOINT = "https://<resource-name>.openai.azure.com"  # Enter your endpoint
DEPLOYMENT_NAME = "gpt-35-turbo-16k"  # This is an example. Replace with your deployment name
API_VERSION = "2023-05-15"  # Example API version, adjust as per Azure documentation for the model deployed

def send_request(prompt, max_tokens=150):
    
    url = f"{ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version={API_VERSION}"
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }
    
    payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},  # System message
        {"role": "user", "content": prompt} # User message
    ],
    "max_tokens": max_tokens,   # Setting parameters
    "temperature": 0.7,
    "top_p": 0.95,
    "frequency_penalty": 0,
    "presence_penalty": 0
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        if response:
            print("Response content:", response.text)
        return None


if __name__ == "__main__":
    #set any prompt
    user_prompt = "Explain the concept of computer vision in AI."
    print("Sending request to Azure OpenAI...")
    result = send_request(user_prompt)
    if result:
        print("\nResponse from Azure OpenAI:")
        print(result)
    else:
        print("\nFailed to get a response.")
