import turtle
import pandas

screen = turtle.Screen()
screen.title("E.U State Game")
image = "blank map.gif"
screen.addshape(image)
screen.setup(width=1000, height=700)
turtle.shape(image)
data = pandas.read_csv("eu_states.csv")
all_countries = data.country.to_list()
all_cities = data.cities.to_list()
guessed_country = []
guessed_cities = []
while len(guessed_country) < 39:

    answer_country = screen.textinput(title=f"{len(guessed_country)}/39 Guess the Country",
                                      prompt="What's another Country?").title()
    if answer_country == 'Exit':
        missing_country = []
        for country in all_countries:
            if country not in guessed_country:
                missing_country.append(country)
        new_data = pandas.DataFrame(missing_country)
        new_data.to_csv("country_to_learn")
        learn_state = screen.textinput(title="You should learn next countries", prompt=f'{new_data}')
        break
    if answer_country in all_countries:
        guessed_country.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(answer_country)

