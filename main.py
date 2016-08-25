import webapp2
from ceaser import encrypt
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>first assignment</title>
    <style type="text/css">
        form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
    </style>
</head>
<body>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):

        rotation = """
        <form action="/answer" method="post">
            <label for="rotation1">Rotate By:</label>
                <input name="rotation1" type="text" value="0">
                <p class="error"></p>
            <textarea type="text" name="text1"></textarea>
            <br>
            <input type="submit">
        </form>
        """

        self.response.write(page_header + rotation + page_footer)

class Answer(webapp2.RequestHandler):
    def post(self):
        text = self.request.get("text1")
        rotation = self.request.get("rotation1")
        answer2 = encrypt(text, int(rotation))

        rotationDone = """
        <form action="/answer" method="post">
            <label for="rotation1">Rotate By:</label>
                <input type="text" name="rotation1" value='"""+ rotation + """'></input>
                <p class="error"></p>
            <textarea type="text" name="text1">""" + answer2 + """</textarea>
            <br>
            <input type="submit"></input>
        </form>
        """


        self.response.write(page_header + rotationDone + page_footer)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/answer', Answer)
], debug=True)
