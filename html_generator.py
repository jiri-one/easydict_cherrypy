import difflib
import re
# imports from my other files with classes and methods
from settings import cwd, cwd_static, eng_cze, where

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
    default_html = f"""
    <!DOCTYPE html>
    <html>
    <head><link rel="stylesheet" href="https://unpkg.com/purecss@2.0.3/build/pure-min.css" integrity="sha384-cg6SkqEOCV1NbJoCu11+bm0NvBRc8IYLRGXkmNrqUBfTjmMYwNKPWBTIKyw9mHNJ" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="static/css/easydict_styles.css">
    <meta charset="utf-8">
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.8.9/brython.min.js">
    </script>
    </head>
    <body style="background-color:#2d2d2d;color:#000000;" onload="brython(debug=1)">
    <script type="text/python">
    from browser import document
    document <= "Hello !"
    </script>
    <p style="font-size: 30px;text-align:center;"><b>Welcome to EasyDict (web version)</b></p>
    <p style="text-align:center;"><img src="static/images/ed_icon.png"></p>
    <p style="font-size: 22px;text-align:center;">The first open source translator which is completely open with dictionary data too.</p>
    <form class="pure-form" method="post" action="/">
    <fieldset>
    <label for="checkbox-radio-option-two">
    <input type="radio" id="checkbox-radio-option-two" name="optionsRadios" value="option1" checked="" />Whole word</label>
    <label for="checkbox-radio-option-three">
    <input type="radio" id="checkbox-radio-option-three" name="optionsRadios" value="option2" />Fulltext</label>
    </fieldset>
    <input type="text" class="pure-input-rounded" name="searched_text"/>
    <button type="submit" class="pure-button pure-button-primary" id="button_search">Search</button>
    </form>
    </br>
    </br>
    </body>
    </html>"""    
    
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
        <p style="font-size: 22px"><b><span style="color: #ffffff;">{row["eng"]}</span></b>
        <br>&emsp;<span style="color: #ffffff;">{row["cze"]}{self.notes}{self.special}</span>
        </p>
        """
        return html

#vystup = CreateHtml(mydoc)
#print(vystup)

#html = f"""
#<p style="font-size: 22px"><b>{row["eng"]}</b>
#<br>&emsp;{row["cze"]}
#&emsp;{row["notes"]}
#&emsp;{row["special"]}</p>"""

new_html = """
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="static/css/easydict_styles.css">
    <meta charset="utf-8">
    <script src="https://cdn.jsdelivr.net/npm/brython@3.8.9/brython.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/brython@3.8.9/brython_stdlib.js"></script>
</head>

<body style="background-color:#2d2d2d;color:#000000;" onload="brython(1)">
    <script type="text/python" src="static/brython/ed_ajax.py" />
    </script>
    <div class="grid-container">
        <div class="head">head</div>
        <div class="results" id="results" style="overflow-y:scroll; overflow-x:hidden; height:640px;">The results of search will be here:</div>
        <div class="search_form">
            <fieldset>
                <input type="text" name="searched_text" size="10" maxlength="20" id="searched_text" />
                <button type="submit" id="button_search">Search</button>
                <select id="language">
                    <option>English</option>
                    <option>Czech</option>
                </select>
            </fieldset>
            <fieldset>
                <label for="checkbox-radio-option-two">
                    <input type="radio" id="checkbox-radio-option-two" name="optionsRadios" value="option1" checked="" />Whole word</label>
                <label for="checkbox-radio-option-three">
                    <input type="radio" id="checkbox-radio-option-three" name="optionsRadios" value="option2" />Fulltext</label>
            </fieldset>

        </div>
        <div class="footer">footer</div>
        <div class="body">body</div>
        <div class="rest"></div>
    </div>
</body>

</html>
"""