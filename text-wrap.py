import textwrap

def wrap(string, max_width):
    result = ''
    lines = len(string)//max_width
    for n in range(lines):
        f = max_width*n
        l = max_width*n+max_width
        result += string[f:l] + '\n'
    return result + string[l:]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)