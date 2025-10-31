import vk_api
import os
from random import randint
from dotenv import load_dotenv

class VkBot:
    __token = ""

    def __init__(self):
        # read token
        self.__token = os.getenv("VK_API_KEY")

        vk_session= vk_api.VkApi(token=self.__token)
        self._api = vk_session.get_api()

    def send_message(self, user_id: int, text: str):
        self._api.messages.send(user_id= user_id, random_id=randint(1, 2**30), message=text)


if __name__ == "__main__":
    load_dotenv()
    bot = VkBot()
    bot.send_message(295004935, "This is bot")