gender(tom, male).
gender(clare, female).
gender(kate, female).
gender(alex, male).

parent(tom, kate).
parent(tom, alex).
parent(clare, kate).
parent(clare, alex).

parents(X, Mom, Dad) :-
    gender(Mom, female),
    gender(Dad, male),
    parent(X, Mom),
    parent(X, Dad).

children(X, Child) :-
    parent(Child, X).

siblings(X, Y) :-
    parents(X, Mom, Dad),
    parents(Y, Mom, Dad),
    X \== Y.