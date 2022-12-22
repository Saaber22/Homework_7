"""Функция """
def modern_string (str):
    x = []
    for i in range(len(str)):
        x.append(str[i].encode('utf-8'))      
    return x

def reverse_string (str):
    y = []
    for i in range(len(str)):
        y.append(str[i].decode('utf-8')) 
    return y


if __name__ == "__main__":
    print("Hello")