import json
import requests

# Configuration for the API (hypothetical setup based on provided documentation)
API_BASE_URL = 'http://192.168.10.100:11434/api/generate'
API_KEY = ''  # Your API key, if needed

# Function to send tasks to the API, adjusted to API specifications
def send_task_to_crewai(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'mistral:7b',  # Specifying the model
        'prompt': prompt,
        'stream': False  # Assuming non-streaming for simplicity
    }
    response = requests.post(API_BASE_URL, headers=headers, json=data)
    try:
        return response.json()
    except json.decoder.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        print("Raw response:", response.text)
        return None

# Example task for the CrewAI
prompt = 'Create a YouTube video explaining basic computer algorithms'

# Send the task to the CrewAI
result = send_task_to_crewai(prompt)

print("Task submission result:", json.dumps(result, indent=4))
