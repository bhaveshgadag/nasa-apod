import requests

API_KEY = "Cc5PehSUdUcHYqawg3mya68sK6JJZBjs7lt3pADi"

def get_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    response = requests.get(url)
    content = response.json()

    return content

if __name__ == '__main__':
    content = get_apod()
    print(content)
