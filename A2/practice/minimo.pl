minimo([X], X) :- !.
minimo([X,Y|Tail], N):-
    ( X > Y ->
        minimo([Y|Tail], N)
    ;
        minimo([X|Tail], N)
    ).
