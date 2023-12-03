import requests

base_url = 'http://evgeniymuravyov.pythonanywhere.com'

response = requests.post(f'{base_url}/new_chat')
chat_id = response.json()['chat_id']
print(f'New chat created. Chat ID: {chat_id}')

message_data = {
    'message': 'Hello, chatbot!'
}
response = requests.post(f'{base_url}/chat/{chat_id}', json=message_data)
assistant_response = response.json()['assistant_response']
print(f'Assistant Response: {assistant_response}')

response = requests.get(f'{base_url}/messages/{chat_id}')
chat_messages = response.json()['messages']
print('Chat Messages:')
for message in chat_messages:
    print(f"{message['role']}: {message['content']}")