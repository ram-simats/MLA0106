% -------- CHECK VOWEL --------

is_vowel(a).
is_vowel(e).
is_vowel(i).
is_vowel(o).
is_vowel(u).

is_vowel('A').
is_vowel('E').
is_vowel('I').
is_vowel('O').
is_vowel('U').

% -------- COUNT VOWELS --------

count_vowels([], 0).

count_vowels([H|T], Count) :-
    is_vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.

count_vowels([H|T], Count) :-
    \+ is_vowel(H),
    count_vowels(T, Count).
