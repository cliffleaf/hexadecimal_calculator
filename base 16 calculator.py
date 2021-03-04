import tkinter 

def hex_arithmetic(hex_num1, operator, hex_num2):

    hex_num1 = hex_num1.strip()
    hex_num2 = hex_num2.strip()
    operator = operator.strip()

    if operator == "+":
        answer_in_deci = int(hex_num1, 16) + int(hex_num2, 16)
    elif operator == "-":
        answer_in_deci = int(hex_num1, 16) - int(hex_num2, 16)
    elif operator == "*":
        answer_in_deci = int(hex_num1, 16) * int(hex_num2, 16)
    elif operator == "/":
        answer_in_deci = int(hex_num1, 16) / int(hex_num2, 16)

    elif operator == "**":
        answer_in_deci = int(hex_num1, 16) ** int(hex_num2, 16)
        
    else:
        return "invalid operator"
    
    answer_in_hex = hex(answer_in_deci)
    answer_in_hex = answer_in_hex[2:].upper()

    return answer_in_hex


def get_user_input():
    hex_num1 = entry_num1.get()
    hex_num2 = entry_num2.get()
    operator = entry_operator.get()

    return hex_num1, operator, hex_num2

def show_answer():
    hex_num1, operator, hex_num2 = get_user_input()
    answer = hex_arithmetic(hex_num1, operator, hex_num2)

    for widget in answerFrame.winfo_children():
       widget.destroy()

    answer_txt = tkinter.Label(answerFrame, text = str(answer), font = ("Courier", 12), bg = "white")
    answer_txt.grid(row = 40, column = 5, columnspan = 100)

# GUI section
root = tkinter.Tk()
root.geometry("190x200+300+200")
root.title("Base 16 calculator")
root.configure(bg = "white")

topFrame = tkinter.Frame(root, bg = "white")
topFrame.grid(row = 0, column = 0)

label_num1 = tkinter.Label(topFrame, text = "number 1", width = 10, font = ("Courier", 13), bg = "white")
label_num1.grid(row = 30, column = 1)
entry_num1 = tkinter.Entry(topFrame, width = 10, bg = "white")
entry_num1.grid(row = 30, column = 4)

label_operator = tkinter.Label(topFrame, text = "operator", width = 10, font = ("Courier", 13), bg = "white")
label_operator.grid(row = 50, column = 1)
entry_operator = tkinter.Entry(topFrame, width = 10, bg = "white")
entry_operator.grid(row = 50, column = 4)

label_num2 = tkinter.Label(topFrame, text = "number 2", width = 10, font = ("Courier", 13), bg = "white")
label_num2.grid(row = 70, column = 1)
entry_num2 = tkinter.Entry(topFrame, width = 10)
entry_num2.grid(row = 70, column = 4)


blank_label = tkinter.Label(topFrame, bg = "white")
blank_label.grid(row = 80)


buttonFrame = tkinter.Frame(root, bg = "white")
buttonFrame.grid(row = 1, column = 0)
button = tkinter.Button(buttonFrame, text = "calculate", command = show_answer)
button.grid(row = 90, column = 4)

answerFrame = tkinter.Frame(root, bg = "white")
answerFrame.grid(row = 2, column = 0)

root.mainloop()