# Chatbot service - OpenAI Function Calling

## Create api key to use OpenAI models
- Go to "https://platform.openai.com/" to sign up and create api key
- Them go to ".env", fill in OPENAI_API_KEY

## Run
```
pip install -r requirements.txt
uvicorn main:app --reload
```
- "main:app" is a application in main.py with app function
- "--reload" is an optional, will restart automatically when detecting the change in source
- After run the above command: go to "http://127.0.0.1:8000/docs" to use the app  

## Demo
![](./chatbot_function_calling/Demo.mp4)