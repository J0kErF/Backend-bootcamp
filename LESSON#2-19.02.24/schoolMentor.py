
def printABC():
    for letter in range(65, 91):
        print(chr(letter), end=' ')
    print()

def printabc():
    for letter in range(97, 123):
        print(chr(letter), end=' ')
    print()

def printMultiplicationTable(number):
    for i in range(1, number+1):
        for j in range(1, number+1):
            print(i*j, end=' ')
        print()

def printSquareNumber(number):
    print(number**2)

def isPrime(number):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

def printWord(letter):
    words= ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'imbe', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'watermelon', 'ximenia', 'yuzu', 'zucchini']
    for word in words:
        if word[0] == letter:
            print(word)

def main():
    func=input('Enter the function you want to run: \n 1. print the ABC \n 2. print the abc \n 3. print Multiplication Table \n 4. print Square Number \n 5. is the number prime \n 6. print a Word \n')
    match func:
        case '1':
            printABC()
        case '2':
            printabc()
        case '3':
            number= int(input('Enter the number: '))
            printMultiplicationTable(number)
        case '4':
            number= int(input('Enter the number: '))
            printSquareNumber(number)
        case '5':
            number= int(input('Enter the number: '))
            print(isPrime(number))
        case '6':
            letter= input('Enter the letter: ')
            printWord(letter)
        case _:
            print('Invalid input')
            return main()
main()