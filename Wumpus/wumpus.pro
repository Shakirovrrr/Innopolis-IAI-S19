:- ['Wumpus\\game_map.pro'].

:- dynamic([agent_path/1]).

% --------------------- Helpers ---------------------

agent_pos(Pos) :-
	agent_path([Pos | _]).

prev_pos(Pos) :-
	agent_path([_, Pos | _]).

is_neighbour(What, [X, Y]) :-
	place(What, [WX, WY]),
	(X is WX-1, Y is WY;
	X is WX, Y is WY-1;
	X is WX, Y is WY+1;
	X is WX+1, Y is WY).

is_smell([X, Y]) :-
	is_neighbour(wumpus, [X, Y]).

on_smell :-
	agent_pos(Pos),
	is_smell(Pos).

is_breeze([X, Y]) :-
	is_neighbour(pit, [X, Y]).

on_breeze :-
	agent_pos(Pos),
	is_breeze(Pos).

possible_steps([Xfrom, Yfrom], [Xprev, Yprev], [Xto, Yto]) :-
	((Xto is Xfrom-1, Yto is Yfrom-1);
	(Xto is Xfrom-1, Yto is Yfrom);
	(Xto is Xfrom-1, Yto is Yfrom+1);
	(Xto is Xfrom, Yto is Yfrom-1);
	(Xto is Xfrom, Yto is Yfrom+1);
	(Xto is Xfrom+1, Yto is Yfrom-1);
	(Xto is Xfrom+1, Yto is Yfrom);
	(Xto is Xfrom+1, Yto is Yfrom+1)),
	not((Xto is Xprev, Yto is Yprev)),
	Xto > 0, Xto =< 5, Yto > 0, Yto =< 5.

can_update(NewPos) :-
	agent_pos(Pos),
	prev_pos(Prev),
	possible_steps(Pos, Prev, NewPos).

update_pos(NewPos) :-
	can_update(NewPos),
	agent_path(Path),
	append([NewPos], Path, NewPath),
	retractall(agent_path(_)),
	assert(agent_path(NewPath)).