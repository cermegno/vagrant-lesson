import os
from flask import Flask
import redis

r = redis.Redis(host='192.168.56.11', port='6379')
counter = r.get('counter')
print counter

app = Flask(__name__)

@app.route('/')
def mainmenu():

    global r
    counter = r.incr('counter')

    return """
    <html>
    <body>

    <center><h1>Hi, I'm up<br/>
	<h2><u>The Flask provisioning thru Vagrant worked!!<br>
	Number of page views: {0}<br>
    </center>
    </body>
    </html>
    """.format(counter)

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
