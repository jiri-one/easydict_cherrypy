from browser import document, ajax, markdown

def on_complete(req):
	if req.status == 200 or req.status == 0:
		document["results"].html = req.text
	else:
		document["results"].html = "There is some error: " + req.text

def ajax_post(button_search):
	document["results"].html = "Loading..."
	language = document["language"]
	searched_text = document["searched_text"]
	fulltext = document["fulltext"]
	ajax.post("/searchengine",
			  headers={"Content-Type": "application/x-www-form-urlencoded"},
			  data={"language": language.value,
					"searched_text": searched_text.value,
					"fulltext": fulltext.checked
					},
			  oncomplete=on_complete)

def hit_enter(ev):
	if ev.keyCode == 13:
		ajax_post(None)

def test(button):
	#print(button.target.id)
	#print(button.option)
	print(document["language"].value)
	#print(button.returnValue)
	
document["button_search"].bind("click", ajax_post)
document["searched_text"].bind("keypress", hit_enter)
document["whole_word"].checked = True
document["language"].bind("click", test)

#document["whole_word"].target.checked = True
#fulltext = document["fulltext"]
#fulltext.bind("click", test)
#fulltext.checked = True

#document["whole_word"].bind("click", test)
