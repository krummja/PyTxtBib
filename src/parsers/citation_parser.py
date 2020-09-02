import re
from scholarly import scholarly as sch
import pylatex as tex


class CitationParser:

    def __init__(self, data):
        self.data = data
