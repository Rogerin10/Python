pswd_real = "python123"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    pswd_user = input("Contraseña: ")
    intentos += 1

    if pswd_user == pswd_real:
        print("Acceso concedido")
        break
    else:
        print("Incorrecta")

if pswd_user != pswd_real:
    print("Acceso denegado")
