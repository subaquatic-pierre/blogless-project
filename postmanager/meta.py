class PostMeta:
    def __init__(self, id, title, attrs) -> None:
        self.id = id
        self.title = title
        self._attrs_list = []
        self._init_attrs(attrs)

    def to_json(self):
        data = {}
        for attr in self._attrs_list:
            value = getattr(self, attr)
            data[attr] = value

        return data

    def _init_attrs(self, attrs):
        for key in attrs.keys():
            self._attrs_list.append(key)

        for key, value in attrs.items():
            if key == "id" or key == "title":
                continue
            else:
                setattr(self, key, value)

    @staticmethod
    def from_json(attrs: dict):
        title = attrs.get("title", None)
        id = attrs.get("id", None)

        if title == None:
            raise Exception("Title attrs object")

        if id == None:
            raise Exception("Title attrs object")

        post_meta = PostMeta(id, title, attrs)

        return post_meta
