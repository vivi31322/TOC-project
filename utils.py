import os
import random
import numpy as np

from linebot import LineBotApi, WebhookParser
from linebot.models import*# MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
np.random.seed(0)
def lottery():
    
    p = np.array([0.33, 0.33, 0.33, 0.01])
    index = np.random.choice([1, 0, 2, 3], p = p.ravel())
    return index
def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    msg = TextSendMessage(text=text)
    line_bot_api.reply_message(reply_token, msg)

    return "OK"

def send_oracle_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    msg=[]
    n=lottery()
    url=[['聖筊，\n海螺覺得可以~','https://tshop.r10s.com/c3745850-6485-11e8-90bd-a81e84d03920/coaster/coaster_smoothly.jpg'],
        ['笑筊，\n海螺覺得呵呵 :/','https://pic.pimg.tw/goodincense888/1498641821-694813174.jpg'],
        ['陰筊，\n海螺覺得不行 :(','https://pic.pimg.tw/ken201010/1560940820-747636450_n.jpg'],
        ['立筊，\n!!!!!天有異相!!!!!','']]
    msg.append(ImageSendMessage(original_content_url=url[n][1], preview_image_url=url[n][1]))
    msg.append(TextSendMessage(text=("神奇海螺決定給 "+url[n][0])))
   # msg.append(TextSendMessage(text=("神奇海螺決定給 "+url[n][0])))
    line_bot_api.reply_message(reply_token, msg)

    return "OK"

def send_lott_menu(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Confirm_template = TemplateSendMessage(
        alt_text='抽籤目錄',
        template=ConfirmTemplate(
            text='你想如何吩咐本海螺?( ͡° ͜ʖ ͡°)\n你有兩種選擇:',
            actions=[                              
                MessageTemplateAction(
                    label='神選數字',
                    text='num',
                ),
                MessageTemplateAction(
                    label='天擇選民',
                    text='text'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token,Confirm_template)

    return "OK"

def send_menu(user_id):
    line_bot_api = LineBotApi(channel_access_token)
    button_template_message =ButtonsTemplate(
                            thumbnail_image_url="https://i.imgur.com/KwefLw8.jpg",
                            title='吾乃神奇海螺，在線為民服務', 
                            text='人類，說出你的來意吧。\n請選擇功能',
                            ratio="1.5:1",
                            #image_size="cover",
                            actions=[
                                MessageTemplateAction(
                                    label='擲筊', 
                                    text='@@@擲筊@@@',
                                   
                                ),
                                MessageTemplateAction(
                                    label='抽籤', text='@@@抽籤@@@'
                                ),
                            ]
                        )
    line_bot_api.push_message(user_id, TemplateSendMessage(alt_text="Template Example", template=button_template_message))

    return "OK"

def send_lott_final_msg(reply_token, op,n,lo_text):
    
    
    if op==True :
        m=random.randint(1, n)
        send_text_message(reply_token,"===結果出爐===\n\n恭喜 "+str(m)+" 被選中!\n面對命運吧 (΄◞ิ౪◟ิ‵)")
    else:
        send_text_message(reply_token,"===結果出爐===\n\n恭喜 "+np.random.choice(lo_text)+" 被選中!\n面對命運吧 (΄◞ิ౪◟ิ‵)")
    
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
