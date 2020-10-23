
    c = 1
    p = 1
    numero = 3
    primos = "2, "
    while p < limite:
        ehprimo = 1
        for i in range(2, numero):
            if numero%i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(numero) + ","
            p+=1
        numero +=1

    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

primo.py[+] [unix] (02:45 23/10/2020)                                                       22,1 All
-- INSERT --
 
