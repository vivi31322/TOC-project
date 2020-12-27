import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "menu", "oracle","lottery","lott_num","lott_text","ora_final","lott_final"],
    transitions=[
        {"trigger": "advance","source": "user","dest": "menu","conditions": "is_going_to_menu"},
        {"trigger": "advance","source": "menu","dest": "oracle","conditions": "is_going_to_oracle"},
        {"trigger": "advance","source": "menu","dest": "lottery","conditions": "is_going_to_lottery"},
        {"trigger": "advance","source": "oracle","dest": "ora_final","conditions": "is_going_to_ora_final"},
        {"trigger": "advance","source": "lottery","dest": "lott_num","conditions": "is_going_to_lott_num"},
        {"trigger": "advance","source": "lottery","dest": "lott_text","conditions": "is_going_to_lott_text"},
        {"trigger": "advance","source": ["lott_num","lott_text"],"dest": "lott_final","conditions": "is_going_to_lott_final"},
        #{"trigger": "advance","source": "lott_text","dest": "lott_final","conditions": "is_going_to_"},
        {"trigger": "go_back", "source": ["lott_final", "ora_final"], "dest": "menu"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = "a3787783654163236a09e6dde29b08c8"
channel_access_token = "+1raVzws1NpP7Kny+PDWFMRACrHHfG0E6HiQawFPOSIPUV69VzAzqENYWjFZw5fFP72gveEaJigI6HQsjDvf3Tdu2QaXsGmYsqs6g2UXfmgAp+VtagjIuefuQkjHGlvIh/lvUbSjNv9Va2/KsYh+wAdB04t89/1O/w1cDnyilFU="
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")

        #start here


        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "請好好使用海螺ˋˊ")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
