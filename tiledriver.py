# Name: Robert Vermeulen
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Spring 2021

import random
from typing import List, Tuple


class PuzzleState:  # do not modify

    def __init__(self, tiles: Tuple[int, ...], path: str) -> None:
        self.tiles = tiles
        self.width = int(len(tiles) ** 0.5)
        self.path = path

    def __eq__(self, other: "PuzzleState") -> bool:
        return self.tiles == other.tiles and self.path == other.path

    def __repr__(self) -> str:
        return self.path




def make_adjacent(state: PuzzleState) -> List[PuzzleState]:
    """
    Return a list of PuzzleState objects that represent valid, non-opposing
    moves from the given PuzzleState. A move is considered valid if it moves a
    tile adjacent to the blank tile into the blank tile. A move is considered
    non-opposing if it does not undo the previous move.

    >>> state = PuzzleState((3, 2, 1, 0), "")
    >>> make_adjacent(state)
    [PuzzleState((3, 0, 1, 2), "J"), PuzzleState((3, 2, 0, 1), "L")]
    """

    answ = []

    if state.width == 2:

        if state.tiles[0] == 0:
            answ = at0_2(state)

        if state.tiles[1] == 0:
            answ = at1_2(state)

        if state.tiles[2] == 0:
            answ = at2_2(state)

        if state.tiles[3] == 0:
            answ = at3_2(state)

    if state.width == 3:

        if state.tiles[0] == 0:
            answ = at0_3(state)

        if state.tiles[1] == 0:
            answ = at1_3(state)

        if state.tiles[2] == 0:
            answ = at2_3(state)

        if state.tiles[3] == 0:
            answ = at3_3(state)

        if state.tiles[4] == 0:
            answ = at4_3(state)

        if state.tiles[5] == 0:
            answ = at5_3(state)

        if state.tiles[6] == 0:
            answ = at6_3(state)

        if state.tiles[7] == 0:
            answ = at7_3(state)

        if state.tiles[8] == 0:
            answ = at8_3(state)

    return answ


def at0_2(state: PuzzleState) -> List[PuzzleState]:

    h = PuzzleState((state.tiles[1], state.tiles[0], state.tiles[2],
                     state.tiles[3]), state.path + "H")
    k = PuzzleState((state.tiles[2], state.tiles[1], state.tiles[0],
                     state.tiles[3]), state.path + "K")
    if state.path == '':
        return [k, h]
    if state.path[len(state.path) - 1] == "J":
        return [h]
    if state.path[len(state.path) - 1] == "L":
        return [k]
    return []


def at1_2(state: PuzzleState) -> List[PuzzleState]:

    l = PuzzleState((state.tiles[1], state.tiles[0], state.tiles[2],
                     state.tiles[3]), state.path + "L")
    k = PuzzleState((state.tiles[0], state.tiles[3], state.tiles[2],
                     state.tiles[1]), state.path + "K")
    if state.path == '':
        return [k, l]
    elif state.path[len(state.path) - 1] == "J":
        return [l]
    elif state.path[len(state.path) - 1] == "H":
        return [k]
    return []


def at2_2(state: PuzzleState) -> List[PuzzleState]:

    j = PuzzleState((state.tiles[2], state.tiles[1], state.tiles[0],
                     state.tiles[3]), state.path + "J")
    h = PuzzleState((state.tiles[0], state.tiles[1], state.tiles[3],
                     state.tiles[2]), state.path + "H")
    if state.path == '':
        return [j, h]
    elif state.path[len(state.path) - 1] == "K":
        return [h]
    elif state.path[len(state.path) - 1] == "L":
        return [j]
    return []


def at3_2(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    j = PuzzleState((w[0], w[3], w[2],
                     w[1]), state.path + "J")
    l = PuzzleState((w[0], w[1], w[3],
                     w[2]), state.path + "L")

    if state.path == '':
        return [j, l]
    elif state.path[len(state.path) - 1] == "K":
        return [l]
    elif state.path[len(state.path) - 1] == "H":
        return [j]
    return []


def at0_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    k = PuzzleState((w[3], w[1], w[2], w[0], w[4], w[5], w[6], w[7], w[8]),
                    state.path + "K")
    h = PuzzleState((w[1], w[0], w[2], w[3], w[4], w[5], w[6], w[7], w[8]),
                    state.path + "H")

    if state.path == '':
        return [k, h]
    if state.path[len(state.path) - 1] == "L":
        return [k]
    if state.path[len(state.path) - 1] == "J":
        return [h]

    return []


def at1_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    k = PuzzleState((w[0], w[4], w[2], w[3], w[1], w[5], w[6], w[7], w[8]),
                    state.path + "K")
    l = PuzzleState((w[1], w[0], w[2], w[3], w[4], w[5], w[6], w[7], w[8]),
                    state.path + "L")
    h = PuzzleState((w[0], w[2], w[1], w[3], w[4], w[5], w[6], w[7], w[8]),
                    state.path + "H")

    if state.path == '':
        return [k, l, h]
    if state.path[len(state.path) - 1] == "H":
        return [k, h]
    if state.path[len(state.path) - 1] == "L":
        return [k, l]
    if state.path[len(state.path) - 1] == "J":
        return [l, h]

    return []


def at2_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    k = PuzzleState((w[0], w[1], w[5], w[3], w[4], w[2], w[6], w[7], w[8]),
                    state.path + "K")
    l = PuzzleState((w[0], w[2], w[1], w[3], w[4], w[5], w[6], w[7], w[8]),
                    state.path + "L")

    if state.path == '':
        return [k, l]
    if state.path[len(state.path) - 1] == "H":
        return [k]
    if state.path[len(state.path) - 1] == "J":
        return [l]

    return []


def at3_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    k = PuzzleState((w[0], w[1], w[2], w[6], w[4], w[5], w[3], w[7], w[8]),
                    state.path + "K")
    j = PuzzleState((w[3], w[1], w[2], w[0], w[4], w[5], w[6], w[7], w[8]),
                    state.path + "J")
    h = PuzzleState((w[0], w[1], w[2], w[4], w[3], w[5], w[6], w[7], w[8]),
                    state.path + "H")

    if state.path == '':
        return [k, j, h]
    if state.path[len(state.path) - 1] == "L":
        return [k, j]
    if state.path[len(state.path) - 1] == "J":
        return [j, h]
    if state.path[len(state.path) - 1] == "K":
        return [k, h]

    return []


def at4_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    k = PuzzleState((w[0], w[1], w[2], w[3], w[7], w[5], w[6], w[4], w[8]),
                    state.path + "K")
    j = PuzzleState((w[0], w[4], w[2], w[3], w[1], w[5], w[6], w[7], w[8]),
                    state.path + "J")
    l = PuzzleState((w[0], w[1], w[2], w[4], w[3], w[5], w[6], w[7], w[8]),
                    state.path + "L")
    h = PuzzleState((w[0], w[1], w[2], w[3], w[5], w[4], w[6], w[7], w[8]),
                    state.path + "H")

    if state.path == '':
        return [k, j, l, h]
    if state.path[len(state.path) - 1] == "H":
        return [k, j, h]
    if state.path[len(state.path) - 1] == "L":
        return [k, j, l]
    if state.path[len(state.path) - 1] == "J":
        return [j, l, h]
    if state.path[len(state.path) - 1] == "K":
        return [k, l, h]

    return []


def at5_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    k = PuzzleState((w[0], w[1], w[2], w[3], w[4], w[8], w[6], w[7], w[5]),
                    state.path + "K")
    j = PuzzleState((w[0], w[1], w[5], w[3], w[4], w[2], w[6], w[7], w[8]),
                    state.path + "J")
    l = PuzzleState((w[0], w[1], w[2], w[3], w[5], w[4], w[6], w[7], w[8]),
                    state.path + "L")

    if state.path == '':
        return [k, j, l]
    if state.path[len(state.path) - 1] == "H":
        return [k, j]
    if state.path[len(state.path) - 1] == "J":
        return [j, l]
    if state.path[len(state.path) - 1] == "K":
        return [k, l]

    return []


def at6_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    j = PuzzleState((w[0], w[1], w[2], w[6], w[4], w[5], w[3], w[7], w[8]),
                    state.path + "J")
    h = PuzzleState((w[0], w[1], w[2], w[3], w[4], w[5], w[7], w[6], w[8]),
                    state.path + "H")

    if state.path == '':
        return [j, h]
    if state.path[len(state.path) - 1] == "L":
        return [j]
    if state.path[len(state.path) - 1] == "K":
        return [h]

    return []


def at7_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    j = PuzzleState((w[0], w[1], w[2], w[3], w[7], w[5], w[6], w[4], w[8]),
                    state.path + "J")
    l = PuzzleState((w[0], w[1], w[2], w[3], w[4], w[5], w[7], w[6], w[8]),
                    state.path + "L")
    h = PuzzleState((w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[8], w[7]),
                    state.path + "H")

    if state.path == '':
        return [j, l, h]
    if state.path[len(state.path) - 1] == "K":
        return [l, h]
    if state.path[len(state.path) - 1] == "L":
        return [j, l]
    if state.path[len(state.path) - 1] == "H":
        return [j, h]

    return []


def at8_3(state: PuzzleState) -> List[PuzzleState]:

    w = []
    for i in state.tiles:
        w.append(i)

    j = PuzzleState((w[0], w[1], w[2], w[3], w[4], w[8], w[6], w[7], w[5]),
                    state.path + "J")
    l = PuzzleState((w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[8], w[7]),
                    state.path + "L")

    if state.path == '':
        return [j, l]
    if state.path[len(state.path) - 1] == "K":
        return [l]
    if state.path[len(state.path) - 1] == "H":
        return [j]

    return []



def mergethatshit(thenums: List[int], invos: int) -> Tuple[List[int], int]:

    if len(thenums) < 2:
        return thenums, invos
    half = len(thenums)//2
    alist = []
    blist = []
    for num in range(len(thenums)):
        if num < half:
            alist.append(thenums[num])
        else:
            blist.append(thenums[num])

    anums, invos = mergethatshit(alist, invos)
    bums, invos = mergethatshit(blist, invos)

    out = []
    while len(anums) + len(bums) > 0:

        if len(anums) > 0 and len(bums) > 0:
            a = anums[0]
            b = bums[0]
            if a < b:
                out.append(anums.pop(0))
            else:
                out.append(bums.pop(0))
                invos += len(anums)

        elif len(anums) > 0:
            out.append(anums.pop(0))
        else:
            out.append(bums.pop(0))

    return out, invos



def is_solvable(tiles: Tuple[int, ...]) -> bool:
    """
    Return a Boolean indicating whether the given tuple represents a solvable
    puzzle. Use the Merge Sort algorithm (possibly in a helper function) to
    efficiently count the number of inversions.

    >>> is_solvable((3, 2, 1, 0))
    True
    >>> is_solvable((0, 2, 1, 3))
    False
    """
    c = []

    for num in tiles:
        c.append(num)

    nani = mergethatshit(c, 0)
    even = nani[1] % 2

    if len(c) == 4:
        q = c.index(0)
        if q == 1 or q == 2:
            if even == 0:
                return False
            return True
        if even == 0:
            return True
        return False

    if len(c) == 9:
        if even == 0:
            return True
    return False




def solve_puzzle(tiles: Tuple[int, ...]) -> str:
    """
    Return a string (containing characters "H", "J", "K", "L") representing the
    optimal number of moves to solve the given puzzle using Uniform Cost Search.
    A state is considered a solution if its tiles are sorted.

    >>> solve_puzzle((3, 2, 1, 0))
    "JLKHJL"
    """
    strrr = ''
    moves = []
    final: Tuple[int, ...] = ()
    if len(tiles) == 4:
        final = (0, 1, 2, 3)
    elif len(tiles) == 9:
        final = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    else:
        raise ValueError
    explored = []
    while tiles != final:
        c = PuzzleState(tiles, strrr)
        liss = make_adjacent(c)

        for i in liss:
            if i not in explored:
                moves.append(i)

        shortes = 0
        for move in range(len(moves)):
            if len(moves[move].path) < len(moves[shortes].path):
                shortes = move
            if moves[move].tiles == final:
                shortes = move

        tiles = moves[shortes].tiles
        strrr = moves[shortes].path
        explored.append(moves.pop(shortes))

    return strrr







c = True

def main() -> None:
    while c:
        #random.seed(int(input("Random Seed: ")))
        #tiles = list(range(int(input("Puzzle Width: ")) ** 2))  # use 2 or 3
        #random.shuffle(tiles)

        tiles = []
        d = input("what da tiles doe: ")
        for a in d:
            tiles.append(int(a))

        print("Tiles:", "[", " ".join(str(t) for t in tiles), "]")
        #print(tuple(tiles))
        if not is_solvable(tuple(tiles)):
            print("Unsolvable")
        else:
            print("Solution:", solve_puzzle(tuple(tiles)))


if __name__ == "__main__":
    main()
