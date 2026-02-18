% -------- INITIAL STATE --------
% state(MonkeyPosition, MonkeyStatus, BoxPosition, HasBanana)

initial_state(state(at_door, on_floor, at_window, no)).

% -------- GOAL STATE --------
goal_state(state(_, _, _, yes)).

% -------- ACTION RULES --------

% Move monkey from one position to another
move(state(X, on_floor, B, H),
     go(X, Y),
     state(Y, on_floor, B, H)) :-
     X \= Y.

% Push box (monkey must be on floor and at same position as box)
move(state(X, on_floor, X, H),
     push(X, Y),
     state(Y, on_floor, Y, H)) :-
     X \= Y.

% Climb the box
move(state(X, on_floor, X, H),
     climb,
     state(X, on_box, X, H)).

% Grasp banana (banana is at middle)
move(state(middle, on_box, middle, no),
     grasp,
     state(middle, on_box, middle, yes)).

% -------- SEARCH STRATEGY --------

solve :-
    initial_state(State),
    plan(State, []).

plan(State, _) :-
    goal_state(State),
    write('Monkey got the banana!'), nl.

plan(State, Visited) :-
    move(State, Action, NewState),
    \+ member(NewState, Visited),
    write(Action), nl,
    plan(NewState, [NewState|Visited]).
