# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch18.html#:-:text=Things%20to%20Do

# Skipped b/c more advanced and not presently needed.

# 18.1 If you haven’t installed flask yet, do so now. This will also install werkzeug, jinja2, and possibly other packages.

# 18.2 Build a skeleton website, using Flask’s debug/reload development web server. Ensure that the server starts up for hostname localhost on default port 5000. If your computer is already using port 5000 for something else, use another port number.

# 18.3 Add a home() function to handle requests for the home page. Set it up to return the string It's alive!.

# 18.4 Create a Jinja2 template file called home.html with the following contents:

# <html>
# <head>
# <title>It's alive!</title>
# <body>
# I'm of course referring to {{thing}}, which is {{height}} feet tall and {{color}}.
# </body>
# </html>
# 18.5 Modify your server’s home() function to use the home.html template. Provide it with three GET parameters: thing, height, and color.