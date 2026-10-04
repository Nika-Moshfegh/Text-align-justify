def justify(text, width):
    words = text.split()
    lines = []          
    result = []         
    counter = 0         
    for i in range(len(words)):
        word = words[i]

        if counter == 0:
            new_counter = len(word)
        else:
            new_counter = counter + 1 + len(word)

        if new_counter <= width:
            result.append(word)
            counter = new_counter
        else:
            lines.append(result)
            result = [word]
            counter = len(word)

    if result:
        lines.append(result)

    output = ""
    for i in range(len(lines)):
        line = lines[i]

        if len(line) == 1 or i == len(lines) - 1:
            output += " ".join(line)
        else:
            total_chars = sum(len(w) for w in line)
            total_spaces = width - total_chars
            gaps = len(line) - 1
            base = total_spaces // gaps
            extra = total_spaces % gaps

            parts = []
            for j in range(len(line)):
                parts.append(line[j])
                if j < gaps:
                    spaces = base + (1 if j < extra else 0)
                    parts.append(" " * spaces)
            output += "".join(parts)

        if i != len(lines) - 1:
            output += "\n"

    return output