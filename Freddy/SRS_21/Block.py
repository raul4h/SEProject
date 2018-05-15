class Block:

    def __init__(self, name, req):
        self.blockName = name
        self.required = req

    def Name(self):
        return self.blockName + ", req: " + self.required