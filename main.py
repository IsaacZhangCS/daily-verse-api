
from fastapi import FastAPI
import json
from datetime import datetime
import pytz

app = FastAPI()

# Load verses from file
with open("verses.json") as f:
    verses = json.load(f)

@app.get("/verse-of-the-day")
def get_verse_of_the_day():
    # Get the current day in PST
    pst = pytz.timezone("America/Los_Angeles")
    today = datetime.now(pst)
    day_of_year = today.timetuple().tm_yday

    # Select the verse based on day of the year
    verse = verses[day_of_year % len(verses)]

    # Return the response
    return {
        "verse": {
            "details": {
                "reference": verse["reference"],
                "text": verse["text"]
            }
        }
    }
