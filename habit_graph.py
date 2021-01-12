from constants import Constants
import requests

constants = Constants()


class Habits(Constants):
    def __init__(self):
        super().__init__()
        self.endpoint = f"{constants.PIXELA_ENDPOINT}/{constants.USERNAME}/graphs"

    def habit_response(self):
        # TODO 2. Create a graph definition habit (Coding Time):
        response = requests.post(
            headers=constants.HEADERS,
            url=self.endpoint,
            json={
                "id": constants.GRAPH_ID,
                "name": "Coding Time",
                "unit": "Hours",
                "type": "float",
                "color": "ajisai",
                "timezone": "Asia/Amman"
            }
        )

        response.raise_for_status()
        print(f"{response.status_code}\n")
        print(response.text)

