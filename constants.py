from datetime import datetime
import os
username = os.environ.get("tareqmjoudeh")
token = os.environ.get("~2AgEd^%DG!Tj")
class Constants:
    def __init__(self):
        self.PIXELA_ENDPOINT = "https://pixe.la/v1/users"
        self.USERNAME = username
        self.TOKEN = token
        self.GRAPH_ID = "graph01"
        self.HEADERS = {
            "X-USER-TOKEN": self.TOKEN
        }
        self.DATE = datetime.now()
        self.TODAY = self.DATE.strftime("%Y%m%d")
        self.YESTERDAY = datetime(year=2021, month=1, day=11)
        self.FORMATTED_YESTERDAY = self.YESTERDAY.strftime("%Y%m%d")

