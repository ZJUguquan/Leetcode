

import re
def parse_molecule (formula):
    for br in "[{":
        formula = formula.replace(br, "(")
    for br in "]}":
        formula = formula.replace(br, ")")
    while "(" in formula:
        clsbr = formula.find(")")
        opnbr = clsbr - formula[:clsbr][::-1].find("(")
        subformula = formula[opnbr:clsbr]
        subindex = re.match("\)([0-9]*)", formula[clsbr:]).group(1)
        z = "(" + subformula + ")" + subindex
        subindex = 1 if not subindex else int(subindex)
        simplified = [str(a) + str(n * subindex) for a, n in parse_molecule(subformula).iteritems()]
        formula = formula.replace(z, ''.join(simplified))
    formula = re.sub("([a-zA-Z0-9])([A-Z])", r"\1 \2", formula)
    formula = re.sub("([a-zA-Z0-9])([A-Z])", r"\1 \2", formula)
    formula = re.sub("([A-Za-z]+)([0-9]*)", r"\1:\2", formula)
    els = [element.split(":") for element in formula.split(" ")]
    elements = [(el[0], (int(el[1]) if el[1] else 1)) for el in els]
    atoms = {}
    for a, n in elements:
        if a not in atoms:
            atoms[a] = n
        else:
            atoms[a] += n
    return atoms