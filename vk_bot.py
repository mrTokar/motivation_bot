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
            self._photo = f"photo{response["owner_id"]}_{response["photo_id"]}_{response["access_key"]}"
            return True
        else:
            print("Failed to upload photo")
            return False

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