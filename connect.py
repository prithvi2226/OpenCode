'''
We first try to connect the figma api
and try to get a figma file by its key
'''

import requests

figma_API_base_url = "https://api.figma.com"



def get_figma_file(file_key):

    url = f"https://api.figma.com/v1/files/{file_key}"

    headers = {
        "X-figma-token": access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        figma_file = response.json()
        return figma_file
    else:
        print(f"Failed to fetch Figma file: {response.text}")

if __name__ == "__main__":
    file_key = "HOEemgNB1Ce3lo4qn0jKeN"
    figma_file = get_figma_file(file_key)

    if figma_file:
        print("figma file fetched successfully!")
        print(figma_file)



