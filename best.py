def justify(text, width):
    words = text.split()
    line, length, res = [], 0, []
    
    for w in words:
        if length + len(w) + len(line) > width:
            for i in range(width - length):
                line[i % (max(1, len(line) - 1))] += '' if len(line) == 1 else ' '
            res.append(''.join(line))
            line, length = [], 0
        line.append(w)
        length += len(w)
        
    return '\n'.join(res + [' '.join(line)])