from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>
<html>
  <head>
    <title>Web Caesar</title>
    <style>
      form {{
        background-color: #eee;
        padding: 20px;
        margin: 0 auto;
        width: 540px;
        font: 16px sans-serif;
        border-radius: 10px;
      }}
      textarea {{
        margin: 10px 0;
        width: 540px;
        height: 120px;
      }}
    </style>
  </head>
  <body>
    <form method="post">
      <label>Rotate by:
        <input type="number" value="0" name="rot">
      </label>
      <br>
      <textarea name="text">{0}</textarea>
      <input type="submit">
    </form>
  </body>
</html>
"""

@app.route("/")
def index():
  return form.format("")

@app.route("/", methods = ["POST"])
def encrypt():
  rotate = int(request.form.get("rot"))
  message = request.form.get("text")
  return form.format(rotate_string(message, rotate))
  
app.run()
