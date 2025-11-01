import console_gui as gui
from vk_bot import VkBot
from parse import get_messages
from dotenv import load_dotenv

__version__ = "1.0.0"

class MotivationBot:
    motivation_path = ""
    photo_path = ""
    sep_line = "="*80

    def __init__(self):
        print("Motivation Bot", __version__)
        load_dotenv()
        self.bot = VkBot()
    
    def _get_file_path(self):
        print("Загрузите индивидуальные мотивационнаые сообщения...")
        self.motivation_path = gui.select_file("с мотивационными сообщениями")
        if (gui.request("Хотите заменить разделяющую строку?", default_answer=False)):
            self.sep_line = input("Введите новую разделяющую строку: ")

    def _send_messages(self):
        for vk_id, message in get_messages(self.motivation_path, self.sep_line):
            self.bot.send_message(vk_id, message)
            print(f"Sent to {vk_id}")
    
    def run(self):
        while True:
            if self.motivation_path == "":
                self._get_file_path()
            if gui.request("Хотите загрузить изображение?"):
                self.photo_path = gui.select_file("изображения")
                self.bot.upload_photo(self.photo_path)
            print()
            
            print(f"Загруженные данные: \n-текст: {self.motivation_path} \n-изображение: {self.photo_path}")
            if gui.request("Все верно? Отправляем сообщения?"): break

        self._send_messages()   
    
if __name__ == "__main__":
    MotivationBot().run()
