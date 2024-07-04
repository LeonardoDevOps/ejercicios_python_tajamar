def save_users(name_file, user, password):
    with open(name_file, "a") as file:
        file.write(f"{user},{password}\n")

def main():
    name_file = "data_base_users.txt"
    while True:
        user = input("Introduce el nombre de usuario: ")
        password = input("Introduce la contraseña: ")
        
        save_users(name_file, user, password)
        
        continuar = input("¿Deseas guardar otro usuario? (s/n): ").lower()
        if continuar != 's':
            break

    print("Base de datos de usuarios guardada en data_base_users.txt")

if __name__ == "__main__":
    main()