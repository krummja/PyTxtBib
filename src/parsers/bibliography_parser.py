import re
from scholarly import scholarly as sch


class BibliographyParser:

    def __init__(self, data):
        self.data = data
