import sys
import langdetect
from openai import OpenAI
from config import API_KEY

api_key = API_KEY
client = OpenAI(api_key=api_key)

def generate_dynamic_code(static_code):
    # Wrap the static code in a prompt
    prompt = "Generate dynamic code for the following static code:\n" + static_code + "\n\nDynamic code with prompts:"
    
    
    # Define the conversation messages
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    dynamic_code = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            dynamic_code += chunk.choices[0].delta.content
    
    return dynamic_code

def detect_language(code):
    if "import" in code or "export" in code or ".tsx" in code:
        return "tsx"  
    else:
        return langdetect.detect(code)


def save_to_file(code, language):
    filename = f"Sample.{language}"
    with open(filename, "w") as file:
        file.write(code)
    print(f"Generated code saved to {filename}")

if __name__ == "__main__":
    print("Enter the static code (press Ctrl+D to finish):")
    static_code = sys.stdin.read()
    dynamic_code = generate_dynamic_code(static_code)
    language = detect_language(dynamic_code)
    save_to_file(dynamic_code, language)
