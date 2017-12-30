import falcon
import controller as c

app = falcon.API()

app.add_route("/", c.HelloController())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()