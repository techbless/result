from flask import Flask
from flask import request as req
import urllib.request
import json

app = Flask(__name__)

@app.route("/recommend")
def search():
    orgTitle = req.args.get('orgTitle')
    orgAuthor = req.args.get('orgAuthor')

    #title = urllib.parse.quote(orgTitle)
    #author = urllib.parse.quote(orgAuthor)
    print(orgTitle)

    with open(orgTitle + '.json') as json_file:
        data = json.load(json_file)
  
    return json.dumps(data, ensure_ascii=False)