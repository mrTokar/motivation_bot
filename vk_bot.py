import vk_api
from random import randint

class VkBot:
    __token = ""

    def __init__(self):
        # read token
        with open("token.txt") as token_file:
            self.__token = token_file.readline()
        if (self.__token == ""):
            raise Exception("Empty token")

        vk_session= vk_api.VkApi(token=self.__token)
        self._api = vk_session.get_api()

    def send_message(self, user_id: int, text: str):
        self._api.messages.send(user_id= user_id, random_id=randint(1, 2**30), message=text)


if __name__ == "__main__":
    bot = VkBot()
    bot.send_message(295004935, "This is bot")