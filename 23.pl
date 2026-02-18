% -------- FACTS --------

male(john).
male(paul).
male(mike).
male(david).

female(mary).
female(linda).
female(susan).
female(anna).

parent(john, paul).
parent(mary, paul).

parent(john, linda).
parent(mary, linda).

parent(paul, mike).
parent(susan, mike).

parent(paul, anna).
parent(susan, anna).

parent(linda, david).

% -------- RULES --------

father(X,Y):- parent(X,Y), male(X).

mother(X,Y):- parent(X,Y), female(X).

sibling(X,Y):- parent(Z,X), parent(Z,Y), X\=Y.

brother(X,Y):- sibling(X,Y), male(X).

sister(X,Y):- sibling(X,Y), female(X).

grandparent(X,Y):- parent(X,Z), parent(Z,Y).

grandfather(X,Y):- grandparent(X,Y), male(X).

grandmother(X,Y):- grandparent(X,Y), female(X).

ancestor(X,Y):- parent(X,Y).
ancestor(X,Y):- parent(X,Z), ancestor(Z,Y).
