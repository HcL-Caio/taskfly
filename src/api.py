import requests

def get_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice", timeout=5)
        data = response.json()
        return data["slip"]["advice"]
    except:
        return "Stay focused and keep improving! 💪"
