#Pulse = Daily summary bot
#Fetches: weather (wttr.in) + a quote (zenquotes.io)
#runs: everyday at 8 AM IST via Github actions

import requests
from datetime import date

def get_weather(city="Thiruvananthapuram"):
    """Fetch todays weather as a one line summary"""
    url=f"https://wttr.in/{city}?format=3"
    try:
        response= requests.get(url,timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Weather unavailable ({e})"
def get_quotes():
    """Fetch a random motivational quote from zen quotes"""
    url=f"https://zenquotes.io/api/random"
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        data=response.json()
        quote=data[0]["q"]
        author=data[0]["a"]
        return f'"{quote}" - {author}'
    except Exception as e:
        return f"Quote unavailable ({e})"
def build_summary():
    """"Assemble the full daily summary from all data sources"""
    today= date.today().strftime("%A %d %B %Y")
    weather=get_weather()
    quote=get_quotes()


    summary =f"""
====================================
    PULSE -Daily Summary
    {today}
====================================

WEATHER
    {weather}

TODAY'S QUOTE
    {quote}

====================================
"""
    return summary
def run():
    """Maint entry point. Called by github actions"""
    summary=build_summary()
    print(summary)

    with open("daily_summary.txt","w",encoding="utf-8") as f:
        f.write(summary)
    print("pulse ran succesfully.")

if __name__== "__main__":
    run()