:- ['Wumpus\\game_map.pro'].

:- dynamic([agent_path/1, useless/1]).

% --------------------- Helpers ---------------------

agent_pos(Pos) :-
	agent_path([Pos | _]).

prev_pos(Pos) :-
	agent_path([_, Pos | _]).

restart :-
	retractall(agent_path(_)),
	assert(agent_path([[1, 1], [1, 1]])).

rollback :-
	agent_path([Miss | Tail]),
	retractall(agent_path(_)),
	assert(agent_path(Tail)),
	useless(Places),
	append([Miss], Places, NewPlaces),
	retractall(useless(_)),
	assert(useless(NewPlaces)).

is_neighbour(What, [X, Y]) :-
	place(What, [WX, WY]),
	(X is WX-1, Y is WY;
	X is WX, Y is WY-1;
	X is WX, Y is WY+1;
	X is WX+1, Y is WY).

in_bounds([X, Y]) :-
	X > 0, X =< 5,
	Y > 0, Y =< 5.

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

possible_steps([Xfrom, Yfrom], [Xprev, Yprev], [Xto, Yto], Cost) :-
	(Xto is Xfrom-1, Yto is Yfrom);
	(Xto is Xfrom, Yto is Yfrom-1);
	(Xto is Xfrom, Yto is Yfrom+1);
	(Xto is Xfrom+1, Yto is Yfrom);
	not((Xto is Xprev, Yto is Yprev)),
	in_bounds([Xto, Yto]),
	Cost is 2,
	(Xprev=:=Xto; Yprev=:=Yto -> Cost is 1).

death(Pos) :-
	place(wumpus, Pos);
	place(pit, Pos).

can_update(NewPos) :-
	agent_pos(Pos),
	prev_pos(Prev),
	agent_path(Path),
	\+member(NewPos, Path),
	useless(Places),
	\+member(NewPos, Places),
	possible_steps(Pos, Prev, NewPos, _).

update_pos(NewPos) :-
	can_update(NewPos),
	agent_path(Path),
	append([NewPos], Path, NewPath),
	retractall(agent_path(_)),
	assert(agent_path(NewPath)),
	format('Moved to (~p, ~p).~n', NewPos).
