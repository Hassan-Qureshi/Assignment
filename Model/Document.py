class Document:
    def __init__(self, id, name, author, description):
        self.id = id
        self.name = name
        self.author = author
        self.description = description

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_name(self):
        return self.author

    def get_description(self):
        return self.description

    def set_id(self, did):
        self.id = did

    def set_name(self, dname):
        self.name = dname

    def set_author(self, dauthor):
        self.author = dauthor

    def set_description(self, ddescription):
        self.description = ddescription
