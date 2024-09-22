import argparse

class AlreadyExistedException(Exception): pass 

parser = argparse.ArgumentParser(description="Process some files.")
parser.add_argument('--file', type=str, required=True, help='The UIScript file.')
args = parser.parse_args()

f = open(args.file, encoding='UTF-8')

def interpret(code: str):
    float_vars = dict()
    str_vars = dict()
    prg = 0
    while prg < len(code.split('\n')):
        lines = code.split('\n')[prg]
        blocks = lines.split(' ')
        cmd = blocks[0]
        match cmd:
            case 'boncau':
                if blocks[1] == 'float':
                    if not blocks[2] in float_vars.keys():
                        float_vars[blocks[2]] = float(blocks[3])
                elif blocks[1] == 'str':
                    if not blocks[2] in str_vars.keys():
                        str_vars[blocks[2]] = ' '.join(blocks[3:])
            case 'iadun':
                if blocks[1] == 'float':
                    print(float_vars[blocks[2]])
                elif blocks[1] == 'str':
                    print(str_vars[blocks[2]])
            case 'add':
                float_vars[blocks[1]] += float_vars[blocks[2]]
            case 'sub':
                float_vars[blocks[1]] -= float_vars[blocks[2]]
            case 'mul':
                float_vars[blocks[1]] *= float_vars[blocks[2]]
            case 'div':
                float_vars[blocks[1]] /= float_vars[blocks[2]]
            case 'gis':
                if blocks[1] == 'float':
                    str_vars[blocks[3]] = str(float_vars[blocks[2]])
                if blocks[1] == 'str':
                    float_vars[blocks[3]] = float(str_vars[blocks[2]])
            case 'damdai':
                str_vars[blocks[3]] = str_vars[blocks[1]] + str_vars[blocks[2]]
            case 'input':
                str_vars[blocks[1]] = input()
            case 'iangay':
                prg = int(float_vars[blocks[1]])-2
            case 'iabang':
                if blocks[1] == 'float':
                    if float_vars[blocks[2]] == float_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
                if blocks[1] == 'str':
                    if str_vars[blocks[2]] == str_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
            case 'iakhongbang':
                if blocks[1] == 'float':
                    if float_vars[blocks[2]] != float_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
                if blocks[1] == 'str':
                    if str_vars[blocks[2]] != str_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
            case 'iahon':
                if blocks[1] == 'float':
                    if float_vars[blocks[2]] > float_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
                if blocks[1] == 'str':
                    if str_vars[blocks[2]] > str_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
            case 'iait':
                if blocks[1] == 'float':
                    if float_vars[blocks[2]] < float_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
                if blocks[1] == 'str':
                    if str_vars[blocks[2]] < str_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
            case 'iahonbang':
                if blocks[1] == 'float':
                    if float_vars[blocks[2]] >= float_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
                if blocks[1] == 'str':
                    if str_vars[blocks[2]] >= str_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
            case 'iaitbang':
                if blocks[1] == 'float':
                    if float_vars[blocks[2]] <= float_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
                if blocks[1] == 'str':
                    if str_vars[blocks[2]] <= str_vars[blocks[3]]:
                        prg = int(float_vars[blocks[4]])-2
            case 'daubungqua':
                break
                
        prg += 1
    
interpret(f.read())