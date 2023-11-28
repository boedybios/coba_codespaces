import falcon


class ObjRequestClass:
    def on_get(self, req, resp):
        content = {"name": "Jono", "role": "ds lead", "company": "tiket.com"}
        # resp.body = json.dumps(content)
        resp.media = content


api = falcon.App()
api.add_route("/test", ObjRequestClass())
