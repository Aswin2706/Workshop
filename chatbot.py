import gradio
from groq import Groq
client = Groq(
    api_key="Your api key",
)
def initialize_messages():
    return [{"role": "system",
             "content": """You are a skilled driver with a
             successful track record in various rides experience. Your role is to
             assist people by providing guidance on driving suggestion and
             correction."""}]
messages_prmt = initialize_messages()
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to vehicle"),
                     title="Driver Assistance",
                     description="Chat bot for drive assistance",
                     theme="soft",
                     examples=["hi","Speed limit", "Parking Assistance"]
                     )
iface.launch(share=True)