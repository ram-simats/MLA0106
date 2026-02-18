% -------- FACTS --------

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grapes, green).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(guava, green).
fruit_color(cherry, red).

% -------- RULE --------

get_fruit_color(Fruit, Color) :-
    fruit_color(Fruit, Color).
