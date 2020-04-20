class Validation():
    """
    Validate input data

    return: bool
    """

    def __init__(self, data, token):
        self.data = data
        self.token = token

    def valdation_data(self):
        if not "input" in self.data.keys():
            return False

        for i in self.data["input"].split():

            if not i.strip().lower() in self.token.word_index:
                return False

        return True
