import os
Board = {
    "Input": [],
    "Output": []
}
os.system("cls")
def add_gate(gtype: str, in0: str, in1: str, end: bool):
    global Board
    gnum = len([i for i in Board.keys() if f"{gtype} Gate" in i]) + 1
    gname = f"{gtype} Gate {gnum}"
    Board[gname] = {"Inputs": [in0, in1], "Output": None, "end": end}
    return f"{gname} created with connections {in0}, {in1}"

def run_game(*inputs):
    global Board
    for i in inputs:
        if i > 1 or i < 0:
            raise "One or more inputs are not a bit."
        Board["Input"].append(i)
    for gname, gate in Board.items():
            if "Input" in gname or "Output" in gname:
                continue
            gin1, gin2 = gate["Inputs"]
            c = [False, False]
            if "Input" in gin1:
                gin1.split()
                try:
                    gin1val = Board["Input"][int(gin1[-1])]
                except:
                    print(f"Too few inputs: {gin1[-1]}")
                    break
                c[0] = True
            if gin2 != None:
                if "Input" in gin2:
                    gin2.split()
                    try:
                        gin2val = Board["Input"][int(gin2[-1])]
                    except:
                        print(f"Too few inputs: {gin2[-1]}")
                        break
                    c[1] = True
            if not c[0]:
                gin1val = Board[gin1]["Output"]
            if not c[1] and gin2 != None:
                gin2val = Board[gin2]["Output"]
            if "NAND Gate" in gname:
                out = int(not (gin1val & gin2val))
                print(f"{gin1val} ({gin1}) NAND {gin2val} ({gin2})   -> {out}", end="")
            elif "AND Gate" in gname:
                out = gin1val & gin2val
                print(f"{gin1val} ({gin1})  AND {gin2val} ({gin2})   -> {out}", end="")
            elif "XOR Gate" in gname:
                out = gin1val ^ gin2val
                print(f"{gin1val} ({gin1})  XOR {gin2val} ({gin2})   -> {out}", end="")
            elif "OR Gate" in gname:
                out = gin1val | gin2val
                print(f"{gin1val} ({gin1})   OR {gin2val} ({gin2})   -> {out}", end="")
            elif "NOT Gate" in gname:
                out = int(not gin1val)
                print(f"                    NOT {gin1val} ({gin1})   -> {out}", end="")
            else:
                raise f"Invalid Gate: {gname}"
            
            if gate["end"]:
                print(" (end)")
                Board["Output"].append(str(out))
            else:
                gate["Output"] = out
                print()
    if Board['Output'] == []:
        Board['Output'] = ["Error"]
    return f"End result: {' '.join(Board['Output'])}"