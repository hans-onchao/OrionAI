from flask import Flask, request, jsonify, render_template
from chat_ai import ask_ai
import markdown

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    # Get raw Markdown reply from AI
    ai_reply_markdown = ask_ai(user_input)

    # Convert Markdown to HTML with code block support
    ai_reply_html = markdown.markdown(
        ai_reply_markdown,
        extensions=['fenced_code', 'codehilite']
    )

    # Return the HTML-formatted reply
    return jsonify({"reply": ai_reply_html})

if __name__ == "__main__":
    app.run(debug=True)
