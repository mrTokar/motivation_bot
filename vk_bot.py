import os
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.upload import VkUpload

class VkBot:
    __token = ""
    _photo = ""

    def __init__(self):
        # read token
        self.__token = os.getenv("VK_API_KEY")
        vk_session= VkApi(token=self.__token)
        self._api = vk_session.get_api()
        self._upload = VkUpload(self._api)

    def upload_photo(self, photo_file:str) -> bool:
        if os.path.exists(photo_file):
            response = self._upload.photo_messages(photo_file)[0]
            self._photo = f"photo{response["owner_id"]}_{response["id"]}"
            return True
        else:
            print("Failed to upload photo")
            return False

    def remove_photo(self):
        self._photo = ""

    def send_message(self, user_id: int, text: str):
        if self._photo == "":
            self._api.messages.send(
                user_id= user_id,
                random_id= get_random_id(),
                message= text
            )
        else:
            self._api.messages.send(
                user_id= user_id,
                random_id= get_random_id(),
                message= text,
                attachment= self._photo
            )


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    bot = VkBot()
    bot.upload_photo("source/image.jpg")
    bot.send_message(295004935, "This is bot")