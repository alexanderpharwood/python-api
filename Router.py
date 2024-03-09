from controllers.HomeController import HomeController


class Router:
    def __init__(self, app):
        self.app = app
        self.HomeController = HomeController()

    def boot(self):
        self.app.route("/")(self.index)

    def index(self):
        # Any middleware
        return self.HomeController.index()
