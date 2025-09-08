"""
This file contains a dictionary that defines the set of available building types, their construction
times, and their profit per unit of operational time.

Keys:
    "T" : Theatre
        - Construction time: 5 units
        - Profit rate: $1500 per unit time after completion
    "P" : Pub
        - Construction time: 4 units
        - Profit rate: $1000 per unit time after completion
    "C" : Commercial Park
        - Construction time: 10 units
        - Profit rate: $3000 per unit time after completion

The optimizer imports this configuration to compute the best construction
schedule.
"""


BUILDINGS = {
    "T": {"time": 5, "profit": 1500},
    "P": {"time": 4, "profit": 1000},
    "C": {"time": 10, "profit": 3000},
}
