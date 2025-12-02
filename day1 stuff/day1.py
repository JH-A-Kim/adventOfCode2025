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
    file_path='day1 stuff/password.txt'
    lines = read_lines_from_file(file_path)
    current=50
    count=0
    for line in lines:
        current=rotate_dial(current, line.strip())
        if current==0:
            count+=1
    print("Final position:", current)
    print("Number of times at position 0:", count)