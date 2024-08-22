class todo:
    def __init__(self, code_id: int, title: str, description: str, completed: bool):
            self.code_id = code_id
            self.title = title
            self.description = description
            self.completed = False
            self.tags = []