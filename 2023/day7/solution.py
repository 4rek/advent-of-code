import os
from time import process_time_ns

score_ranks = {
    "high": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "full": 4,
    "four": 5,
    "five": 6,
}

part1_ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
part2_ranks = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def custom_sort(strings, ranks):
    rank_dict = {char: i for i, char in enumerate(ranks[::-1])}

    # Function to calculate a score for a string
    def score_string(s):
        return [rank_dict.get(char, len(ranks)) for char in s]

    # Sort the strings using the score function as key
    return sorted(strings, key=score_string)


def part1(lines: str):
    card_bids = {}
    results = {key: [] for key in score_ranks.keys()}

    for line in lines.split("\n"):
        hand = {}

        cards, bid = line.split()
        card_bids[cards] = int(bid)

        for c in cards:
            hand[c] = 1 if c not in hand else hand[c] + 1

        c = (cards, int(bid))

        v = hand.values()

        if 5 in v:
            results["five"].append(cards)
            continue

        if 4 in v:
            results["four"].append(cards)
            continue

        if 3 in v and 2 in v:
            results["full"].append(cards)
            continue

        if 3 in v:
            results["three"].append(cards)
            continue

        if list(v).count(2) == 2:
            results["two"].append(cards)
            continue

        if list(v).count(2) == 1:
            results["one"].append(cards)
            continue

        results["high"].append(cards)

    for key, value in results.items():
        results[key] = list(
            map(lambda x: card_bids[x], custom_sort(value, part1_ranks))
        )

    i = 1
    s = 0
    for r in results.values():
        if len(r) > 0:
            for x in r:
                s += i * x
                i += 1
    return s


def part2(lines: str):
    card_bids = {}
    results = {key: [] for key in score_ranks.keys()}

    for line in lines.split("\n"):
        hand = {}

        cards, bid = line.split()
        card_bids[cards] = int(bid)

        for c in cards:
            if c != "J":
                hand[c] = 1 if c not in hand else hand[c] + 1

        c = (cards, int(bid))

        if "J" in cards:
            if not bool(hand):
                hand["A"] = 5  # this covers case when card is "JJJJJ"
            else:
                max_hand_value = max(hand.values())
                max_hand_keys = [k for k, v in hand.items() if v == max_hand_value]

                best = max_hand_keys[0]
                hand[best] = hand[best] + cards.count("J")

        v = hand.values()

        if 5 in v:
            results["five"].append(cards)
            continue

        if 4 in v:
            results["four"].append(cards)
            continue

        if 3 in v and 2 in v:
            results["full"].append(cards)
            continue

        if 3 in v:
            results["three"].append(cards)
            continue

        if list(v).count(2) == 2:
            results["two"].append(cards)
            continue

        if list(v).count(2) == 1:
            results["one"].append(cards)
            continue

        results["high"].append(cards)

    for key, value in results.items():
        results[key] = list(
            map(lambda x: card_bids[x], custom_sort(value, part2_ranks))
        )

    s, i = 0, 1

    for value in results.values():
        if len(value) > 0:
            for x in value:
                s += i * x
                i += 1
    return s


# def main():
#     time_start = process_time_ns()
#     f = open(f"{os.getcwd()}/day7/inputs/main.txt", "r")
#     lines = f.read().strip()
#     print(part2(lines))
#     time_end = process_time_ns()
#     time_duration = time_end - time_start
#     print(f"Took {time_duration} ns")


# main()
