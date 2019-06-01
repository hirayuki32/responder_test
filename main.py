import responder
import time

api = responder.API()


@api.route("/hello.html")
async def hello_html(req, resp):
    user = "hirayuki"
    person_you_chose = ""
    try:
        data = await req.media()
        person_you_chose = data["name"]
    except:
        pass
    resp.html = api.template('index.html', user=user,
                             person_you_chose=person_you_chose)

api.run(port=3000)
