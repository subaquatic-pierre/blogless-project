class PostMeta:
    def __init__(self) -> None:
        pass

    def to_json(self):
        data = {}
        for attr in self._attrs_list:
            value = getattr(self, attr)
            data[attr] = value

        return data

    @staticmethod
    def from_json(attrs: dict):
        post_meta = PostMeta()

        title = attrs.get("title", False)
        id = attrs.get("id", False)

        if not title or id:
            raise Exception("Title and ID must exist on attrs object")

        for key, value in attrs.items():
            setattr(post_meta, key, value)

        attrs_list = []
        for key in attrs.keys():
            attrs_list.append(key)

        post_meta._attrs_list = attrs_list
        return post_meta
