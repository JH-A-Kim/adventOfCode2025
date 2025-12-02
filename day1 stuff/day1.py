import io

def read_lines_from_file(file_path):
    with io.open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return lines

def rotate_dial(current, input):
    if input[0]=='L':
        current=(current-int(input[1:]))%100
    elif input[0]=='R':
        current=(current+int(input[1:]))%100
    return current

if __name__ == "__main__":
    file_path = 'day1 stuff/password.txt'
    lines = read_lines_from_file(file_path)
    current = 50
    
    total_password = 0

    for line in lines:
        line = line.strip()
        if not line: continue 
        
        direction = line[0]
        distance = int(line[1:])
    
        total_password += distance // 100
        
        remainder = distance % 100
        
        if direction == 'L':
            if 0 < current <= remainder:
                total_password += 1
                
        elif direction == 'R':
            if current + remainder >= 100:
                total_password += 1
        current = rotate_dial(current, line)

    print("Final position:", current)
    print("Total password (Part 2):", total_password)