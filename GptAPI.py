# from openai import OpenAI
# from config import API_KEY

# # # Initialize the OpenAI client with your API key
# api_key = API_KEY
# client = OpenAI(api_key=api_key)


# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "What do u think about kid cudi"}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")
# a


from openai import OpenAI
from config import API_KEY

api_key = API_KEY
client = OpenAI(api_key=api_key)

def generate_dynamic_code(static_code):
    stream = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": "Here is the static code: {static_code}, I need to change it a dynamic code, give me dynamic code"}],
        stream = True,
    )

    dynamic_code = ""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            dynamic_code += chunk.choices[0].delta.content
    return dynamic_code


if __name__ == "__main__":
    static_code = input("Enter Static Code: ")
    dynamic_code = generate_dynamic_code(static_code)

    print("dynamic code with prompts: ")
    print(dynamic_code)







