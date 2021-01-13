import requests
from constants import Constants
constant = Constants()


class EditGraph:
    def __init__(self):
        super().__init__()
        self.constant = constant
        self.endpoint = f"{constant.PIXELA_ENDPOINT}" \
                        f"/{constant.USERNAME}/graphs/{constant.GRAPH_ID}" \
                        f"/{constant.TODAY}"

    def update_response(self):
        # TODO: Update an entry in the graphs:
        response = requests.put(
            headers=self.constant.HEADERS,
            url=self.endpoint,
            json={
                "quantity": input("Enter a new coding hours: ")
            }
        )
        response.raise_for_status()
        print(response.status_code)
        print(response.text)
