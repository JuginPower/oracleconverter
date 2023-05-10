import re
from services import search_replace


class ConstraintTranslator:

    def __init__(self, orig_line):

        self._orig_line = orig_line
        self._task = None

    def from_oracle_to_mysql(self):

        self._task = "otom"
        
        if re.search(r'UNIQUE\s*\(.+\)', self._orig_line):
            self._translate_unique()

        if re.search(r'PRIMARY KEY\s*\(.+\)', self._orig_line):
            self._translate_primary_key()

        if re.search(r'FOREIGN KEY\s*\(.+\)', self._orig_line):
            self._translate_primary_key()
        
        if re.search(r'CHECK\s*\(.+\)', self._orig_line):
            self._translate_check()

        if re.search(r'"\w+"\s*(\w+|\w+\(.+\))\s*CONSTRAINT\s*.+', self._orig_line):
            self._translate_default()
    
        self._orig_line = search_replace(self._orig_line)
        return self._orig_line

    def _translate_unique(self):
        if self._task == "otom":
            self._orig_line = re.sub(r'"', '', self._orig_line)

    def _translate_primary_key(self):
        if self._task == "otom":
            self._orig_line = re.sub(r'"', '', self._orig_line)

    def _translate_foreign_key(self):
        if self._task == "otom":
            self._orig_line = re.sub(r'"', '', self._orig_line)

    def _translate_check(self):
        if self._task == "otom":
            self._orig_line = re.sub(r'"', '', self._orig_line)

    def _translate_default(self):
        if self._task == "otom":
            self._orig_line = self._orig_line.replace("DATE CONSTRAINT", "DATETIME CONSTRAINT")
            self._orig_line = re.sub("CONSTRAINT", "DEFAULT", self._orig_line)
            self._orig_line = self._orig_line.replace('"', '', 2) # Weil DEFAULT Namen Anführungszeichen brauchen.

    def _translate_index(self):
        pass

        