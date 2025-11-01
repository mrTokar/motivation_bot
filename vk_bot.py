import os
from vk_api import VkApi
from vk_api.utils import get_random_id

class VkBot:
    __token = ""

    def __init__(self):
        # read token
        self.__token = os.getenv("VK_API_KEY")

        vk_session= VkApi(token=self.__token)
        self._api = vk_session.get_api()

    def send_message(self, user_id: int, text: str):
        self._api.messages.send(
            user_id= user_id,
            random_id= get_random_id(),
            message= text
        )


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    bot = VkBot()
    bot.send_message(295004935, "This is bot")