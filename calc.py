print('calculator\n' + 'to use calculator please enter one of the following function\n' + 
      '+ for addition\n' + 
      '- for subtraction\n' + 
      'x for multiplication\n' + 
      '/ for division\n' +
      'log for logarithm\n' +
      'quad for quadratic\n' +
      'sin for sine\n' +
      'cos for cosine\n' +
      'tan for tan\n')

#some standard values
pi = 3.14159
e = 2.71828

# addition 
def add():
    int1 = float(input('input number 1:'))
    int2 = float(input('input number 2:'))
    return int1+int2

#subtraction
def subs():
    int1 = float(input('input number 1:'))
    int2 = float(input('input number 2:'))
    return int1-int2

#multiplication
def multiply():
    int1 = float(input('input number 1:'))
    int2 = float(input('input number 2:'))
    return int1*int2

#logarithm
def log_n(int1 = 0):
    if int1 == 0:
        int1 = float(input('input number 1:'))
    int_part,frac_part = 0,0
    while int1 > 1:
        int1 = int1/e
        int_part += 1
    x = int1 - 1
    p = x
    for i in range(999):
        frac_part = frac_part + p
        p = (-p)(x)((i+1)/(i+2))
    return int_part + frac_part

def log():
    int1 = input('enter base(press "e" for natural log):')
    int2 = float(input('enter the number:'))
    if int1 == "e":
        return log_n(int2)
    return log_n(int2)/log_n(float(int1))


#division
def divide():
    int1 = float(input('input number 1:'))
    int2 = float(input('input number 2:'))
    return int1/int2

#trignometric functions
def sin(inp=0):
    if inp == 0:
        inp = float(input('enter angle:'))
    while inp > 90:
        inp = -(inp - 180)
    x = inp*(pi/180)
    p = 0
    q = x
    for i in range(999999):
        p = p + q
        q = -(q*(x*2/(i*2+5*i+6)))
    return p

def cos(inp=0):
    if inp == 0:
        inp = float(input('enter angle:'))
    while inp > 90:
        inp = (inp - 180)
    x = inp*(pi/180)
    p = 0
    q = 1
    for k in range(999999):
        p = p + q
        q = -(q*(x*2/(k*2+k*3+2)))
    return p

def tan():
    inp = float(input('enter angle:'))
    p = sin(inp)/cos(inp)
    return p

def quad():
    a= float(input('enter co-efficient of degree 2:'))
    b= float(input('enter co-efficient of degree 1:'))
    c= float(input('enter constant term:'))
    smaller,larger = (-b-(b*2-(4*a*c)))/(2*a),(-b+(b*2-(4*a*c)))/(2*a)
    return "root 1:"+ str(smaller) + " root 2:"+ str(larger)
#main "loop"
run = True
while run:
    user_input = input('Enter a function :')

    if user_input == '+':
        print(add())
    if user_input == '-':
        print(subs())
    if user_input == 'x':
        print(multiply())
    if user_input == '/':
        print(divide())
    if user_input == 'quad':
        print(quad())
    if user_input == 'sin':
        print(sin())
    if user_input == 'cos':
        print(cos())
    if user_input == 'tan':
        print(tan())
    if user_input == 'log':
        print(log())
    if user_input == 'q':
        run = False
