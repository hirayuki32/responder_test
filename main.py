import responder
  
api = responder.API()

@api.route("/hello.html")
def hello_html(req, resp):
    my_name = "hirayuki"  # 追記
    resp.html = api.template('index.html', name=my_name)  # 追記

api.run(port=3000)
