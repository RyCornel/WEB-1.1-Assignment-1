from flask import Flask 

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user. """
    return "Are you there, world? It's me, Ducky!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal"""
    return f"Wow, {users_animal} is my favorite animal, too!"

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f"How did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f"I once had a {noun} that used to {adjective} a lot."

@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
  num1 = int(num1)
  num2 = int(num2) 
  answer = int(num1 * num2)

  if answer != int(num1 * num2):
    return f"Invalid input. Please try again by entering two numbers!"  
  else :
    return f"{num1} times {num2} is {answer}!"

    

if __name__ == '__main__':
    app.run(debug=True)

