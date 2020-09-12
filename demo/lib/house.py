''' Defining the House class '''
class House():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._region = data['region']
        self._insignia = data['coatOfArms']
        self._save()

    def _save(self):
        self.all.append(self)

    def get_name(self):
        return self._name
    
    def get_region(self):
        return self._region

    def get_insignia(self):
        return self._insignia
    
    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]