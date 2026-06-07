# Unfinished code, TODO: Add tool call for pybricks api. 
import requests
import json

api_key = input("Enter your API key: ")
query = input("Enter your query: ")
response = requests.post(
    'https://ai.hackclub.com/proxy/v1/responses',
    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    },
    json={
        'model': 'qwen/qwen3-32b',
        'input': query,
        'stream': True,
        'max_output_tokens': 9000,
    },
    stream=True
)

for line in response.iter_lines():
    if line:
        line_str = line.decode('utf-8')
        if line_str.startswith('data: '):
            data = line_str[6:]
            if data == '[DONE]':
                break
            try:
                parsed = json.loads(data)
                print(parsed)
            except json.JSONDecodeError:
                continue