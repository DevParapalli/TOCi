# DFA to accept strings ending with 00

MACHINE = {
    "STATES": ["A", "B", "C"],
    "INPUT_SYMBOLS": ["0", "1"],
    "TRANSITION_FUNCTION": {
        "A": {
            "0": "B",
            "1": "A",
        },
        "B": {
            "0": "C",
            "1": "A",
        },
        "C": {
            "0": "C",
            "1": "A",
        }
        },
    "START_STATE": "A",
    "ACCEPT_STATES": ["C"]
}

STRING = "10010101"


def run_dfa(machine, string: str) -> str:
    out_str = ""
    
    current_state = machine["START_STATE"]
    for idx, char in enumerate(string):
        out_str += f"({current_state}, {string[idx:]})" + " -> "
        current_state = machine["TRANSITION_FUNCTION"][current_state][char]
    
    out_str += f"({current_state}, ε)\n"
    
    if current_state in machine["ACCEPT_STATES"]:
        out_str += "ACCEPT"
    else:
        out_str += "REJECT"
    
    return out_str


if __name__ == "__main__":
    print(run_dfa(MACHINE, STRING))