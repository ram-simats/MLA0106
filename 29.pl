% -------- FACTS --------

fact(sunny).
fact(weekend).

% -------- RULES --------

rule(go_for_walk) :-
    fact(sunny),
    fact(weekend).

rule(play_cricket) :-
    fact(sunny).

rule(stay_home) :-
    fact(rainy).

% -------- FORWARD CHAINING --------

forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    write('New fact derived: '), write(X), nl,
    fail.

forward.
