class CustomExceptions(AssertionError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def call(message):
        return AssertionError(message)