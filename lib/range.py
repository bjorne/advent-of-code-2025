def overlaps(a: range, b: range) -> bool:
    return a.start <= b.start <= a.stop or b.start <= a.start <= b.stop

def merge_overlapping(ranges: list[range]) -> list[range]:
    ranges = sorted(ranges, key=lambda r: r.start)
    merged = []
    for i, r in enumerate(ranges):
        if len(merged) > 0 and (last := merged[-1]) and overlaps(r, last):
            merged[-1] = range(min(r.start, last.start), max(r.stop, last.stop))
        else:
            merged.append(r)

    return merged
