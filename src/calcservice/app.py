from mathkitlite import add, mean


def totals(rows):
    return {"sum": add(sum(rows), 0), "avg": mean(rows)}
