import json


class Response:
    def __init__(self, body, status_code=200) -> None:
        self.status_code = status_code
        self.body = body

    def get_default_headers(self):
        return {"cool": "coolio"}

    def to_json(self):
        data = {
            "isBase64Encoded": False,
            "statusCode": self.status_code,
            "headers": self.get_default_headers(),
            "body": json.dumps(self.body),
        }
        return data
