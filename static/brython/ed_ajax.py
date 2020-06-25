from browser import document, ajax, markdown

def on_complete(req):
	if req.status == 200 or req.status == 0:
		document["results"].html = req.text
	else:
		document["results"].html = "There is some error: " + req.text

def ajax_post(button_search):
	document["results"].html = "Loading..."
	searched_text = document["searched_text"]
	ajax.post("/searchengine", headers={"Content-Type": "application/x-www-form-urlencoded"}, data={'searched_text': searched_text.value}, oncomplete=on_complete)
	
button_search = document["button_search"]
button_search.bind("click", ajax_post)