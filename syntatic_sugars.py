class sstr(str):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value[::-1]

    def __len__(self):
        return ord(self.value[0])

    def __repr__(self):
        return 1

    def __add__(self, other):
        return self.value + 'abacate'