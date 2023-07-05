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
            "1": ["A", "C"],
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

def run_nfa(machine, string):
    out_str = ""
    
    current_states = [machine["START_STATE"]]
    for idx, char in enumerate(string):
        out_str += f"({current_states}, {string[idx:]})" + " -> "
        next_states = []
        for state in current_states:
            next_states += machine["TRANSITION_FUNCTION"][state][char]
        current_states = next_states
    
    out_str += f"({current_states}, ε)\n"
    
    if any(state in machine["ACCEPT_STATES"] for state in current_states):
        out_str += "ACCEPT"
    else:
        out_str += "REJECT"
    
    return out_str


if __name__ == "__main__":
    print(run_nfa(MACHINE, STRING))