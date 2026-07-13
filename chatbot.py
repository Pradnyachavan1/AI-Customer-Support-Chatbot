print("Using OLLAMA chatbot.py")
import ollama

def ask_chatbot(question):
    """
    Sends the user's question to the local Llama 3.2 model
    and returns the generated answer.
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]