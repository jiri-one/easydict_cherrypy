import difflib
import re
# imports from my other files with classes and methods
from settings import eng_cze, where

def db_search(language, text, fulltext):
    if fulltext == False: 
        text = rf'\b{text}\b'
    results = eng_cze.search(where(language).search(text, flags=re.IGNORECASE))
    results_with_matchratio = []
    for result in results:
        ratio = difflib.SequenceMatcher(None, result[language], text).ratio()
        results_with_matchratio.append([result, ratio])
    return sorted(results_with_matchratio, key=lambda x: x[1], reverse=True)

class CreateHtml:
    def finish_html(self, results):
        self.html_string = ""    
        for row in results:
            self.html_string = self.html_string + self.create_html(row[0])

        return self.html_string
            
    def create_html(self, row):
        if "notes" in row.keys():
            self.notes =  ", " + row["notes"]
        else:
            self.notes = ""
        if "special" in row.keys():
            self.special = ", "  + row["special"]
        else:
            self.special = ""        
    
        html = f"""
        <p>{row["eng"]}</b>
        <br>&emsp;{row["cze"]}{self.notes}{self.special}<hr />
        </p>
        """
        return html
