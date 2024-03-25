from openai import OpenAI
from config import API_KEY

# # Initialize the OpenAI client with your API key
api_key = API_KEY
client = OpenAI(api_key=api_key)

# # Define the conversation messages
# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
# ]

# # Create completions for the conversation
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=messages
# )

# # Print the response
# print(response)


###
from openai import OpenAI

# client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What do u think about kid cudi"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")



