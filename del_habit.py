import requests
from constants import Constants

constant = Constants()


class DelGraph:
    def __init__(self):
        self.constant = constant
        self.endpoint = f"{constant.PIXELA_ENDPOINT}/{constant.USERNAME}" \
                        f"/graphs/{constant.GRAPH_ID}/{constant.FORMATTED_YESTERDAY}"

    def del_response(self):
        response = requests.delete(
            headers=self.constant.HEADERS,
            url=self.endpoint
        )
        response.raise_for_status()
        print(f"""
        {response.status_code}
        {response.text}
        """)
