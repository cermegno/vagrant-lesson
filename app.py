import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainmenu():

    return """
    <html>
    <body>

    <center><h1>Hi, I'm up<br/>
	<h2><u>The Flask provisioning thru Vagrant worked!!
    </br>
    </center>
    </body>
    </html>
    """

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
