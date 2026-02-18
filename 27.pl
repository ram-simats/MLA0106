edge(a,b).
edge(a,c).
edge(b,d).
edge(b,e).
edge(c,f).
edge(e,g).
edge(f,g).

h(a,5).
h(b,4).
h(c,3).
h(d,6).
h(e,2).
h(f,1).
h(g,0).

goal(g).

bestfs(Start,Path):-
    search([[Start]],Path).

search([[Node|Rest]|_],[Node|Rest]):-
    goal(Node).

search([Path|Paths],Solution):-
    extend(Path,NewPaths),
    append(Paths,NewPaths,Paths1),
    sort_paths(Paths1,SortedPaths),
    search(SortedPaths,Solution).

extend([Node|Rest],NewPaths):-
    findall([NewNode,Node|Rest],
        (edge(Node,NewNode),
        \+ member(NewNode,[Node|Rest])),
        NewPaths).

sort_paths(Paths,Sorted):-
    map_list_to_pairs(get_h,Paths,Pairs),
    keysort(Pairs,SortedPairs),
    pairs_values(SortedPairs,Sorted).

get_h([Node|_],H):-
    h(Node,H).
