import responder
import time

api = responder.API()


@api.route("/hello.html")
def hello_html(req, resp):
    my_name = "hirayuki"
    resp.html = api.template('index.html', name=my_name)

@api.route("/incoming")
async def receive_incoming(req, resp):
    data = await req.media()
    resp.html = api.template('index.html', name=data)
    print(data)

api.run(port=3000)
