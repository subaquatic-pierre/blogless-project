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
            if key == "id" or "title":
                pass
            setattr(self, key, value)

    @staticmethod
    def from_json(attrs: dict):
        title = attrs.get("title", False)
        id = attrs.get("id", False)

        if not title or id:
            raise Exception("Title and ID must exist on attrs object")

        post_meta = PostMeta(id, title, attrs)
        return post_meta
