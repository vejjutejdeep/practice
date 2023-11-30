def fibonacciTriangleGenerator(lines):

    numberElement = 0

    for iter1 in range(lines):

        ope1 = 1

        ope2 = 1

        counter = 0

        while(counter <= numberElement):
            
            print(str(ope1), end="\t")

            ope1, ope2 = ope2, ope1 +ope2

            counter += 1
        
        numberElement = counter
        
        print()

print("Enter number of lines to generate:", end=' ')
lines = int(input())
fibonacciTriangleGenerator(lines)