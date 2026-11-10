from tkinter import Label, Button, Entry, Tk, messagebox
from coches.cochesBD import CochesBD

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x800")
        self.ventana.resizable(0, 0)
        self.main()
        
    def esperarTecla(self):
        input("... ¡Oprima cualquier tecla para continuar! ...")

    # Vistas y Limpieza de Pantalla
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="\n\t...::: M E N U   P R I N C I P A L :::...\n\t").pack(pady=20)
        Button(self.ventana, text="\n\t 1.- Coches\n\t", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana, text="\n\t 2.- Salir \n\t", command=self.ventana.quit).pack(pady=5)

    def menu_acciones(self):
        self.borrarPantalla()
        self_tipo = "C O C H E S"
        Label(self.ventana, text=f"\n\t...::: M E N U   {self_tipo} :::...\n\t").pack(pady=20)
        Button(self.ventana, text="\n\t 1.- Agregar\n\t", command=self.insertar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 2.- Borrar \n\t", command=self.eliminar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 3.- Modificar\n\t", command=self.modificar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 4.- Consultar \n\t", command=self.consultar_view).pack(pady=5)
        Button(self.ventana, text="\n\t 5.- Salir \n\t", command=self.main).pack(pady=5)
             
    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar los datos del coche...").pack(pady=10)
        
        Label(self.ventana, text="Marca").pack(pady=5)
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)
        
        Label(self.ventana, text="Color").pack(pady=5)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)
        
        Label(self.ventana, text="Modelo").pack(pady=5)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)
        
        Label(self.ventana, text="Velocidad").pack(pady=5)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana, text="Potencia").pack(pady=5)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)
        
        Label(self.ventana, text="Asientos").pack(pady=5)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)
        
        Button(self.ventana, text="Guardar", command=self.insertar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del Coche a borrar...").pack(pady=10)
        
        Label(self.ventana, text="ID del Coche").pack(pady=5)
        self.id_coche = Entry(self.ventana)
        self.id_coche.focus()
        self.id_coche.pack(pady=5)

        Button(self.ventana, text="Borrar", command=self.eliminar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Modificar datos del coche...").pack(pady=10)
        
        Label(self.ventana, text="ID del coche a modificar").pack(pady=5)
        self.id_coche = Entry(self.ventana)
        self.id_coche.focus()
        self.id_coche.pack(pady=5)

        Label(self.ventana, text="Nueva Marca").pack(pady=5)
        self.marca = Entry(self.ventana)
        self.marca.pack(pady=5)
        
        Label(self.ventana, text="Nuevo Color").pack(pady=5)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)
        
        Label(self.ventana, text="Nuevo Modelo").pack(pady=5)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)
        
        Label(self.ventana, text="Nueva Velocidad").pack(pady=5)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana, text="Nueva Potencia").pack(pady=5)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)
        
        Label(self.ventana, text="Nuevos Asientos").pack(pady=5)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)
        
        Button(self.ventana, text="Modificar", command=self.modificar_controller).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Consultar los coches").pack(pady=10)
        filas = ""
        filas = self.consulta_controller(filas)
        Label(self.ventana, text=f"{filas}").pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    # Controladores
    def respuesta_sql(self, respuesta):
        if respuesta:   
            messagebox.showinfo(title="Exitoso", message="...¡Acción Realizada con Éxito!...")
        else:
            messagebox.showerror(title="Error", message="Esta acción no pudo realizarse")   

    def insertar_controller(self):
        coche1 = CochesBD(
            self.marca.get(), 
            self.color.get(), 
            self.modelo.get(), 
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)

    def eliminar_controller(self):
        id_val = self.id_coche.get()
        respuesta = CochesBD.eliminar(id_val)
        self.respuesta_sql(respuesta)

    def consulta_controller(self, filas):
        coche1 = CochesBD('', '', '', 0, 0, 0)
        registros = coche1.consultar()
        if registros and len(registros) > 0:
            num_coches = 1
            for fila in registros:
                filas = filas + (f"\nCoche # {num_coches}\t ID: {fila[0]}\t Marca: {fila[1]}\n\t Color: {fila[2]}\t Modelo: {fila[3]}\n\t Velocidad: {fila[4]}\t Potencia: {fila[5]}\n\t Asientos: {fila[6]}\n")
                num_coches += 1
        else:
            filas = ("\n\t... No hay registros de coches ...")
        return filas

    def modificar_controller(self):
        id_val = self.id_coche.get()
        coche1 = CochesBD(
            self.marca.get(), 
            self.color.get(), 
            self.modelo.get(), 
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )
        respuesta = coche1.actualizar(id_val) if hasattr(coche1, 'actualizar') else coche1.modificar(id_val)
        self.respuesta_sql(respuesta)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()


    

