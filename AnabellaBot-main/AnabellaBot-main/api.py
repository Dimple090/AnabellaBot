from flask import Flask, render_template, request, jsonify
import asyncio
from main_agent import main_agent  # Import your main_agent function
from playwright.async_api import async_playwright


messages = []
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
async def send():
    user_input = request.json.get('user_input')
    response = await main_agent(user_input,page="",messages=messages)  # Directly call main_agent without Playwright
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
