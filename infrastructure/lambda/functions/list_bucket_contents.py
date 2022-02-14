import boto3


def handler(event, context):
    """
    Accepts an action and a number, performs the specified action on the number,
    and returns the result.

    :param event: The event dict that contains the parameters sent when the function
                  is invoked.
    :param context: The context in which the function is called.
    :return: The result of the specified action.
    """

    s3 = boto3.resource("s3")
    bucket = s3.Bucket("serverless-blog-contents")

    response = {"result": "this is the reponse"}
    return response
