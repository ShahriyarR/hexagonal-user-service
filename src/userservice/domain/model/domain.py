from readonce import ReadOnce


class Password(ReadOnce):
    def __init__(self, password: str) -> None:
        super().__init__()
        self.add_secret(password)
