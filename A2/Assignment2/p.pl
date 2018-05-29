occurrences([],_,0).
occurrences([X|Y],X,N):- occurrences(Y,X,W),N is W + 1.
occurrences([X|Y],Z,N):- occurrences(Y,Z,N),X\=Z.

p([]).
p([X|Y]).
occurrences(p,a,X).
occurrences(p,b,Y).
X==Y.
