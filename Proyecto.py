import os 
def logueo():  #Solo estos nombres estan registrados
    usuarios = ["Adriana","Daniela","Hersal"]
    claves = ['1234','6678','0066']
   
    separador()
    nombre = input('Escriba el usuario: ')
    clave = input('Ingrese la Contraseña: ')

    encontrado = False
    for idx in range(len(usuarios)):
        if (nombre == usuarios[idx]) and (clave == claves[idx]):
            encontrado = True
            continue
    if (encontrado):
        opcion2 = 0
        salir = False
        while not salir:
            print ("1. Registros")
            print ("2. Ficha Clínica")     
            print ("3. Venta de productos")   
            print ("4. Historial")  
            print ("6. Salir")
            opcion2 = pedirNumero()
            if opcion2 == 1:
                registros()
            elif opcion2 == 2:
                Ficha_Clinica()
            elif opcion2 == 3:
                Venta_Productos()
            elif opcion2 == 4:
                Historial()
            elif opcion2 == 6:
                salir = True
    else:
        print("¡Algún dato es incorrecto!")

def crear_archivo():
        nuevos=open("registrosnuevos.txt", "w")
        Nombre=input("Ingrese su Nombre: ")
        Cedula=input("Ingrese su número de cédula: ")
        Telefono=input("Ingrese su número de teléfono: ")
        Correo_Electronico=input("Ingrese su Correo Electrónico: ")
        Direccion=input("Ingrese su dirección: ")
        Datos_de_Mascota_Nombre=input("Ingrese el nombre de su mascota: ")
        tipo_mascota=input("Ingrese el tipo de mascota: ")
        Raza=input("Ingrese la raza de su mascota: ")
        Fecha_de_Nacimiento=input("Ingrese la fecha de nacimiento de su mascota: ")
        Sexo=input("Ingrese el sexo de su mascota: ")
        Peso=input("Ingrese el peso de su mascota: ")
        Caracteristicas=input("Que características tiene su mascota: ")
        Alimento=input("Que alimento consume su mascota: ")
        Observaciones=input("Observaciones de la mascota: ")
        aux=Nombre +" | " + Cedula + " | " + Telefono + " | " + Correo_Electronico + " | " + Direccion + " | " + Datos_de_Mascota_Nombre + " | " + tipo_mascota + " | " + Raza + " | " + Fecha_de_Nacimiento +" | " + Sexo + " | " + Peso + " | " + Caracteristicas + " | " + Alimento + " | " + Observaciones
        print(aux, file=nuevos)
        nuevos.close()
        separador()

def separador():
    print("")
    print("=============================================")
    print("")

def registros():
    reg=open("registros.txt", "r")
    print("Abriendo Archivo.......")
    print("--------------------------------------")
    mensaje=reg.read()
    valores =mensaje.split("\n")
    for i in valores:
        print(i)
    print("Bienvenido Por Favor Ingresar datos")
    print("-------------------------------------")
    if os.path.isfile('registrosnuevos.txt'):
        print("-----------")
        print('El archivo existe.')
        print("-----------\n")
        nuevos=open("registrosnuevos.txt", "a")
        Nombre=input("Ingrese su Nombre: ")
        Cedula=input("Ingrese su número de cédula: ")
        Telefono=input("Ingrese su número de teléfono: ")
        Correo_Electronico=input("Ingrese su Correo Electrónico: ")
        Direccion=input("Ingrese su dirección: ")
        Datos_de_Mascota_Nombre=input("Ingrese el nombre de su mascota: ")
        tipo_mascota=input("Ingrese el tipo de mascota: ")
        Raza=input("Ingrese la raza de su mascota: ")
        Fecha_de_Nacimiento=input("Ingrese la fecha de nacimiento de su mascota: ")
        Sexo=input("Ingrese el sexo de su mascota: ")
        Peso=input("Ingrese el peso de su mascota: ")
        Caracteristicas=input("Que características tiene su mascota: ")
        Alimento=input("Que alimento consume su mascota: ")
        Observaciones=input("Observaciones de la mascota: ")
        aux=Nombre +" | " + Cedula + " | " + Telefono + " | " + Correo_Electronico + " | " + Direccion + " | " + Datos_de_Mascota_Nombre + " | " + tipo_mascota + " | " + Raza + " | " + Fecha_de_Nacimiento +" | " + Sexo + " | " + Peso + " | " + Caracteristicas + " | " + Alimento + " | " + Observaciones
        print(aux,file=nuevos)
        nuevos.close() 
        print("Sus registros fueron creados")
        separador()
    else:
        crear_archivo()
        
def Ficha_Clinica():
            menusecundario=int(input("Elija su cita: \n 1-Agende su cita \n 2-Agende su cita de Vacunación \n 0-Salir \n "))
            while menusecundario !=0:
                if menusecundario == 1:
                    print("Bienvenido a la Clínica ")
                    print("A continuacion ingrese los datos correspondientes para agendar una cita")
                    if os.path.isfile('citas.txt'):
                        print("------------------------")
                        citas = open("citas.txt", "w")
                        nombre = input("Nombre cliente:")
                        apellido = input("Apellido cliente: ")
                        fecha = input("Fecha que desea su cita: ")
                        motivo = input("Motivo de su cita: ")
                        print(fecha,nombre,apellido,motivo,"\n", file=citas)
                        print("------------------------------------")
                        print("Su cita ha sido guardada con éxito!")
                        citas.close()
                        break

                    else:
                        citas=open("citas.txt", "a")
                        nombre = input("Nombre cliente:") 
                        apellido = input("Apellido cliente: ")
                        fecha = input("Fecha que desea su cita: ")
                        motivo = input("Motivo de su cita: ")
                        print(fecha,nombre,apellido,motivo,"\n", file=citas)
                        print("------------------------------------")
                        print("Su cita ha sido guardada con éxito!")
                        citas.close()
                        break

                elif menusecundario == 2:
                    print("Bienvenido a la Clínica, Esta es la vacunación a cumplir.")
                    if os.path.isfile('citavacunacion.txt'):
                        citv=open("citavacunacion.txt", "a")
                        nombre = input("Nombre cliente:") 
                        apellido = input("Apellido cliente: ")
                        fecha = input("Fecha que desea su cita: ")
                        tipoMascota = input("El tipo de mascota: ")
                        print(fecha,nombre,apellido,tipoMascota,"\n", file=citv)
                        print("------------------------------------")
                        print("Su cita ha sido guardada con éxito!")
                        citv.close()

                    else:
                        print("El archivo ya existe....")
                        citv=open("citavacunacion.txt", "w")
                        nombre = input("Nombre cliente:") 
                        apellido = input("Apellido cliente: ")
                        fecha = input("Fecha que desea su cita: ")
                        tipoMascota = input("El tipo de mascota: ")
                        print(fecha,nombre,apellido,tipoMascota,"\n", file=citv)
                        print("------------------------------------")
                        print("Su cita ga sido guardada con éxito!")
                        citv.close()

                    if tipoMascota == "Perro" or tipoMascota == "perro":
                        os.path.isfile('citavacunacion.txt')
                        citv=open("citavacunacion.txt", "a")
                        print("1.Vacuna contra el parvovirus y moquillo. Se aplica a las 6 primeras semanas de vida.", file=citv)
                        print("2.Vacuna Polivalente. Protege contra parvovirus, virus del moquillo, virus de Parainfluenza, virus de la hepatitis y leptospi, debe colocarse a los 2 meses de edad.", file=citv)
                        print("3.Refuerzo de la vacuna polivalente, se administra a los 3 meses de vida del perro.", file=citv) 
                        print("4.Vacuna contra la rabia y segundo refuerzo de vacuna polivalente a los 4 meses de edad.", file=citv) 
                        print("5.Refuerzo de vacuna contra la rabia y polivalente. Se coloca al año de vida del cachorro. \n ", file=citv)
                        citv.close()
                        print("El archivo se creó.......")
                        break

                    elif tipoMascota == "Gato" or tipoMascota == "gato":
                        os.path.isfile('citavacunacion.txt')
                        citv=open("citavacunacion.txt", "a")
                        print("1.Rabia, aplicar esta vacuna es un requisito legal en algunos países debido a que es mortal y puede transmitirse a humanos con una mordedura.", file=citv)
                        print("2.Trivalente contra rinotraqueitis, calicivirus y panleucopenia.", file=citv)
                        print("""3.Rinotraqueitis, es provocada por el virus del herpes felino común. Los síntomas incluyen estornudos, secreción nasal y babeo. Los ojos de tu 
gato pueden tener costras mucosas, que provocarán mucho más molestias y a la vez, lo harán comer mucho menos de lo normal. Si no se trata, esta enfermedad causa deshidratación, inanición y, finalmente, la muerte""", file=citv)
                        print("""4.Calicivirus tiene síntomas similares que afectan el sistema respiratorio y también causan úlceras en la boca. 
Puede provocar neumonía si no se trata: los gatitos y los gatos mayores son especialmente vulnerables.""", file=citv)
                        print("5.La panleucopenia también se conoce como moquillo y se transmite fácilmente de un gato a otro. El moquillo es tan común que casi todos los gatos", file=citv)
                        print("6.Leucemia felina, si algún gato en tu hogar pasa tiempo al aire libre o es de los que escapa a menudo, también debes vacunarlo contra el virus. \n ", file=citv)            
                        citv.close()
                        print("El archivo se creó.......")
                        break

                    elif tipoMascota != "gato" and tipoMascota != "perro":
                        os.path.isfile('citavacunacion.txt')
                        citv=open("citavacunacion.txt", "a")
                        print("Vacunas en Hurones:", file=citv)
                        print("1.Vacuna contra el moquillo", file=citv)
                        print("Vacunas para suricatos:", file=citv)
                        print("1.Vacuna contra la Panleucopenia felina", file=citv)
                        print("Vacunas en cerdos como animal de compañia:", file=citv)
                        print("1.Vacuna de parvovirus erysipelothrix rhusiopathiae conocido como (mal rojo) \n ", file=citv )
                        citv.close()
                        
def Venta_Productos():
    def monto_descuento(cantidad_precio,descuento):
        resultado_monto_descuento = cantidad_precio*descuento/100
        return resultado_monto_descuento

    def descontado(cantidad_precio,a_descontar):
        resultado_descontado= cantidad_precio-a_descontar
        return resultado_descontado

    def iva(cantidad_menos_descuento,porcentaje_iva):
        resultado_iva = cantidad_menos_descuento*porcentaje_iva/100
        return resultado_iva

    def pago_final(cantidad_menos_descuento,a_cobrar_iva):
        resultado_final=cantidad_menos_descuento+a_cobrar_iva
        return resultado_final
    
    def retorna_precio(codigo,list_productos):
        for x in range(len(list_productos)):
            if str(list_productos[x][0])==str(codigo):
                return int(list_productos[x][2])

    def retorna_nombre(codigo,list_productos):
         for x in range(len(list_productos)):
            if str(list_productos[x][0])==str(codigo):
                return (list_productos[x][1])
    
    list_productos=[["COD ","NOMBRE                 ","PRECIO"],
               ["--------------------------------------"],
               ["001","Pro-Plan Exigente 3Kg  ","14400"],
               ["002","Pro-Plan Exigente 1Kg  ","5300"],
               ["003","Alpo Carne 4Kg         ","6130"],
               ["004","Alpo Carne 2Kg         ","3110"],
               ["005","Beneful 4Kg            ","11200"],
               ["006","Beneful 2Kg            ","6600"],
               ["007","Dog Chow 4Kg           ","10000"],
               ["008","Dog Chow 2Kg           ","5000"],
               ["--------------------------------------"],
               ["       ALIMENTO PARA CACHORRO      "],
               ["--------------------------------------"],
               ["COD","NOMBRE                 ","PRECIO"],
               ["009","Beneful Puppy 10.1Kg   ","21000"],
               ["010","Beneful Puppy 4Kg      ","11200"],
               ["011","Beneful Puppy 2Kg      ","6600"],
               ["012","Hills Puppy 7Kg        ","36000"],
               ["013","Hills Puppy 2Kg        ","11200"],
               ["014","Maxi Dog Cachorro 1.5Kg","1800"],
               ["--------------------------------------"],
               ["        ALIMENTO FELINO            "],
               ["--------------------------------------"],
               ["COD","NOMBRE                 ","PRECIO"],
               ["--------------------------------------"],
               ["015","Hills Felino 1.81Kg    ","14700"],
               ["016","Hills Felino 3.18Kg     ","25000"],
               ["--------------------------------------"],
               ["        ACCESORIOS           "],
               ["--------------------------------------"],
               ["017","Pechera Ruffwear       ","41000"],
               ["018","Spunky Bola            ","6500"],
               ["019","Correa Ruffwear        ","30000"]]

    for l in range(len(list_productos)):
        print(*list_productos[l])
    os.path.isfile('factura.txt')
    fact = open("factura.txt","w")
    historial= open("ListaProductos.txt","w")
    lista_compras = [[],[]]
    nombreCliente = input("Ingrese el nombre del cliente: ")
    compra_nueva = "si"
    cantidadtotal = 0
    cantidadprecio = 0
    while compra_nueva == "si":     #Solo si es "si" va seguir el codigo
        codigo = input("Ingrese el COD del producto a comprar: ")
        precio=retorna_precio(codigo,list_productos)
        nombre=retorna_nombre(codigo,list_productos)
        print(nombre,precio)
        print("--------------------------------------------------------")
        cantidad = int(input("Ingrese la cantidad: "))
        precio_total_productos=precio*cantidad
        cantidadprecio += precio_total_productos
        cantidadtotal += cantidad
        compra_nueva = input("Quiere comprar otro producto si/no: ")
        lista_compras[1].append(nombre)
        lista_compras[0].append(cantidad)
        continue

    descuento = int(input("Porcentaje del descuento: "))
    a_descontar = monto_descuento(cantidadprecio,descuento)
    cantidad_menos_descuento = descontado(cantidadprecio,a_descontar)
    porcentaje_iva = int(input("Porcetaje a cobrar de IVA: "))
    a_cobrar_iva = iva(cantidad_menos_descuento,porcentaje_iva)
    monto_final = pago_final(cantidad_menos_descuento,a_cobrar_iva)
    print("Factura Electronica FamilyPets \nNombre:",nombreCliente,"\nProductos: ",*lista_compras[1],"Total de productos:",cantidadtotal,"\nSubTotal:",cantidadprecio,"\nDescuento:",a_descontar,"\nProductos menos descuento:",cantidad_menos_descuento,"\nIva",porcentaje_iva,"%:",a_cobrar_iva,"\nTotal:",monto_final,"\n", file=fact)
    print(*lista_compras[1], file=historial)
    historial.close()
    fact.close()
    print("----------------------------------")
    print("Su factura se creó.")
    print("----------------------------------")

def Historial():
    def Historial_Ficha():
        reg=open("citas.txt", "r")
        print("Abriendo Historial De Fichas Clínicas.......")
        print("--------------------------------------")
        mensaje=reg.read()
        valores =mensaje.split("\n")
        for i in valores:
            print(i)
        separador()

    def Historial_Citas():
        reg2=open("citavacunacion.txt", "r")
        print("Abriendo Historial De Citas Clínicas.......")
        print("--------------------------------------")
        mensaje = reg2.read()
        valores = mensaje.split("\n")
        for i in valores:
            print(i)
        separador()

    def Historial_Productos():
        reg2=open("ListaProductos.txt", "r")
        print("Abriendo Historial De Productos.......")
        print("--------------------------------------")
        mensaje = reg2.read()
        valores = mensaje.split("\n")
        for i in valores:
            print(i)
        separador()

    opcion3 = 0
    salir = False
    while not salir:
        print ("1. Historial Ficha Clínica")
        print ("2. Historial Citas Programadas")     
        print ("3. Historial De Venta Productos")     
        print ("6. Salir")
        opcion3 = pedirNumero()
        if opcion3 == 1:
            Historial_Ficha()
        elif opcion3 == 2:
            Historial_Citas()
        elif opcion3 == 3:
            Historial_Productos()
        elif opcion3 == 6:
            salir = True

def pedirNumero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Por favor ingrese algún número de opción: "))
            correcto=True
        except ValueError:
            print('Error, Ingrese un número entero')
    return num
salir = False
opcion = 0
while not salir:
    print ("1. Logueo")   
    print ("6. Salir")
    opcion = pedirNumero()
    if opcion == 1:
        logueo()
    elif opcion == 6:
        salir = True
    else:
        print ("Ingrese una opción entre 1 y 6")

