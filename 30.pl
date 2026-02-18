% -------- FACTS --------

fact(sunny).
fact(weekend).

% -------- RULES --------

go_for_walk :-
    fact(sunny),
    fact(weekend).

play_cricket :-
    fact(sunny).

stay_home :-
    fact(rainy).

% -------- BACKWARD CHAINING --------

prove(Goal) :-
    fact(Goal).

prove(Goal) :-
    call(Goal).
