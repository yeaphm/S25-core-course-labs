from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def moscow_time():
    # Get Moscow time (UTC+3)
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"Current time in Moscow: {current_time}"

if __name__ == '__main__':
    app.run()