membr(H, [H | _]).
membr(X, [_ | T]) :-
	membr(X, T).

len([], 0).
len([_ | T], N) :-
	len(T, M),
	N is M + 1.