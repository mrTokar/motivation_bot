import console_gui as gui
from vk_bot import VkBot
from parse import get_messages_from_json
from dotenv import load_dotenv

__version__ = "1.2.0"

class MotivationBot(VkBot):
    motivation_path = ""
    photo_path = ""

    def __init__(self):
        print("Motivation Bot", __version__)
        load_dotenv()
        super().__init__()

    def _get_motivation_path(self):
        """Load motivational messages file path from user"""
        print("Загрузите индивидуальные мотивационнаые сообщения...")
        self.motivation_path = gui.select_file(
            ".json", 
            comment="с мотивационными сообщениями"
        )

    def _get_photo_path(self):
        """Load photo file path from user"""
        print("Загрузите изображение...")
        self.photo_path = gui.select_file(
            ".jpg", ".jpeg", ".png", ".gif",
            comment="изображения"
        )
        try:
            self.upload_photo(self.photo_path)
        except Exception as e:
            print("Ошибка при загрузке изображения:", e)

    def _send_messages_from_file(self):
        """Send motivational messages from file to users"""
        try:
            for vk_id, message in get_messages_from_json(self.motivation_path):
                self.send_message(vk_id, message)
                print(f"Sent to {vk_id}")
        except Exception as e:
            print("Ошибка при отправке сообщений:", e)

    def run(self):
        """Main method to run the Motivation Bot"""
        while True:  # loop until user confirms data
            if self.motivation_path == "":
                self._get_file_path()
            if gui.request("Хотите загрузить изображение?"):
                self._get_photo_path()

            print()
            
            print(f"Загруженные данные: \n-текст: {self.motivation_path} \n-изображение: {self.photo_path}")
            if gui.request("Все верно? Отправляем сообщения?"): break
        # Send messages
        self._send_messages_from_file()   
    
if __name__ == "__main__":
    MotivationBot().run()
