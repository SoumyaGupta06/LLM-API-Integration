import requests

# Configuration
API_KEY = "key"  #insert actual key
BASE_URL = "http://127.0.0.1:8080"  # Update as per your url
MODEL_ENDPOINT = "/completion"  # Endpoint needed to connect with models on Anaconda AI Navigator

url = f"{BASE_URL}{MODEL_ENDPOINT}"

def connect_and_communicate(prompt):
    payload = {
        "prompt":  prompt
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",  
        "Content-Type": "application/json"    
    }
    try:
        
        response = requests.post(url, json=payload, headers=headers)
     
        if response.status_code == 200:
            print("Model Response:")
            print(response.json())  # Print the model's response
        else:
            print(f"Failed to connect to the model. Status Code: {response.status_code}")
            print("Response Text:", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred while connecting to the model:", str(e))


def call():
    #Send any prompt
    connect_and_communicate("How is the weather in Delhi?")

if __name__ == "__main__":
    call()

