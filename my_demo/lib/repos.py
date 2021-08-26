class Repos():
    all = []

    def __init__(self, data):
        self._name = data['name']
        # self._id = id
        self._private = data['private']
        self._has_wiki = data['has_wiki']
        self._save()
    
    def _save(self):
        self.all.append(self)
    
    @property
    def name(self):
        return self._name

    # @property
    # def id(self):
    #     return self.id

    @property
    def private(self):
        return self._private

    @property
    def has_wiki(self):
        return self._has_wiki

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]