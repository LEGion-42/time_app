from flask import Flask
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    tz = timezone(timedelta(hours=-5))  # Timezone set to UTC-5
    now = datetime.now(tz)
    return now.strftime("%Y-%m-%d %H:%M:%S")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)