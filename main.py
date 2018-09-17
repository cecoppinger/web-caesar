from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>
<html>
  <head>
    <title>Web Caesar</title>
  </head>
  <body>
    <form>
      <label>Rotate by:
        <input type="number" value="0" name="rotate-by">
      </label>
      <textarea name="message"></textarea>
    </form>
  </body>
</html>
"""

@app.route("/")
def index():
  return form

app.run()
