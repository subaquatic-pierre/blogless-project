class MetaData:
    def __init__(self, attrs) -> None:
        self.attributes = ["id"]
        self.attributes += attrs

    def to_json(self):
        data = {}
        for attr in self.attributes:
            value = self.__getattribute__(attr)
            data.__setitem__(attr, value)
        return data


class PostMetaData(MetaData):
    def __init__(self, post_id, title, timestamp, template="blog") -> None:
        super().__init__(["title", "timestamp", "template"])

        self.id = post_id
        self.title = title
        self.timestamp = timestamp
        self.template = template
