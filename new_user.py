import requests
from constants import Constants

constants = Constants()


class NewUser(Constants):
    def __init__(self):
        super().__init__()

    def new_user_response(self):
        # TODO Create a new user:
        response = requests.post(
            url=constants.PIXELA_ENDPOINT,
            json={
                "token": constants.TOKEN,
                "username": constants.USERNAME,
                "agreeTermsOfService": "yes",
                "notMinor": "yes"
            }
        )
        response.raise_for_status()
        print(f"{response.status_code}\n")
        print(response.text)
