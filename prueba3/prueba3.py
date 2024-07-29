import reflex as rx
import os
import time
from dotenv import load_dotenv
from datetime import datetime, timedelta
from supabase import create_client, Client
from typing import Any
from prueba3.style.style import *


class Total(rx.Base):
    id:int 
    semana:str
    dia:str
    fecha:str
    hora:str
    mails:list
    lugar_disponible:int

class Usuarios(rx.Base):
    id:int
    usuario:str 
    clases_disponibles:int
    recuperar:int
    trigger_alert:int
   

class Semanas(rx.Base):
    id:int 
    numero_semana:str

class Dias(rx.Base):
    id:int
    id_semana:int
    dia_semana:str

class Horarios(rx.Base):
    id:int
    id_dia:int
    hora_inicio:str
    hora_fin:Any


class Alumnos(rx.Base):
    id:int
    mails:list
    id_horario:Any

class Fechas(rx.Base):
    id :int
    fecha:str
    dia_id:int

async def confirmar_usuario_en_semana() -> str:
    return supabase.confirmar_usuario_en_semana()

async def data_usuarios() -> list[Usuarios]:       
        return supabase.data_usuarios()   

    
async def data_total() -> list[Total]:       
        return supabase.data_total()   

async def data_semanas() -> list[Semanas]:       
        return supabase.data_semanas()
    
async def data_dias() -> list[Dias]:        
        return supabase.data_dias()
    
async def data_horarios() -> list[Horarios]:        
        return supabase.data_horarios()
    
async def data_alumnos() -> list[Alumnos]:      
        return supabase.data_alumnos()

class PageState(rx.State):

    semanas_info:list[Semanas]
    dias_info:list[Dias]
    horarios_info:list[Horarios]
    alumnos_info:list[Alumnos]
    total_info:list[Total]
    usuarios_info:list[Usuarios]
    fecha: str = "15/07"
    cap_max:int = 7 
    user:str 
    hora_prueba:str
    fecha_prueba:str
    id_prueba:int
    semana:str = "semana1"
    indice: int = 0  
    fecha_actual = datetime.now()
    limite_recuperacion = timedelta(hours=24)
    user_email: str = ""
    user_cached: str = None
    

    def siguiente(self):
        if self.semana == "semana1" :
            self.semana = "semana2"
        elif self.semana == "semana2":
            self.semana = "semana3"
        elif self.semana == "semana3" :
            self.semana = "semana4"
        elif self.semana == "semana4" :
            self.semana = "semana5"
        elif self.semana == "semana5" :
            self.semana = "semana1"
        
    
    def anterior(self):
        if self.semana == "semana1" :
            self.semana = "semana5"
        elif self.semana == "semana5" :
            self.semana = "semana4"
        elif self.semana == "semana4" :
            self.semana = "semana3"
        elif self.semana == "semana3" :
            self.semana = "semana2"
        elif self.semana == "semana2" :
            self.semana = "semana1"
                

    async def usuarios(self):
        self.usuarios_info = await data_usuarios()
    
    async def total(self):
        self.total_info = await data_total()

    async def semanas(self):
        self.semanas_info = await data_semanas()
    
    async def dias(self):
        self.dias_info = await data_dias()

    async def horarios(self):
        self.horarios_info = await data_horarios()

    async def alumnos(self):
        self.alumnos_info = await data_alumnos()

    def handle_submit(self, form_data: dict):
        self.fecha = form_data["select"]

    
    async def insertar_usuario(self, form_data: dict) -> int:
        self.user = form_data["user"]
        self.hora_prueba = form_data["hora"]
        self.fecha_prueba = form_data["fecha"]
        for i in await data_total():
            if i.hora == form_data["hora"] and i.fecha == form_data["fecha"]:
                self.id_prueba = i.id
        
        supabase.agregar_usuario_a_horario(self.id_prueba, self.user, False)

    async def remover_usuario(self, form_data: dict) -> int:
        self.user = form_data["user"]
        self.hora_prueba = form_data["hora"]
        self.fecha_prueba = form_data["fecha"]
        for i in await data_total():
            if i.hora == form_data["hora"] and i.fecha == form_data["fecha"]:
                self.id_prueba = i.id
        
        supabase.eliminar_usuario_a_horario(self.id_prueba, self.user)
        
    @rx.var
    def filtered_list_fecha(self) -> list[Total]:
        return [item for item in self.total_info if item.fecha == self.fecha]

    @rx.var
    def filtered_list_semana(self) -> list[Total]:
        result = []
        days_seen = set()  

        for item in self.total_info:
            if item.semana == self.semana:  
                if item.dia not in days_seen:  
                    result.append(item)
                    days_seen.add(item.dia) 
        return result 
    
    @rx.var
    def filtered_list_lunes(self) -> list[Total]:
        result = []
        hours_seen = set()  
        
        for i in self.total_info:
            if i.dia == "lunes" and i.semana == self.semana:
                if i.hora not in hours_seen:
                    result.append(i)
                    hours_seen.add(i.hora)
        return result
    
    @rx.var
    def filtered_list_martes(self) -> list[Total]:
        result = []
        hours_seen = set()  
        
        for i in self.total_info:
            if i.dia == "martes" and i.semana == self.semana:
                if i.hora not in hours_seen:
                    result.append(i)
                    hours_seen.add(i.hora)
        return result
    
    @rx.var
    def filtered_list_miercoles(self) -> list[Total]:
        result = []
        hours_seen = set()  
        
        for i in self.total_info:
            if i.dia == "miercoles" and i.semana == self.semana:
                if i.hora not in hours_seen:
                    result.append(i)
                    hours_seen.add(i.hora)
        return result
    
    @rx.var
    def filtered_list_jueves(self) -> list[Total]:
        result = []
        hours_seen = set()  
        
        for i in self.total_info:
            if i.dia == "jueves" and i.semana == self.semana:
                if i.hora not in hours_seen:
                    result.append(i)
                    hours_seen.add(i.hora)
        return result
    
    @rx.var
    def filtered_list_viernes(self) -> list[Total]:
        result = []
        hours_seen = set()  
        
        for i in self.total_info:
            if i.dia == "viernes" and i.semana == self.semana:
                if i.hora not in hours_seen:
                    result.append(i)
                    hours_seen.add(i.hora)
        return result
    
    
    @rx.var
    def check_recuperar(self) -> int:
        result = 0
        for i in self.usuarios_info:
            if i.usuario == self.obtener_user:
                result = i.recuperar 
        return result
    
    @rx.var
    def check_cant_clases(self) -> int:
        result = 0
        for i in self.usuarios_info:
            if i.usuario == self.obtener_user:
                result = i.clases_disponibles 
        return result
    
    @rx.var
    def check_trigger_alert(self) -> int:
        result = 0
        for i in self.usuarios_info:
            if i.usuario == self.obtener_user:
                result = i.trigger_alert 
        return result
    
    @rx.var
    def obtener_clases_user(self) -> list : 
        
        result = []
        
        for i in self.total_info:
            if self.obtener_user in i.mails:
                result.append(i)  
        return result  
    
    @rx.var
    def tiempo_hasta_clase(self) -> list[float]:

        año_actual = self.fecha_actual.year
        return [
            (datetime.strptime(f"{año_actual}/{item.fecha} {item.hora}", "%Y/%d/%m %H:%M") - self.fecha_actual).total_seconds() / 3600
            for item in self.total_info
        ]
    
    @rx.var
    def proxima_clase(self) -> tuple:

        año_actual = self.fecha_actual.year

        clases_futuras = [
            (item, datetime.strptime(f"{año_actual}/{item.fecha} {item.hora}", "%Y/%d/%m %H:%M"))
            for item in self.obtener_clases_user
            if datetime.strptime(f"{año_actual}/{item.fecha} {item.hora}", "%Y/%d/%m %H:%M") > self.fecha_actual
        ]
        if clases_futuras:
            return min(clases_futuras, key=lambda x: x[1])
        return None, None

    @rx.var
    def tiempo_hasta_proxima_clase(self) -> str:
        clase, tiempo = self.proxima_clase
        if clase and tiempo:
            diferencia = tiempo - datetime.now()
            dias = diferencia.days
            horas = diferencia.seconds // 3600
            minutos = (diferencia.seconds % 3600) // 60
            return f"Faltan {dias} días, {horas} horas y {minutos} minutos para tu próxima clase"

    @rx.var
    def obtener_user(self) -> str:
        if self.user_cached:
            return self.user_cached

        user_info = supabase.supabase.auth.get_user()
        if user_info:
            self.user_cached = user_info.user.email
            return self.user_cached
        return ""

    
    def actualizar_user(self):
        user = self.obtener_user
        if user:
            self.user_email = user  
        self.user_cached = None
        
    @rx.var
    def horarios_user(self) -> list:
        info = []
        
        for i in self.total_info:
            if self.obtener_user in i.mails:
                info.append(i)
        return info
                

        
class ReservaCancela(rx.State):
    
    async def reset_database(self):
        reset = reset_databasee()
        return reset
    
    
    async def eliminar_usuario(self, id, user):
        eliminar = eliminar_usuarioo(id, user)
        return eliminar

    async def agregar_usuario(self, id, user, parametro):
        agregar = agregar_usuarioo(id, user, parametro)
        return agregar

    
    async def sign_out(self):
        out = sign_outt()
        return out
    
def reset_databasee():
    supabase.reset_data_base()

    
def eliminar_usuarioo(id, user):
    supabase.eliminar_usuario_a_horario(id, user)

def agregar_usuarioo(id, user, parametro):
    supabase.agregar_usuario_a_horario(id, user, parametro)


def sign_outt():
    supabase.sign_out()


class ButtonState(rx.State):

    show_text_lunes: bool = False
    show_text_martes: bool = False
    show_text_miercoles: bool = False
    show_text_jueves: bool = False
    show_text_viernes: bool = False

    def toggle_text(self, dia):
        if dia == "lunes":
            self.show_text_lunes = not self.show_text_lunes
        elif dia == "martes":
            self.show_text_martes = not self.show_text_martes
        elif dia == "miercoles":
            self.show_text_miercoles = not self.show_text_miercoles
        elif dia == "jueves":
            self.show_text_jueves = not self.show_text_jueves
        elif dia == "viernes":
            self.show_text_viernes = not self.show_text_viernes
            
    def reset_dias(self):
        if self.show_text_lunes == True:
            self.show_text_lunes= False
        if self.show_text_martes == True:
            self.show_text_martes= False
        if self.show_text_miercoles == True:
            self.show_text_miercoles= False
        if self.show_text_jueves == True:
            self.show_text_jueves= False
        if self.show_text_viernes == True:
            self.show_text_viernes= False
        

class Login(rx.State):

    email:str
    password:str
    user_info:dict


    def registrar_usuario_submit(self, form_data):

        usuarios = []
        ids = []

        self.email = form_data["email"]
        self.password = form_data["password"]
        data = supabase.supabase.auth.sign_up(credentials={"email": form_data["email"], "password": form_data["password"]})

        for i in supabase.data_usuarios():
            usuarios.append(i.usuario)
            ids.append(i.id)
        id=max(ids)
        id+=1
        if form_data["email"] not in usuarios:
            response = (supabase.supabase.table("usuarios").insert({"id": id ,"usuario": form_data["email"], "clases_disponibles": 0, "recuperar":0, "trigger_alert": 0}).execute())
    
    def iniciar_sesion_submit(self, form_data):
        self.email = form_data["email"]
        self.password = form_data["password"]
        data = supabase.supabase.auth.sign_in_with_password({"email": form_data["email"], "password": form_data["password"]})
        print(data.user.email)
        print(data.user.id)
        
        PageState.actualizar_user()





        
        

class SupaBase():

    load_dotenv()

    URL: str = os.environ.get("URL")
    KEY: str = os.environ.get("KEY")

    supabase: Client = create_client(URL, KEY)

    def data_total(self) -> list[Total]:
        
        total_class = []

        total = self.supabase.table("total").select("*").execute()
        
        for i in total.data:
            total_class.append(Total(id=i["id"], semana=i["semana"], dia=i["dia"], fecha=i["fecha"], hora=i["hora"], mails=i["mails"], lugar_disponible=i["lugar_disponible"]))
        total_list_sorted = sorted(total_class, key=lambda alumno: alumno.id)
        return total_list_sorted
    
        
    def data_usuarios(self) -> list[Usuarios]:

        usuarios_class = []

        usuarios = self.supabase.table("usuarios").select("*").execute()

        for i in usuarios.data:
            usuarios_class.append(Usuarios(id=i["id"], usuario=i["usuario"], clases_disponibles=i["clases_disponibles"], recuperar=i["recuperar"], trigger_alert=i["trigger_alert"]))
        return usuarios_class



    def data_semanas(self) -> list[Semanas]:
        semanas_class = []

        semanas = self.supabase.table("semanas").select("*").execute()
        
        for i in semanas.data:
            semanas_class.append(Semanas(id=i["id"], numero_semana=i["numero_semana"],))
        return semanas_class
    
    def data_dias(self) -> list[Semanas]:
        dias_class = []

        dias = self.supabase.table("dias").select("*").execute()
        for i in dias.data:
            dias_class.append(Dias(id=i["id"], id_semana=i["id_semana"], dia_semana=i["dia_semana"]))
        return dias_class
    
    def data_horarios(self) -> list[Horarios]:
        horarios_class = []

        horarios = self.supabase.table("horarios").select("*").execute()
        
        for i in horarios.data:
            print
            horarios_class.append(Horarios(id=i["id"], id_dia=i["id_dia"], hora_inicio=i["hora_inicio"], hora_fin=i["hora_fin"] ))
        return horarios_class
    
    def data_alumnos(self) -> list[Alumnos]:
        alumnos_class = []
        alumnos = self.supabase.table("alumnos").select("*").execute()
        
        for i in alumnos.data:
            alumnos_class.append(Alumnos(id=i["id"], mails=i["mails"],id_horario=i["id_horario"]))               
        alumnos_list_sorted = sorted(alumnos_class, key=lambda alumno: alumno.id)
        return alumnos_list_sorted
        

    def data_fechas(self) -> list[Fechas]:
        fechas_class = []

        fechas = self.supabase.table("fechas").select("*").execute()
        
        for i in fechas.data:
            fechas_class.append(Fechas(id=i["id"], fecha=i["fecha"] ,dia_id= i["dia_id"]))
        return fechas_class



    def obtener_fechas_proximas_semanas(self):
        today = datetime.now()
        
        
        last_monday = today - timedelta(days=today.weekday())
        
        fechas = []
        for i in range(5):  
            lunes = last_monday + timedelta(weeks=i)
            
            for j in range(5):  
                fecha = lunes + timedelta(days=j)
                fecha_actualizada = fecha.replace(year=today.year)
                fechas.append(fecha_actualizada.strftime("%d/%m"))
        
        return fechas

    def check_user_in_semana(self, user, semana):
        check_semana = []
        for i in self.data_usuarios():
            if i.usuario == user and semana in i.semanas:
                check_semana.append(semana)
        if len(check_semana) > 0 :
            return False
        return True
    
    def check_trigger_alert_user(self, user):
        for i in self.data_usuarios():
            if i.usuario == user :
                return i.trigger_alert
    
    
    
            
    def encontrar_diaid_con_horario(self, id ):
        for i in self.data_horarios():
            if i.id == id:
                return i.id_dia
            
    
    def actualizar_fecha(self, id):
        for index, i in enumerate(self.obtener_fechas_proximas_semanas()):
            if index + 1 == id:
                return i
        
    
    def cant_clases_usuario(self, user):

        for i in self.data_usuarios():
            if user == i.usuario:
                return i.clases_disponibles
    
    def recuperar_clase(self, user):
        recupera = 0
        for i in self.data_usuarios():
            if user == i.usuario:
                return i.recuperar
                        
    
    def id_usuario(self, user):

        for i in self.data_usuarios():
            if user == i.usuario:
                return i.id

    
        
    def recuperar_con_usuario(self, usuario):
        for i in self.data_usuarios():
            if i.usuario == usuario:
                return i.recuperar
      
    def trigger_alert_con_usuario(self, usuario):
        for i in self.data_usuarios():
            if i.usuario == usuario:
                return i.trigger_alert      
    
    def agregar_usuario_a_horario(self, id, user, parametro):

        
        for data in self.data_total():
            if data.id == id:
                if user not in data.mails:
                    if self.cant_clases_usuario(user) > 0 or self.recuperar_clase(user) > 0 or not parametro:
                        alumnos = data.mails
                        alumnos.append(user)
                        lugar_disponible = data.lugar_disponible
                        lugar_disponible -= 1
                        response = (self.supabase.table("total").update({"mails": alumnos}).eq("id", id).execute())
                        response = (self.supabase.table("total").update({"lugar_disponible": lugar_disponible}).eq("id", id).execute())
                        if self.cant_clases_usuario(user) > 0:
                            response = (self.supabase.table("usuarios").update({"clases_disponibles": self.cant_clases_usuario(user) - 1}).eq("id", self.id_usuario(user)).execute())
                        for i in self.data_usuarios():
                            if i.recuperar > 0:
                                response = (self.supabase.table("usuarios").update({"recuperar": self.recuperar_clase(user) - 1}).eq("id", self.id_usuario(user)).execute())
                
    

    def eliminar_usuario_a_horario(self, id, user):
        
        for data in self.data_total():
            if data.id == id:
                if user in data.mails:
                    alumnos = data.mails
                    alumnos.remove(user)
                    lugar_disponible = data.lugar_disponible
                    lugar_disponible += 1
                    response = (self.supabase.table("total").update({"lugar_disponible": lugar_disponible}).eq("id", id).execute())
                    response = (self.supabase.table("total").update({"mails": alumnos}).eq("id", id).execute())
                    if self.fecha_hora_recuperar(id, user):
                        response = (self.supabase.table("usuarios").update({"recuperar": self.recuperar_con_usuario(user) + 1}).eq("id", self.id_usuario(user)).execute())
                        if self.trigger_alert_con_usuario(user) > 0 :
                            response = (self.supabase.table("usuarios").update({"trigger_alert": 0}).eq("id", self.id_usuario(user)).execute())
    
   
    
    def sign_out(self):
        res = self.supabase.auth.sign_out()
    
    def agregar_fechas_constantemente(self):
        for i in self.data_total():
            response = (self.supabase.table("total").update({"fecha": self.actualizar_fecha(self.encontrar_diaid_con_horario(i.id)) }).eq("id", i.id).execute())
            
    def reset_data_base(self):
        for i in self.data_total():
            response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "Theo Rey"]}).eq("id", i.id).execute())
            response = (self.supabase.table("total").update({"lugar_disponible":0}).eq("id", i.id).execute())
            if i.fecha == "19/07" and i.hora == "16:00":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "manumanu97@hotmail.com"]}).eq("id", i.id).execute())
            if i.fecha == "26/07" and i.hora == "16:00":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "manumanu97@hotmail.com"]}).eq("id", i.id).execute())
            if i.fecha == "02/08" and i.hora == "16:00":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "manumanu97@hotmail.com"]}).eq("id", i.id).execute())
            if i.fecha == "09/08" and i.hora == "16:00":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "manumanu97@hotmail.com"]}).eq("id", i.id).execute())
            if i.fecha == "22/07" and i.hora == "17:30":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "reycamila04@gmail.com"]}).eq("id", i.id).execute())
            if i.fecha == "29/07" and i.hora == "17:30":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "reycamila04@gmail.com"]}).eq("id", i.id).execute())
            if i.fecha == "05/08" and i.hora == "17:30":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "reycamila04@gmail.com"]}).eq("id", i.id).execute())
            if i.fecha == "12/08" and i.hora == "17:30":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey", "reycamila04@gmail.com"]}).eq("id", i.id).execute())    
            if i.fecha == "16/07" and i.hora == "14:00":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey"]}).eq("id", i.id).execute())
            if i.fecha == "25/07" and i.hora == "16:30":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey"]}).eq("id", i.id).execute())
            if i.fecha == "30/07" and i.hora == "10:00":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey"]}).eq("id", i.id).execute())
            if i.fecha == "06/08" and i.hora == "14:00":
                response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey"]}).eq("id", i.id).execute())    
            if i.fecha == "16/07" and i.hora == "14:00":
                response = (self.supabase.table("total").update({"lugar_disponible": 1}).eq("id", i.id).execute())
            if i.fecha == "25/07" and i.hora == "16:30":
                response = (self.supabase.table("total").update({"lugar_disponible": 1}).eq("id", i.id).execute())
            if i.fecha == "30/07" and i.hora == "10:00":
                response = (self.supabase.table("total").update({"lugar_disponible": 1}).eq("id", i.id).execute())
            if i.fecha == "06/08" and i.hora == "14:00":
                response = (self.supabase.table("total").update({"lugar_disponible": 1}).eq("id", i.id).execute())    
                
        for i in self.data_usuarios():
            response = (self.supabase.table("usuarios").update({"clases_disponibles":0 }).eq("id", i.id).execute())
            response = (self.supabase.table("usuarios").update({"recuperar":0 }).eq("id", i.id).execute())
            response = (self.supabase.table("usuarios").update({"trigger_alert":0 }).eq("id", i.id).execute())
            
    
    def fecha_hora_recuperar(self, id, user):
        fecha_actual = datetime.now()
        limite_recuperacion = timedelta(hours=24)

        for i in self.data_total():
            if i.id == id:
                fecha_recuperar = datetime.strptime(i.fecha, "%d/%m")
                hora_recuperar = datetime.strptime(i.hora, "%H:%M")
                fecha_clase = datetime(fecha_actual.year, fecha_recuperar.month, fecha_recuperar.day,
                                    hora_recuperar.hour, hora_recuperar.minute)   
                        
                diferencia_tiempo = fecha_clase - fecha_actual                
                if diferencia_tiempo >= limite_recuperacion:
                    return True
                
                response = (self.supabase.table("usuarios").update({"trigger_alert": self.trigger_alert_con_usuario(user) + 1}).eq("id", self.id_usuario(user)).execute())
                return False
              
supabase = SupaBase()


@rx.page(
    title="index",
    description="Taller de cerámica",
    on_load= [
              PageState.total,
              PageState.actualizar_user,
              PageState.usuarios
              ]
)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        button_reset_database(),
    )



@rx.page(
    route="/turnos", 
    title="turnos",
    description="Taller de ceramica",
    on_load= [
              PageState.total,
              PageState.actualizar_user,
              PageState.usuarios
            ]
)
def turnos() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                navbar(),
                box_marron("Para inscribirse a la clase haga click en un boton que este disponible"),
                dias_semanales(),
                width = "100%"
            )
        )
    )

@rx.page(
        route="/mis_horarios",
        title="mis horarios ",
        description="Taller de ceramica",
        on_load=[
              PageState.total,
              PageState.actualizar_user,
              PageState.usuarios
            ]
)
def mis_horarios():
    return rx.box(
        rx.center(
            rx.vstack(
                navbar(),
                alert(),
                total_horarios(),
                proxima_clase_info(),
                width = "100%"  
            )
        )
    )

@rx.page(
        route="/gestion_horarios",
        title="horarios ",
        description="Taller de ceramica",
        on_load= [
              PageState.total,
              PageState.actualizar_user
            ])
def gestion_horarios():
    return rx.vstack(
        navbar(),
        rx.vstack(
            box_marron("Gestion de horarios"),
            box_marron("En esta seccion podras agregar o eliminar un usuario de una clase: "),
            form_select_fecha(),
            padding_y = "3em",
            padding_x = "0.5em"
        )
    )   


@rx.page(
        route="/crear_usuario",
        title="crear usuario ",
        description="Taller de ceramica",
        on_load= [
              PageState.actualizar_user,
            ])
def crear_usuario():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                registrar_usuario(),
                margin_top = "5em"
            )
        ),
        width="100%"  
    )

@rx.page(
        route="/iniciar_sesion",
        title="crear usuario ",
        description="Taller de ceramica",
        on_load= [
              PageState.actualizar_user,
            ])
def iniciar_sesion():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                iniciar_usuario(),
                margin_top = "5em"
            )
        ),
        width="100%"  
    )




def registrar_usuario():
    return rx.form.root(
            rx.vstack(
                rx.input(
                    labol= "Email:",
                    name="email",
                    placeholder="Ingrese su email:",
                    required=True
                ),
                rx.input(
                    labol= "Contraseña:",
                    name="password",
                    placeholder="Ingrese su contraseña:",
                    type="password",
                    required=True
                ),
                rx.button(
                    rx.text.strong("Confirmar", color= "black"), 
                    type="submit", width ="12em",
                    style=style_perla,
                    on_click=rx.redirect("/")
                )
            ),
            on_submit=Login.registrar_usuario_submit,
            reset_on_submit=True
        )

def iniciar_usuario():
    return rx.form.root(
            rx.vstack(
                rx.input(
                    labol= "Email:",
                    name="email",
                    placeholder="Ingrese su email:",
                    required=True
                ),
                rx.input(
                    labol= "Contraseña:",
                    name="password",
                    placeholder="Ingrese su contraseña:",
                    type="password",
                    required=True
                ),
                rx.button(
                    rx.text.strong("Iniciar sesion", color= "black"), 
                    type="submit", width ="12em",
                    style=style_perla,
                    on_click=rx.redirect("/")
                )
            ),
            on_submit=Login.iniciar_sesion_submit,
            reset_on_submit=True
        )
    

def insertar_usuario():
    return rx.form.root(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="user",
                        placeholder="Usuario:",
                        required=True
                    ),
                    rx.select(
                    supabase.obtener_fechas_proximas_semanas(),
                    default_value="hoy",
                    name="fecha",
                    ),
                    rx.select(
                    ["09:00", "10:00", "14:00", "16:00", "16:30", "17:30", "18:00"],
                    name="hora",
                    )
                ),
                rx.hstack(
                    rx.button(rx.text.strong("Aceptar", color= "black"), type="submit", width ="10em",style=style_perla),
                ),
                spacing="3",
                width="100%",
            ),
            on_submit=PageState.insertar_usuario,
            reset_on_submit=True,
            width="100%",
        )


def form_select_fecha():
    return rx.vstack(
        rx.form.root(
            rx.hstack(
                rx.select(
                    supabase.obtener_fechas_proximas_semanas(),
                    default_value="hoy",
                    name="select",
                ),
                submit_button(),
                width="100%",
            ),
            on_submit=PageState.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),
        rx.divider(width="100%"),
        foreach_fechas(),
        width="100%",
    )

def mostrar_clases(item):
    
    
    return rx.vstack(
        rx.cond(
            PageState.fecha.to_string() == item.fecha.to_string(),
            rx.box(box_ceramica_azul(f"El dia  {item.dia} {item.fecha} a las {item.hora} vienen {item.mails}"),
                rx.hstack(
                    trigger_insertar_usuario(),
                    trigger_remover_usuario()
                )
            )
        )
    )

def actualizar_capacidad_maxima():
    return rx.form(
        rx.vstack(
            rx.input(
                name="input",
                placeholder="cap. max",
            ),
            rx.button("ACEPTAR", type="submit"),
        ),
        on_submit=PageState.capacidad_maxima,
    )

def button_cap_max():
    return rx.button("Actualizar cap. maxima", 
    style=style_ceramica_azul)

def foreach_fechas():
    return rx.vstack(
        rx.foreach(
        PageState.filtered_list_fecha,
        mostrar_clases
    ))

def total_horarios():

    horarios = PageState.total_info
    
    return rx.vstack(
        rx.cond(horarios,
            rx.foreach(
                horarios,
                lambda item, index: text_box(item, index)
            ),
            mensaje_alerta("Todavia no esta inscripto en ninguna clase")
        ),
        padding_top= "3em"
    )
    
def mensaje_alerta(text):
    return rx.box(
        rx.hstack(
            rx.icon(tag="triangle-alert", padding = "0px"),
            rx.text.strong(text),
            spacing="1"
        ),
        style=style_perla
    )

def text_box(item, index):
   
    return rx.cond(item.mails.contains(PageState.obtener_user),
        rx.hstack(
            rx.box(
                rx.text.strong(f"Tenes clase el dia {item.dia} {item.fecha} a las {item.hora}"),
                bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
                color="#333333",
                border="2px solid #bdbdbd",
                border_radius="5px",
                box_shadow="4px 4px 8px #b3b3b3, -4px -4px 8px #ffffff",
                padding="3px",
                _hover={
                    "bg": "linear-gradient(145deg, #e0e0e0, #f5f5f5)",
                    "box_shadow": "inset 4px 4px 8px #b3b3b3, inset -4px -4px 8px #ffffff",
                },
            ),
            rx.cond(
                (PageState.tiempo_hasta_clase[index] > 24) ,
                trigger_alert(button_red(item), "Cancelacion exitosa", f"Se ha cancelado la clase del dia {item.dia} {item.fecha} a las {item.hora}. Se ha generado un credito para que puedas recuperar la clase." , "/mis_horarios"),
                trigger_alert(button_red(item), "Cancelacion exitosa", f"Se ha cancelado la clase del dia {item.dia} {item.fecha} a las {item.hora}. Ten en cuenta que no podras recuperar esta clase ya que no cumple con la condicion de cancelar con 24hs de anticipacion" , "/mis_horarios")    
            )
        )
    )

def proxima_clase_info():
    return rx.cond(PageState.user_email,
        box_perla(PageState.tiempo_hasta_proxima_clase),
        mensaje_alerta("Para ver los horarios de tus clases debes iniciar sesion")
    )
            
def submit_button():
    return rx.button(
        rx.text("Buscar", color= "black"),
        type= "submit",
        width = "9em",
        style=style_perla
    )

def dias_semanales():

    return rx.center(
        rx.vstack(
            rx.foreach(
                PageState.filtered_list_semana,
                button_prueba_dias
            ),
            rx.hstack(
                rx.button(rx.icon("arrow-left", color = "black"), on_click=PageState.anterior, style= style_perla, width = "7em"),
                rx.button(rx.icon("arrow-right", color = "black"), on_click=PageState.siguiente, style= style_perla, width = "7em"),
            ),
            width = "100%"
        ),
    )

def alert():
    return rx.vstack(
        box_marron("Antes de cancelar una clase por favor lea atentamente haciendo click en las condiciones:"),
        trigger_alert(button_rubi(),"Recuperar clase",  "Para poder recuperar una clase es indispensable cancelar con 24hs de anticipacion de lo contrario no podra ser recuperada", "/mis_horarios")
    )



def trigger_alert(button, title, dialogo,rute):
    return rx.alert_dialog.root(
            rx.alert_dialog.trigger(
                button
            ),
            rx.alert_dialog.content(
                rx.alert_dialog.title(title),
                rx.alert_dialog.description(
                    dialogo,
                ),
                rx.flex(
                    rx.alert_dialog.action(
                        aceptar_button(rute),
                    ),
                    spacing="3",
                ),
            ),
        )
    
def trigger_insertar_usuario():
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button(
            rx.text.strong("Insertar usuario", color = "black"), 
            style=style_perla, 
            width = "15em",
            margin_top ="3px"
        ),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Insertar usuario a la clase:"),
        rx.alert_dialog.description(
            rx.vstack( 
        rx.form.root(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="user",
                        placeholder="Usuario:",
                        required=True
                    ),
                    rx.select(
                    supabase.obtener_fechas_proximas_semanas(),
                    default_value="hoy",
                    name="fecha",
                    ),
                    rx.select(
                    ["09:00", "10:00", "14:00", "16:00", "16:30", "17:30", "18:00"],
                    name="hora",
                    ),
                ),rx.hstack(
                    rx.flex(
                        rx.alert_dialog.action(
                            rx.button(
                                rx.text.strong("Aceptar", color= "black"), 
                                type="submit", width ="10em",
                                style=style_perla
                            ),
                        ),
                        rx.alert_dialog.cancel(
                            rx.button(
                            rx.text.strong("cancelar", color= "black"),
                            width="10em",
                            style=style_perla
                            ),
                        ),
                    spacing="3",
                    )
                ),
                width="100%",
            ),
            on_submit=PageState.insertar_usuario,
            reset_on_submit=True,
            width="100%",
        ),
    ),
        ),
    ),
)

def trigger_remover_usuario():
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button(
            rx.text.strong("Remover usuario", color = "black"), 
            style=style_perla, 
            width = "15em",
            margin_top ="3px"
        ),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Remover usuario de la clase:"),
        rx.alert_dialog.description(
            rx.vstack( 
        rx.form.root(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="user",
                        placeholder="Usuario:",
                        required=True
                    ),
                    rx.select(
                    supabase.obtener_fechas_proximas_semanas(),
                    default_value="hoy",
                    name="fecha",
                    ),
                    rx.select(
                    ["09:00", "10:00", "14:00", "16:00", "16:30", "17:30", "18:00"],
                    name="hora",
                    ),
                ),rx.hstack(
                    rx.flex(
                        rx.alert_dialog.action(
                            rx.button(
                                rx.text.strong("Aceptar", color= "black"), 
                                type="submit", width ="10em",
                                style=style_perla
                            ),
                        ),
                        rx.alert_dialog.cancel(
                            rx.button(
                            rx.text.strong("cancelar", color= "black"),
                            width="10em",
                            style=style_perla
                            ),
                        ),
                    spacing="3",
                    )
                ),
                width="100%",
            ),
            on_submit=PageState.remover_usuario,
            reset_on_submit=True,
            width="100%",
        ),
    ),
        ),
    ),
)



def box_marron(text):
    return rx.vstack(
        rx.box(
            rx.text.strong(text, color = "black"),
            
            style=style_box_marron
        )
    )

def box_perla(text):
    return rx.vstack(
        rx.box(
            rx.text.strong(text, color = "black"),
            
            style=style_perla
        )
    )

def box_ceramica_azul(text):
    return rx.vstack(
        rx.box(
            rx.text.strong(text, color = "black"),
            
            style=style_ceramica_azul
        )
    )

def box_gris_pizzarra(text):
    return rx.vstack(
        rx.box(
            rx.text.strong(text, color = "black"),
            style=style_gris_pizzarra
        )
    )


def button_clase(item : Total):    

    return rx.center(
        rx.cond(item.semana == PageState.semana,
                rx.cond(
                    item.lugar_disponible > 0,
                    rx.cond(
                            item.mails.contains(PageState.obtener_user),
                            trigger_alert(button_green(item), "Ya tenes clase este dia!", "No puedes inscribirte dos veces en la misma clase", "/turnos"),                            
                        rx.cond(
                                (PageState.check_cant_clases > 0) | (PageState.check_recuperar > 0),
                                trigger_alert(button_green(item), "Incripcion exitosa", f"se ha inscripto exitosamente a la clase el dia {item.dia} {item.fecha} a las {item.hora}", "/turnos"),                            rx.cond(
                                (PageState.check_cant_clases == 0) & (PageState.check_recuperar == 0) & (PageState.check_trigger_alert == 0 ),
                                trigger_alert(button_green(item), "No puedes sumarte a esta clase", 'Ya tienes todas tus clases asignadas del mes, consultalo en "mis horarios" ', "/turnos"),
                                rx.cond(
                                    (PageState.check_trigger_alert > 0 ),
                                    trigger_alert(button_green(item), "No puedes sumarte a esta clase", "Para recuperar una clase debes cancelar con 24hs de anticipacion", "/turnos"),
                                )
                            )
                        )
                    ),
                button_disabled(item)
                )
            ) 
        )

    

    
def aceptar_button(rute):
    return rx.link(
            rx.button(
            rx.text("Aceptar", color="black"),
            bg="linear-gradient(145deg, #f0e4d7, #e6d0b8)",
            border="2px solid #d4b594",
            border_radius="5px",
            box_shadow="2px 2px 3px #c1a684, -2px -2px 3px #ffffff",
            color="#6b4c2c",
            font_weight="bold",
            padding="5px",
            width= "20em",
            _hover={
                "bg": "linear-gradient(145deg, #e6d0b8, #f0e4d7)",
                "box_shadow": "inset 2px 2px 3px #c1a684, inset -5px -5px 10px #ffffff",
            }
            ),
            href=rute
        )


    
    
def colores():
    return rx.vstack(
        ceramica_azul_button(),    
        ceramica_button(),
        terracota(),
        ceramica_button_rojo(),
        Cerámica_Roja_Clara(),
        CerámicarojaTerracota(),
        ceramica_button_rojo4(),
        ceramica_verde(),
        azul_y_blanco(),
        Cerámica_Verde_Bosque(),
        Cerámica_Verde_Jade(),
        Cerámica_Verde_Oliva(),
        Cerámica_Verde_Menta(),
        ceramica_azul_oscuro(),
        CerámicaNegroCarbón(),
        CerámicaNegroMate(),
        CerámicaNegroObsidiana(),
        CerámicaNegroÉbano(),
        CerámicaGrisCarbón(),
        CerámicaGrisClaro(),
        CerámicaGrisMedio(),
        CerámicaGrisPerla(),
        CerámicaGrisPizarra(),
    )
        
def button_green_advertencia():
    pass

def button_green(item) -> rx.Component:
        
        

        return rx.button(
                rx.text(f"{item.dia} {item.fecha} a las {item.hora}"),
                on_click=ReservaCancela.agregar_usuario(item.id, PageState.obtener_user , True),
                bg="linear-gradient(145deg, #a7c7d9, #89a5b7)",
                border="2px solid #6b8399",
                border_radius="5px",
                box_shadow="2px 2px 5px #5a6f80, -5px -5px 10px #ffffff",
                color="#2c4b6b",
                font_weight="bold",
                padding="5px",
                width= "15em",
                _hover={
                    "bg": "linear-gradient(145deg, #A5B7C1, #a7c7d9)",
                    "box_shadow": "inset 1px 1x 1px #5a6f80, inset 1px 1px 1px #ffffff",
                },
            )
        
        
def button_red(item) -> rx.Component:
        return rx.button(
                    rx.text("cancelar"),
                    on_click=ReservaCancela.eliminar_usuario(item.id, PageState.obtener_user),
                    style=style_ceramica_roja,
                )
    

def button_disabled(item) -> rx.Component:
    return rx.center(
        rx.button(
            rx.text(f"{item.dia} {item.fecha} a las {item.hora}"),
            disabled=True,
            bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
            color="#333333",
            # border="1px solid #bdbdbd",
            border_radius="6px",
            padding="5px",
            width= "14.5em",
        )
    ) 

def crear_usuario_button():
    return rx.center(
        rx.link(
            rx.button(
                rx.text("Crear usuario"),
                style=style_gris_pizzarra,
                width = "7em"
            ),
            href="/crear_usuario"
        )
    )

def iniciar_sesion_button():
    return rx.center(
        rx.link(
            rx.button(
                rx.text("Iniciar sesion"),
                style=style_gris_pizzarra,
                width = "7em"
            ),
            href="/iniciar_sesion"
        )
    )
    
def button_sign_out():
    return rx.link(
        rx.button(
            rx.text("Cerrar sesion"),
            on_click=ReservaCancela.sign_out,
            style=style_gris_pizzarra,
            width = "10em"
        ),
        href="/"
    )

    

def navbar() -> rx.Component:
    return rx.box(
            rx.hstack(
                rx.link(
                    rx.text("Taller de ceramica",
                        padding_left="1em"
                    ),
                    href="/",
                    color =  "#FCFDFD",
                ),
                desplegable_button(),
                rx.spacer(),
            rx.box(
                rx.cond(
                    PageState.obtener_user ,
                    rx.box(
                        rx.hstack(
                        button_sign_out(),
                        width = "100%",
                        align_items="end")
                    ),
                    rx.box(
                        rx.hstack(
                        crear_usuario_button(),
                        iniciar_sesion_button(),
                        width = "100%",
                        align_items="end")
                    ),
                ),
                )
            ),
            width = "100%",
        style=dict(
            font_family="Confortaa-Medium",
            font_size = "1.3em",
            position="sticky",
            padding_y="0.5em",
            padding_x="0.5em",
            z_index="999",
            top="0",
            bg="#808080",
            box_shadow="1px 1px 2px #696969, -1px -1px 2px #b8b8b8",
            color="#050505",
            font_weight="bold",
            ),
    )

def desplegable_button():
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon("chevron-down", color="white"),
                variant="ghost",
                size="2",
                width="6em",
                style={
                    "background_color": "#808080"
                }
            ),
        ),
        rx.menu.content(
            button_menu("turnos", "/turnos"),
            button_menu("mis horarios", "/mis_horarios"),
            rx.cond(PageState.obtener_user == "ivannarisaro@hotmail.com",
                button_menu("gestion horarios", "/gestion_horarios")
            ),
        ),
        style={"margin_top": "5.5em",
               "background_color": "#FFFDF4"}  
    )
    
def button_menu(text, rute):
    return rx.link(
        rx.button(
            rx.text(text),
            width="13em",
            style={
                "background_color": "#808080"
            }
        ),
        href=rute,
        style={"margin_bottom": "0.5em"}
    )


def button_prueba_dias(item):
    return rx.hstack(
        rx.cond(
            PageState.semana.to_string() == item.semana.to_string(),
            rx.button(
                f"{item.dia} {item.fecha}" , 
                style=style_gris_pizzarra, 
                width = "15em",
                on_click=ButtonState.toggle_text(item.dia),
            )
        ),
        rx.cond(ButtonState.show_text_lunes,
            rx.cond(
                (item.dia == "lunes") & (item.semana == PageState.semana),
                rx.foreach(
                    PageState.filtered_list_lunes,
                    button_clase
                )
            )
        ),
        rx.cond(ButtonState.show_text_martes,
            rx.cond(
                (item.dia == "martes") & (item.semana == PageState.semana),
                rx.foreach(
                    PageState.filtered_list_martes,
                    button_clase
                )
            )
        ),
        rx.cond(ButtonState.show_text_miercoles,
            rx.cond(
                (item.dia == "miercoles") & (item.semana == PageState.semana),
                rx.foreach(
                    PageState.filtered_list_miercoles,
                    button_clase
                )
            )
        ),
        rx.cond(ButtonState.show_text_jueves,
            rx.cond(
                (item.dia == "jueves") & (item.semana == PageState.semana),
                rx.foreach(
                    PageState.filtered_list_jueves,
                    button_clase
                )
            )
        ),
        rx.cond(ButtonState.show_text_viernes,
            rx.cond(
                (item.dia == "viernes") & (item.semana == PageState.semana),
                rx.foreach(
                    PageState.filtered_list_viernes,
                    button_clase
                )
            )
        ) 
    )



def button_reset_database():
    return rx.button(
        "Reset database",
        width ="15em",
        on_click=ReservaCancela.reset_database(),
        style=style_perla,
        margin_y="3em"
    )

    
BASE_STYLE = {
    "font_family": "1em",
    "font_weight": "300",
    "background_color": "#FFFDF4",
    rx.heading: {
        "color": "#708090",
        "font_family": "Poppins",
        "font_weight": "500"
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": "0.5em",
        "border_radius": "0.8em",
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
    },
    rx.link: {
        "color": "#FCFDFD",
        "text_decoration": "none",
        "_hover": {
            "color": "#708090"
        }
    }
}


app = rx.App(
    style=BASE_STYLE,
    )
app.add_page(index)
app.add_page(turnos)
app.add_page(mis_horarios)
app.add_page(gestion_horarios)