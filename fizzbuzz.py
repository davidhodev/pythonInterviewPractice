# My Fizzbuzz solution
def fizzbuzz(multiples, maximum):
    for i in range(1,maximum):
        output = ''
        for multiple in multiples:
            if i%multiple == 0:
                output += multiples[multiple]
        if output == '':
            output = str(i)
        print(output)

multiples = {3: 'Fizz', 5: 'Buzz', 13: "Thirteen"}
fizzbuzz(multiples, 100)