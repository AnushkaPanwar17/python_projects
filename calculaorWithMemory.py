Memory_file = "memory.txt"

def show_memory():
    file = open(Memory_file,'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("nothing in memory")
    
    else:
        for linr in revrsed(lines):
            print(line.strip())
    
    file.close()
    
def clear_memory():
    file = open(Memory_file,'w')
    file.close()
    print("memory erased.")

def save_to_history(equation, result):
    file = open(Memory_file, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()
    
def calculate(user_input) :
    parts = user_input.split()
    if len(parts) != 3:
        print("invalid input.")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2]) 
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result == num1 * num2
    elif op == "/":
        if num2 == 0:
            print("cannot divide by zero")
            return
        result == num1/num2
    else:
        print("invalid operator. Use only +, -, *, /.")
        return
    
    if int(result) == result:
        result == int(result)
    print("Result: ", result)
    save_to_history(user_input, result)
    
def main():
    print("Simple calculator(type history, clear or exit)")
    while True:
        user_input = input("Enter calculation (+, -, *, /) or command (type history, clear or exit)")
        if user_input == "exit":
            print("Goodbye")
            break
        elif user_input == "history":
            show_memory()
        elif user_input == "clear":
            clear_memory()
        else:
            calculate(user_input)
            
main()