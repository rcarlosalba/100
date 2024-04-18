import os
"""Create, Read, Update, Delete (CRUD) operations 
for the agenda app."""

CARPETA = 'data/'
EXTENSION = '.txt'


def app():
    create_dir()

    ask = True
    while ask:
        show_menu()
        option = input('Escribe el número de la opción: ')
        if option == '1':
            create_contact()
        elif option == '2':
            edit_contact()
        elif option == '3':
            show_contacts()
        elif option == '4':
            delete_contact()
        elif option == '5':
            search_contact()
        else:
            print('Opción no válida')

        ask = input('¿Quieres realizar otra operación? (si/no): ')
        if ask == 'no':
            ask = False


def create_dir():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)


def show_menu():
    print('Seleccione una opción:')
    print('1. Crear contacto')
    print('2. Editar contactos')
    print('3. Ver contacto')
    print('4. Eliminar contacto')
    print('5. Buscar contacto')


def create_contact():
    print('Escribe los datos del nuevo contacto.')
    contact_name = input('Nombre: \r\n')

    is_a_contact = is_there(contact_name)

    if not is_a_contact:
        with open(CARPETA + contact_name + EXTENSION, 'w') as file:
            phone = input('Teléfono: \r\n')
            category = input('Categoría: \r\n')

            file.write('Nombre: ' + contact_name + '\r\n')
            file.write('Teléfono: ' + phone + '\r\n')
            file.write('Categoría: ' + category + '\r\n')
            file.write('\r\n')
            print('Contacto creado correctamente.')
    else:
        print('El contacto ya existe.')


def edit_contact():
    print('Escribe el nombre del contacto a editar.')
    previus_name = input('Nombre del contacto a editar: \r\n')

    is_a_contact = is_there(previus_name)

    if is_a_contact:
        with open(CARPETA + previus_name + EXTENSION, 'w') as file:
            contact_name = input('Nuevo Nombre: \r\n')
            phone = input('Teléfono: \r\n')
            category = input('Categoría: \r\n')

            file.write('Nombre: ' + contact_name + '\r\n')
            file.write('Teléfono: ' + phone + '\r\n')
            file.write('Categoría: ' + category + '\r\n')
            file.write('\r\n')
            print('Contacto editado correctamente.')
        os.rename(CARPETA + previus_name + EXTENSION,
                  CARPETA + contact_name + EXTENSION)
        print('Contacto editado correctamente.')
    else:
        print('El contacto no existe.')


def show_contacts():
    files = os.listdir(CARPETA)
    files_txt = [i for i in files if i.endswith(EXTENSION)]

    for file in files_txt:
        with open(CARPETA + file) as contact:
            for line in contact:
                print(line.rstrip())
            print('\r\n')


def delete_contact():
    name = input('Escribe el nombre del contacto a eliminar: ')
    is_a_contact = is_there(name)
    if not is_a_contact:
        print('El contacto no existe.')
        return
    else:
        os.remove(CARPETA + name + EXTENSION)
        print('Contacto eliminado correctamente.')


def search_contact():
    name = input('Escribe el nombre del contacto a buscar: ')
    is_a_contact = is_there(name)
    if not is_a_contact:
        print('El contacto no existe.')
        return
    else:
        with open(CARPETA + name + EXTENSION) as file:
            for line in file:
                print(line.rstrip())
            print('\r\n')


def is_there(name):
    return os.path.isfile(CARPETA + name + EXTENSION)


app()
