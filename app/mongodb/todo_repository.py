from .repository import Repository


class ToDoRepository(Repository):

    def __init__(self):
        self.collection = self.db.get_collection('to-do')

    def create(self):
        pass

    def read(self):
        pass

    def read_all(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass