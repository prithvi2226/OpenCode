import sys
import langdetect
from openai import OpenAI
from config import API_KEY

api_key = API_KEY
client = OpenAI(api_key=api_key)

def generate_dynamic_code(main_code, feature_code):
    # Wrap the main code and feature code in a prompt
    prompt1 = f"Generate dynamic code by incorporating the following \
                feature:\n{feature_code}\n\nInto the following main \
                    code:\n{main_code}\n\nDynamic code with prompts:"
    
    # Define the conversation messages
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt1}],
        stream=True,
    )
    dynamic_code = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            dynamic_code += chunk.choices[0].delta.content
    
    return dynamic_code

def detect_language(code):
    if "import" in code or "export" in code or ".jsx" in code:
        return "jsx"  
    else:
        return langdetect.detect(code)

def save_to_file(code, language):
    filename = f"Result.{language}"
    with open(filename, "w") as file:
        file.write(code)
    print(f"Generated code saved to {filename}")

if __name__ == "__main__":
    print("Enter the main code (press Ctrl+D to finish):")
    main_code = sys.stdin.read()
    print("Enter the feature code (press Ctrl+D to finish):")
    feature_code = sys.stdin.read()
    
    dynamic_code = generate_dynamic_code(main_code, feature_code)
    language = detect_language(dynamic_code)
    save_to_file(dynamic_code, language)
