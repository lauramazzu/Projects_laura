import turtle

screen = turtle.Screen()
screen.title("Italian Regions Game")

image = "italian_region_blank.gif"

screen.addshape(image)

turtle.shape(image)


import pandas
data = pandas.read_csv("Italian_regions_med_sea.csv")
regions_column = data.region.to_list()

guessed_regions = []
#not_guessed_regions = []
while len(guessed_regions) < 24:
    answer = screen.textinput(title=f"{len(guessed_regions)}/24 States Correct", prompt="what's another region's or sea's name?")
    print(answer)
    update_answer = answer.title()
    print(update_answer)
    if answer == "Exit":
        break

    if update_answer in regions_column:
        region_row = data[data.region == update_answer]

        turtle.penup()
        turtle.goto(int(region_row.x), int(region_row.y))
        turtle.write(update_answer, move= False, align = "center")
        guessed_regions.append(update_answer)
        regions_column.remove(update_answer)



data = pandas.DataFrame(regions_column)
print(data)

data.to_csv("regions_to_learn.csv")
