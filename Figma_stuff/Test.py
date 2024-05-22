from openai import OpenAI
from config import API_KEY

# Initialize the OpenAI client with your API key
api_key = API_KEY
client = OpenAI(api_key=api_key)

def generate_dynamic_code(static_code):
    # Define the conversation messages
    stream = client.chat.completions.create(
        model="text-davinci-003",
        messages=[{"role": "user", "content": static_code}],
        stream=True,
    )
    dynamic_code = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            dynamic_code += chunk.choices[0].delta.content
    return dynamic_code

def remove_newlines(code):
    return code.replace("\n", " ")

if __name__ == "__main__":
    static_code = input("Enter the static code: ")
    static_code_single_line = remove_newlines(static_code)
    dynamic_code = generate_dynamic_code(static_code_single_line)
    print("Dynamic code output:")
    print(dynamic_code)
