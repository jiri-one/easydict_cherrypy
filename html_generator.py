from difflib import SequenceMatcher
# imports from my other files with classes and methods
from settings import eng_cze, where, default_db, mydict, conn, r

class Search(object):
    def __init__(self, language, text, fulltext):
        self.language = language
        self.text = text
        if fulltext == False:
            #self.searched_text = rf"(?i)(^|[, ?.!]){text}([, ?.!]|$)"
            #self.searched_text = rf"(?i)([ \-',]|^){text}([ \-',]|$)"
            self.searched_text = rf"(?i)(?:^|[[:punct:]]| ){text}(?:[[:punct:]]| |$)"
        else:
            self.searched_text = rf'(?i){text}'
        if default_db == "rethinkdb":
            self.search_results = list(mydict.filter(lambda words: words[self.language].match(self.searched_text)).run(conn))
        if default_db == "tinydb":
            self.search_results = eng_cze.search(where(self.language).search(self.searched_text))
        
        self.results = self.finalize_search()        
    
    def finalize_search(self):
        results_with_matchratio = []
        for result in self.search_results:
            ratio = SequenceMatcher(None, result[self.language], self.text).ratio()
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
