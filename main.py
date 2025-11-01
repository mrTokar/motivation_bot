import console_gui as gui
from vk_bot import VkBot
from parce import get_messages
from dotenv import load_dotenv

__version__ = "0.1.0"

class MotivationBot:
    motivation_path = ""
    sep_line = "="*80

    def __init__(self):
        print("Motivation Bot", __version__)
        load_dotenv()
        self.bot = VkBot()
    
    def get_file_path(self):
        print("Загрузите индивидуальные мотивационнаые сообщения...")
        self.motivation_path = gui.select_file("с мотивационными сообщениями")

    def run(self):
        if self.motivation_path == "":
            self.get_file_path()
            
        for vk_id, message in get_messages(self.motivation_path):
            self.bot.send_message(vk_id, message)
            print(f"Sent to {vk_id}: {message}")
    

    

if __name__ == "__main__":
    MotivationBot().run()
