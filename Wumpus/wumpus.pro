% -------- Load map --------
:- ['Wumpus\\game_map.pro'].

agent_path([[1, 1], [1, 1]]).
useless([]).
used_arrow(false).

:- dynamic([agent_path/1, useless/1, used_arrow/1]).

% --------------------- Helpers ---------------------

first_elem(List, E) :-
	nth0(0, List, E).

main :-
	make_step(Solution),
	print(Solution).

agent_pos(Pos) :-
	agent_path([Pos | _]).

prev_pos(Pos) :-
	agent_path([_, Pos | _]).

restart :-
	retractall(agent_path(_)),
	assertz(agent_path([[1, 1], [1, 1]])).

rollback :-
	agent_path([Miss | Tail]),
	retractall(agent_path(_)),
	assertz(agent_path(Tail)),
	useless(Places),
	append([Miss], Places, NewPlaces),
	retractall(useless(_)),
	assertz(useless(NewPlaces)).

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

is_wumpus(Pos) :-
	place(wumpus, Pos).

on_wumpus :-
	agent_pos(Pos),
	is_wumpus(Pos).

on_pit :-
	agent_pos(Pos),
	place(pit, Pos).

on_gold :-
	agent_pos(Pos),
	place(gold, Pos).

cost([Xprev, Yprev], [Xto, Yto], Cost) :-
	(is_wumpus([Xto, Yto]) -> Cost is 10;
	(Xprev=:=Xto; Yprev=:=Yto) -> Cost is 1;
	Cost is 2).

pick_cheapest_aux([], Cheapest, [_, CurTo]) :-
	Cheapest is CurTo.

pick_cheapest_aux([[Cost, To] | Tail], Cheapest, [CurCost, CurTo]) :-
	pick_cheapest_aux(Tail, Cheapest, [CurCost, CurTo]),
	(Cost < CurCost -> CurTo is To).

pick_cheapest([L | Ls], Cheapest) :-
	pick_cheapest_aux(Ls, Cheapest, L).

possible_steps([Xfrom, Yfrom], [Xprev, Yprev], [Xto, Yto], Cost) :-
	((Xto is Xfrom-1, Yto is Yfrom);
	(Xto is Xfrom, Yto is Yfrom-1);
	(Xto is Xfrom, Yto is Yfrom+1);
	(Xto is Xfrom+1, Yto is Yfrom)),
	not((Xto is Xprev, Yto is Yprev)),
	in_bounds([Xto, Yto]),
	cost([Xprev, Yprev], [Xto, Yto], Cost).

can_update(NewPos) :-
	agent_pos(Pos),
	prev_pos(Prev),
	agent_path(Path),
	\+member(NewPos, Path),
	useless(Useless),
	\+member(NewPos, Useless),
	possible_steps(Pos, Prev, NewPos, _).

update_pos(NewPos) :-
	can_update(NewPos),
	agent_path(Path),
	append([NewPos], Path, NewPath),
	retractall(agent_path(_)),
	assertz(agent_path(NewPath)),
	format('Moved to (~p, ~p).~n', NewPos).

make_step(Complete) :-
	agent_pos(CurPos),
	prev_pos(PrevPos),
	findall([Cost, To], possible_steps(CurPos, PrevPos, To, Cost), Bag),
	pick_cheapest(Bag, Che),
	([] is Che -> rollback; update_pos(Che)),
	((on_wumpus -> retractall(used_arrow(_)), assertz(used_arrow(true))); true),
	(on_pit -> rollback),
	agent_path(Path),
	(on_gold -> reverse(Path, Complete); make_step(Complete)).