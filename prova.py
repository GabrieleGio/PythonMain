def rewrite_dict(d: dict[str, int]) -> dict[str, int]:
    somma = sum(d.values())
    out = {}
    for key in d:
        out[key] = d[key] / somma
    return out

