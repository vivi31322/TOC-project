from transitions.extensions import GraphMachine

from utils import*# send_text_message
n=1
op=False
lo_text=[]
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == '召喚海螺'

    def is_going_to_oracle(self, event):
        text = event.message.text
        return text == "@@@擲筊@@@"

    def is_going_to_lottery(self, event):
        text = event.message.text
        return text == "@@@抽籤@@@"

    def is_going_to_ora_final(self, event):
        return True
        

    def is_going_to_lott_num(self, event):
        text = event.message.text
        return text.lower() == "num"

    def is_going_to_lott_text(self, event):
        text = event.message.text
        return text.lower() == "text"
    
    def is_going_to_lott_final(self, event):
        global n,lo_text,op
        text = event.message.text
        if text.lower().isnumeric() and op:
            n = int(text)
            return True
        elif not op :
           lo_text=text.split('\n')
           return True
        return False


    def on_enter_menu(self, event):
        print("I'm entering menu")
        send_menu(event.source.user_id,)
        
        #self.go_back()
    
    def on_enter_oracle(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token,'發問吧，人類。向我尋求解答( ಠ ͜ʖರೃ)')
        

    def on_enter_lottery(self, event):
        print("I'm entering lottery")
        reply_token = event.reply_token
        send_lott_menu(reply_token)
        
        

    def on_enter_ora_final(self, event):
        print("I'm entering orafinal")
        reply_token = event.reply_token
        send_oracle_message(reply_token)
        
        self.go_back(event)

    def on_enter_lott_num(self, event):
        global op
        print("I'm entering lotnum")
        op=True
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入數字範圍上限，\n將隨機抽選1~此數字。")
        
        
    
    def on_enter_lott_text(self, event):
        print("I'm entering lotnum")
        global op
        op=False
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入抽籤選項，以換行區別每個選項。")
        

    def on_enter_lott_final(self, event):
        global op,n,lo_text
        print("I'm entering lotfinal")
        reply_token = event.reply_token
        send_lott_final_msg(reply_token, op,n,lo_text)
        op=False
        n=1
        lo_text=[]
        self.go_back(event)    

    def on_exit_state1(self):
        print("Leaving state1")

