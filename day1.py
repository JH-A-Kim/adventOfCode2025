import io

def read_lines_from_file(file_path):
    with io.open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return lines

def rotate_dial(current, input):
    temp = current
    if input[0]=='l':
        temp -= int(input[2:])

        if temp < 0:
            current = 99-temp
        else:
            current = temp

    elif input[0]=='r':
        temp += int(input[2:])

        if temp > 99:
            current = temp-100
        else:
            current = temp
    
    return current

if __name__ == "__main__":
    file_path='password.txt'
    lines = read_lines_from_file(file_path)
    for line in lines:
        inputs = line.split(',')
        current = 50
        for input in inputs:
            current = rotate_dial(current, input.strip())
        print(current)
