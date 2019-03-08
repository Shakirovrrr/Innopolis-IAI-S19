:- ['Wumpus\\game_map.pro'].

is_neighbour(What, X, Y) :-
	place(What, WX, WY),
	(X is WX-1, Y is WY;
	X is WX, Y is WY-1;
	X is WX, Y is WY+1;
	X is WX+1, Y is WY).

is_smell(X, Y) :-
	is_neighbour(wumpus, X, Y).

is_breeze(X, Y) :-
	is_neighbour(pit, X, Y).