class College:
    def __init__(self, ccode, cname):
        self._ccode = ccode
        self._cname = cname


    def display_college(self):
        # Returning values in a more readable format
        return f"College Code: {self._ccode}, College Name: {self._cname}"
