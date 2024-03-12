'''
We first try to connect the figma api
and try to get a figma file by its key
'''
import json
import requests

figma_API_base_url = "https://api.figma.com"
access_token = "figd_tIhiqKQTIjWzR_eUrwiNnyShdC7Do8XKdAVwgOaF"


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
        # print(figma_file)

        with open("figma_file.json", "w") as json_file:
            json.dump(figma_file, json_file, indent=4)




