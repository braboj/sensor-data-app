class BackendError(Exception):

    def __init__(self, message, context=None):
        self.message = message
        self.context = context
        super().__init__(self.message)

    def __str__(self):

        context = f"({self.context})" if self.context else ""
        return f"{self.__class__.__name__}: {self.message} {context}"

    def __repr__(self):
        return str(self)


def demo():
    try:
        raise BackendError(
            message=f"",
            context=f"expected {int.__name__}, got {type(1.0).__name__}"
        )
    except BackendError as e:
        print(e)


if __name__ == '__main__':
    demo()