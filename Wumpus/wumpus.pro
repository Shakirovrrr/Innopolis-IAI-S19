:- ['Wumpus\\game_map.pro'].

smell(X, Y) :-
	place(wumpus, X-1, Y);
	place(wumpus, X, Y-1);
	place(wumpus, X, Y+1);
	place(wumpus, X+1, Y).
