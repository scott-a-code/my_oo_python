from .api import fetch_repos
from .repos import Repos

class CLI():
    def __init__(self):
        self._user_input_git = ""
        self._user_input_id = None
    
    def start(self):
        self._user_input_git = input(f"Enter you github username to see a list of your repos: ")
        fetch_repos(self._user_input_git)
        self.all_repo_menu()
    
    def all_repo_menu(self):
        for idx, repo in enumerate(Repos.all, start=1):
            print(f"{idx}. {repo.name} \n")
        self.get_user_choice()
    
    def get_user_choice(self):
        try:
            self._user_input_id = input(f"Enter the number of a listed repo to see more details: ")
            if self._user_input_id == 'exit': 
                return self.goodbye()
            if not self.valid_input(self._user_input_id):
                raise ValueError
            self.show_repo()
            self.get_user_choice()
        except ValueError:
            print('urgh, can\'t you follow insturctions! invalid input or enter a NUMBER within the range this time!')
            self.all_repo_menu()

    def show_repo(self):
        repos = Repos.find_by_input(self._user_input_id)
        print(f"This repo is named: {repos.name}")
        print(f"This repos privacy status is: {repos.private}")
        print(f"Does this repo have a wiki: {repos.has_wiki}")
    
    @staticmethod
    def goodbye():
        print("Later tater")

    @staticmethod
    def valid_input(t):
        return int(t) > 0 and int(t) <= len(Repos.all)

if __name__ == '__main__':
    app = CLI()