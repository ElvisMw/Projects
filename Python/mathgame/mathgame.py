import turtle
import random
import time
import winsound
import csv

# Function to read questions from a CSV file
def read_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            questions.append(row)
    return questions

# Function to draw a star shape
def draw_star(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("gold")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(50)
        turtle.right(144)
    turtle.end_fill()

# Function to play a correct answer sound
def play_correct_sound():
    try:
        winsound.PlaySound("correct_answer.wav", winsound.SND_ASYNC)
    except:
        print("Unable to play sound. Please make sure 'correct_answer.wav' is in the same directory.")

# Function to display a random positive message
def display_positive_message():
    positive_messages = [
        "Great job!",
        "Fantastic!",
        "You're a math superstar!",
        "Amazing!",
        "You nailed it!",
        "Keep up the good work!",
        "You're unstoppable!",
        "Well done!",
        "Brilliant!"
    ]
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 150)
    turtle.color("blue")
    turtle.write(random.choice(positive_messages), align="center", font=("Arial", 20, "normal"))
    turtle.hideturtle()
    time.sleep(1.5)
    turtle.clear()

# Function to generate a math question from the list of questions
def generate_question(questions, grade, level):
    filtered_questions = [q for q in questions if 'grade' in q and 'level' in q and 'operation' in q and 'num1' in q and 'num2' in q and 'solution' in q]
    selected_question = random.choice(filtered_questions)
    question = f"{selected_question['num1']} {selected_question['operation']} {selected_question['num2']}"
    return question, int(selected_question['solution'])

# Function to draw colorful buttons with animation
def draw_animated_button(x, y, text, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black", color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x + 50, y + 30)
    turtle.pendown()
    turtle.color("black")
    turtle.write(text, align="center", font=("Arial", 14, "normal"))

# Function to display stars based on the player's score
def display_stars(score):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 180)
    turtle.color("yellow")

    for _ in range(score):
        draw_star(-50 + _ * 30, 180)

    turtle.hideturtle()

# Function to draw the countdown timer
def draw_countdown_timer(timer):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, -150)
    turtle.color("red")
    turtle.write(f"Time Left: {timer} seconds", align="center", font=("Arial", 16, "normal"))
    turtle.hideturtle()

# Main game function
def play_math_game(questions_file='questions.csv'):
    turtle.speed(2)
    turtle.bgcolor("lightblue")
    turtle.title("Math Game for Kids")

    print("Welcome to the Math Game!")

    # Read questions from the CSV file
    questions = read_questions(questions_file)

    for grade in range(1, 4):
        for level in range(1, 201):
            turtle.clear()

            draw_animated_button(-150, -50, "+", "lightgreen")
            draw_animated_button(0, -50, "-", "lightcoral")
            draw_animated_button(150, -50, "*", "lightyellow")

            operation = turtle.textinput("Choose Operation", "Select an operation (+, -, *): ")
            if operation not in ['+', '-', '*']:
                turtle.clear()
                turtle.write("Invalid operation. Please try again.", align="center", font=("Arial", 14, "normal"))
                time.sleep(2)
                continue

            turtle.clear()

            turtle.color("purple")
            turtle.penup()
            turtle.goto(0, 120)
            turtle.write("Get ready!", align="center", font=("Arial", 16, "normal"))
            time.sleep(1)

            turtle.clear()

            draw_star(0, 180)
            question, correct_answer = generate_question(questions, grade, level)
            turtle.goto(0, 120)
            turtle.color("purple")
            turtle.write(question, align="center", font=("Arial", 16, "normal"))

            attempts = 0
            hints_used = 0

            while True:
                timer = 5  # Initial countdown timer value
                start_time = time.time()

                while timer > 0:
                    draw_countdown_timer(timer)
                    time.sleep(1)
                    turtle.clear()
                    timer -= 1

                turtle.clear()

                user_answer = int(turtle.textinput("Math Question", "Your answer:"))

                if user_answer == correct_answer:
                    display_positive_message()
                    play_correct_sound()
                    break  # Move to the next level
                else:
                    turtle.clear()
                    turtle.write(f"Oops! The correct answer was {correct_answer}.", align="center", font=("Arial", 14, "normal"))
                    time.sleep(2)

                    attempts += 1

                    if attempts == 2:
                        turtle.clear()
                        turtle.write("Hint: Try to break down the numbers and use smaller calculations.", align="center", font=("Arial", 14, "normal"))
                        hints_used += 1
                        time.sleep(3)

            display_stars(hints_used)  # Display stars based on the number of hints used

    turtle.clear()
    turtle.hideturtle()
    turtle.bgcolor("lightgreen")

    turtle.write("Congratulations! You completed all levels.", align="center", font=("Arial", 18, "normal"))
    turtle.done()

if __name__ == "__main__":
    play_math_game()
