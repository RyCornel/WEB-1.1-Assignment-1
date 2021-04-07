from flask import Flask,redirect,url_for,render_template,request
import random

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
    str_num1 = str(num1)
    str_num2 = str(num2)

    if str_num1.isdigit() & str_num2.isdigit():
        str_num1 = int(num1)
        str_num2 = int(num2)
        answer = str_num1 * str_num2
        print(f"{num1} times {num2} is {answer}!")
        return answer
    else:
        wrongAnswer = f"Invalid input. Please try again by entering two numbers!"
        print(wrongAnswer)
        return wrongAnswer


@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
  nStr = str(n)
  
  if nStr.isdigit():
      nStr = int(n)

      for i in word:
        space_word = word + " "
      print(space_word * n)
      return space_word * n 

   

@app.route('/dicegame/')
def dicegame():
    roll = random.randint(1,6)

    if roll == 6:
      print(f"You rolled {roll}! You Won!")
    else:
      print(f"You rolled {roll}. Sorry, you lost.")
    




if __name__ == '__main__':
    app.run(debug=True)


