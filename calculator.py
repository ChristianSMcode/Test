import operations
import sys
#Archivo de caculadora
#Comentario2
#Tercer comentario
#Confirm dev branch
operation=sys.argv[1]
num1=int(sys.argv[2])
num2=int(sys.argv[3])

def main():
    if operation == 'sumar':
        print(operations.add(num1,num2))
    elif operation == 'resta':
        print(operations.sustract(num1,num2))
    elif operation == 'multiplicar':
        print(operations.multiply(num1,num2))
    elif operation == 'dividir':
        print(operations.divide(num1,num2))
    else:
        print('Operacion no existe.')

if __name__ == '__main__':
    main()

