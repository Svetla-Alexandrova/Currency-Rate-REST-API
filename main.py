from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  
  return rate
  
app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_curr>-<out_curr>')
def api(in_curr, out_curr):
  rate = get_currency(in_curr, out_curr)
  result_dictionary = {'input currency': in_curr, 'output currency': out_curr, "rate": rate}
  return jsonify(result_dictionary)
  
  
app.run(host='0.0.0.0')

