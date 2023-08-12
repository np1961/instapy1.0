import emoji
def printer_sell(menu_display=False, menu_values=312):
    print(emoji.emojize(':left_luggage:')*menu_values if menu_display else emoji.emojize(':left_luggage:')*int(menu_values/3))
