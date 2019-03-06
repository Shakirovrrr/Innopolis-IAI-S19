teacher(hamna, intro_to_ai).
teacher(nikita, intro_to_ai).
teacher(dr_succi, networks).
teacher(nikita, networks).

likes(hamna, tea).
likes(nikita, coffee).
likes(dr_succi, coffee).

pair(TA1, TA2) :-
    teacher(TA1, Course),
    teacher(TA2, Course),
    TA1 @> TA2.

pair(TA1, TA2) :-
    likes(TA1, X),
    likes(TA2, X),
    TA1 @> TA2.