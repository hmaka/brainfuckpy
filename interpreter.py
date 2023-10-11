tokens = list(input())


def interpret(tokens:list[str]):
    # The original spec called for a tape length of 30,000. So we honor that here.
    tape = [0]*30000
    # We will leverage a stack to deal with loops
    # The top of the stack will indicate the index in tokens where the loop started
    stack = []
    
    tape_ptr = 0
    token_ptr = 0
    
    while token_ptr < len(tokens):
        match tokens[token_ptr]:
            case ">": 
                tape_ptr += 1
            case "<":
                if tape_ptr == 0: raise IndexError("Left-side tape overflow")
                tape_ptr -= 1
            case "+":
                if tape[tape_ptr] == 255: raise OverflowError("Tape byte exceeding 255")
                tape[tape_ptr] += 1
    
            case "-":
                if tape[tape_ptr] == 0: raise OverflowError("Tape byte below 0")
                tape[tape_ptr] -= 1
            case ".":
                print(chr(tape[tape_ptr]), end="")
            case "[":
                # skip tokens in loop if current tape byte is zero.
                if tape[tape_ptr] == 0:
                    count = 0
                    while tokens[token_ptr] != "]" or count: 
                        if tokens[token_ptr] == "[": count += 1
                        elif tokens[token_ptr] == "]": count -= 1
                        token_ptr += 1
                else:
                    stack.append(token_ptr)
            case "]":
                if tape[tape_ptr] == 0: stack.pop()
                else: token_ptr = stack[-1]
    
            
    
        token_ptr += 1
        
    print()
    print("program finished successfully")

interpret(tokens)
