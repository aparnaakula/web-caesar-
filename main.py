from caesar import rotate_string
from flask import Flask, request

app=Flask(__name__)

app.config['DEBUG']= True

form="""

<!DOCTYPE html>

<html>

    <head>

        <style>

            form {{

                background-color: red;

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

           

                <label for="rot">Rotate by:</label>

                <input type="text" name="rot" value="0">           

             <br>

            <textarea type="text" name="text">{0}</textarea>

          <br>

            <input type="submit">

        </form>

    </body>

</html>

"""

@app.route("/", methods=['POST'])

def encrypt(): 

    

   rot=int(request.form['rot'])

   text=request.form['text']

      
   encrypted_string=rotate_string(text,rot)

  

   return form.format(encrypted_string)

    
@app.route("/")

def index():

    return form

app.run()