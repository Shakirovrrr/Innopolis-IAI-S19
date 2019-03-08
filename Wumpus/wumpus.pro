:- ['Wumpus\\game_map.pro'].

:- dynamic([agent_pos/1, prev_pos/1]).

% --------------------- Helpers ---------------------

is_neighbour(What, [X, Y]) :-
	place(What, [WX, WY]),
	(X is WX-1, Y is WY;
	X is WX, Y is WY-1;
	X is WX, Y is WY+1;
	X is WX+1, Y is WY).

is_smell([X, Y]) :-
	is_neighbour(wumpus, [X, Y]).

on_smell(true) :-
	agent_pos(Pos),
	is_smell(Pos).

on_smell(false) :-
	\+ on_smell(true).

is_breeze([X, Y]) :-
	is_neighbour(pit, [X, Y]).

on_breeze(true) :-
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

shift_prev(_) :-
	agent_pos(Pos),
	retractall(prev_pos(_)),
	assert(prev_pos(Pos)).

can_update(true, NewPos) :-
	agent_pos(Pos),
	prev_pos(Prev),
	possible_steps(Pos, Prev, NewPos).

update_pos(NewPos) :-
	can_update(Can, NewPos), Can,
	shift_prev(_),
	retractall(agent_pos(_)),
	assert(agent_pos(NewPos)).
	
