listnama = ["Ashley", "Mariyah", "Soot", "Maizie", "Frost", "Estelle", "Marie", "Maddie", "Salmon", "Alyson", "Pubbles",
            "Angelou", "Mittens", "Dessie", "Olivia", "Socksy", "Cinnamon", "Catie"]

listnamaie = list(map(lambda x: x.__contains__("ie"), listnama))

for x in range(0, len(listnama)):
    if listnamaie[x]:
        print(listnama[x])
