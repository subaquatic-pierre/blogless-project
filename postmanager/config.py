from botocore.session import Session
from botocore.config import Config


def create_session(credentials={}):
    # Add credentials to session
    return Session()


def create_client(session, config={}):
    default_config = Config(
        connect_timeout=5, read_timeout=60, retries={"max_attempts": 2}
    )
    client = session.create_client("s3", config=default_config)
    return client


def setup_client(credentials={}, client_config={}):
    session = create_session()
    client = create_client(session)
    return client
