# 1
def f(x):
    """
    Returns x^2.
    :param x: int.
    :return: int squared x.
    """
    return x ** 2

result = f(3)
print(result)
print("\n")

# 2
def out_str(sen):
    """
    Returns print a sentence.
    :param sen: str.
    :return: output a sentence.
    """
    print(sen)

sen = "I want to be fucked by muscle men."
out_str(sen)
print("\n")

# 3
def g(a,b,c,d=3,e=2):
    """
    Returns a x b + c x d - e.
    :param a: int or float.
    :param b: int or float.
    :param c: int or float.
    :param d: int or float.
    :param e: int or float.
    return int or float of a calculation result.
    """
    return a * b + c * d - e

result2 = g(1,2,3)
print(result2)
print("\n")

# 4
def h():
    """
    Returns a integer (number / 2)
    :param f: a input_number
    return: int of a number devided by 2.
    """
    f = input("input a number.")
    f = int(f)
    return f // 2

def i():
    """
    Returns print a integer (f x 4).
    :param g: a calculation result of h().
    return: int of a number multiplied by 4.
    """
    g = h()
    print(g * 4)
i()
print("\n")

# 5
def j(stnum):
    """
    Returns print a float.
    :param stnum: a string number.
    return a float.
    """
    try:
        return float(stnum)
    except ValueError:
        print("input 'a number'!")
    
stnum = "thanks"
result3 = j(stnum)
if result3:
    print(result3)

