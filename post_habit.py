import requests
from constants import Constants
constants = Constants()


class PostHabit(Constants):
    def __init__(self):
        super().__init__()
        self.endpoint = f"{constants.PIXELA_ENDPOINT}/{constants.USERNAME}/graphs/{constants.GRAPH_ID}"

    def post_response(self):
        # TODO: Post value to the graph:
        response = requests.post(
            headers=constants.HEADERS,
            url=self.endpoint,
            json={

                #  "date": constants.FORMATTED_YESTERDAY,

                "date": constants.DATE.strftime("%Y%m%d"),
                "quantity": input("How many hours did we code today? ")
            }
        )
        response.raise_for_status()
        print(response.status_code)
        print(response.text)
        print(response.json())

