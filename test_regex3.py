import re

names = [
    "TOROS 3 - 9U - B - Masculin - LOTBINIÈRE",
    "MONARQUES BLEU 13UAA",
    "MONARQUES BLEU - 13U - AA",
    "TITANS 5 9UB",
    "JAYS - 13U - A - MASCULIN",
    "MONARQUES-LEV-LOT-ORANGE - Junior - AA - Masculin - SEIGNEURIES"
]

pattern = r'^([A-Za-zÀ-ÿ\-]+(?:\s+[A-Za-zÀ-ÿ0-9\-]+)*?)\s*(?:-)?\s*(\d+U|Junior|Senior|Midget|Bantam|Peewee|Moustique|Atome|Novice).*?([AB]{1,2})(?![A-Za-z])'

for name in names:
    match = re.search(pattern, name, re.IGNORECASE)
    if match:
        print(f"'{name}' -> '{match.group(1).strip()} {match.group(2)}{match.group(3)}'")
    else:
        print(f"'{name}' -> NO MATCH")

