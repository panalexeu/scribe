import os


class Repository:

    def __init__(self):
        self.mongodb_url = os.environ.get('MONGODB_URL')
