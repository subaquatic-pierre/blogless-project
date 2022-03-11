from update import update
from list import list_all
from create import create_post, get_dummy_data

# posts = list_all()
# print(posts)

# data = get_dummy_data()
# create_post(data["title"], data["content"], data["image"])

update(0, title="The New Amazing Title")

new_posts = list_all()
print(new_posts)
