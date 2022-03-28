import sys
import json
from utils import create_event_and_context, print_response
from api_methods import get, list, post, put, delete


def run_api(method_list, post_id=0):
    if "list" in method_list:
        list_event, context = create_event_and_context("/blog", mock_bucket=False)
        list_response = list(list_event, context)
        print_response(list_response)

    if "get" in method_list:
        get_event, context = create_event_and_context(
            f"/blog/{post_id}", mock_bucket=False
        )
        get_response = get(get_event, context)
        print_response(get_response)

    if "post" in method_list:
        post_body = json.dumps(
            {
                "metaData": {"title": "Awesome First Post"},
                "content": {
                    "Heading": "The best first post",
                    "Paragraph": "Some text to go with the best first post",
                },
            }
        )
        post_event, context = create_event_and_context(
            "/blog", body=post_body, mock_bucket=False
        )
        post_response = post(post_event, context)
        print_response(post_response)


if __name__ == "__main__":
    args = sys.argv
    del args[0]

    if len(args) == 0:
        method_list = ["list"]
        run_api(method_list)

    # GET METHOD
    elif args[0] == "get":
        if not isinstance(int(args[1]), int):
            print("Get must have ID")
        else:
            post_id = args[1]
            method_list = ["get"]
            run_api(method_list, post_id)

    # POST METHOD
    elif args[0] == "post":
        run_api(["post"])

    # PUT METHOD
    elif args[0] == "put":
        if not isinstance(int(args[1]), int):
            print("Put must have ID")
        else:
            post_id = args[1]
            method_list = ["put"]
            run_api(method_list, post_id)

    # LIST METHOD
    elif args[0] == "list":
        method_list = ["list"]
        run_api(method_list)

    # DELETE METHOD
    elif args[0] == "delete":
        if not isinstance(int(args[1]), int):
            print("Delete must have ID")
        else:
            post_id = args[1]
            method_list = ["delete"]
            run_api(method_list, post_id)

    else:
        print("No method run")
