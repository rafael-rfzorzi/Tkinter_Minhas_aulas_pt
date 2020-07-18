from modulos import *

class Validadores:
    def validate_entry2(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100
    def validate_entry4(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 10000

    def validate_entry4float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 5
    def validate_entry9float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 10