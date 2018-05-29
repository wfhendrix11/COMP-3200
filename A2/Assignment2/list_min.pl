list_min([X], X) :- !.
list_min([X,Y|Tail], N):-
    ( X > Y ->
        list_min([Y|Tail], N)
    ;
        list_min([X|Tail], N)
    ).
