from datetime import datetime


class Constants:
    def __init__(self):
        self.PIXELA_ENDPOINT = "https://pixe.la/v1/users"
        self.USERNAME = "tareqmjoudeh"
        self.TOKEN = "~2AgEd^%DG!Tj"
        self.GRAPH_ID = "graph01"
        self.HEADERS = {
            "X-USER-TOKEN": self.TOKEN
        }
        self.DATE = datetime.now()
        self.TODAY = self.DATE.strftime("%Y%m%d")
        self.YESTERDAY = datetime(year=2021, month=1, day=11)
        self.FORMATTED_YESTERDAY = self.YESTERDAY.strftime("%Y%m%d")

