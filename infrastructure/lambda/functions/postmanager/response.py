import json


class Response:
    def __init__(self, body={}, status_code=200) -> None:
        self.status_code = status_code
        self.body = body
        self.error_message = ""

    def get_default_headers(self):
        return {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT,DELETE",
        }

    def format(self):
        if self.error_message:
            return {
                "isBase64Encoded": False,
                "statusCode": self.status_code,
                "headers": self.get_default_headers(),
                "body": {"error": {"message": self.error_message}},
            }

        data = {
            "isBase64Encoded": False,
            "statusCode": self.status_code,
            "headers": self.get_default_headers(),
            "body": json.dumps(self.body),
        }
        return data
