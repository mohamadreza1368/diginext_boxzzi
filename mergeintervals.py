def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []
    current_start, current_end = intervals[0]
    
    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged_intervals.append((current_start, current_end))
            current_start, current_end = start, end
    
    merged_intervals.append((current_start, current_end))
    
    return merged_intervals

intervals = [(1, 3), (2, 6), (8, 10)]
result = merge_intervals(intervals)
print(result) 
