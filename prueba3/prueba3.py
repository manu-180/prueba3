import reflex as rx 
import os
import time
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from supabase import create_client, Client
from typing import Any
from enum import Enum
from http.cookies import SimpleCookie
from collections import Counter



class Size(Enum):
    VERY_SMALL = "1em"
    LOGIN_BUTTONS_MOBIL = "2em"
    LOGIN_BUTTONS_DESKTOP = "2.4em"
    SMALL = "4em"
    MEDIUM = "8em"
    BUTTON_DAYS= "9em"
    BUTTON_TRIGGER="10em"


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
    fullname:str
    user_uid:str
    clases_disponibles:int
    recuperar:int
    trigger_alert:int
    sexo:str
    
   

async def data_usuarios() -> list[Usuarios]:       
        return supabase.data_usuarios()   

    
async def data_total() -> list[Total]:       
        return supabase.data_total()   


class PageState(rx.State):
    
    user_cookie: str = rx.Cookie(name="user_cookie")
    total_info:list[Total]
    usuarios_info:list[Usuarios]
    fecha: str = ""
    hora: str = ""
    usuarios_clase: list = []
    semana:str = "semana1"
    fecha_actual = datetime.now()
    limite_recuperacion = timedelta(hours=24)
    user_clase = ""
    fecha_seleccion_horarios = ""
    seleccionar_hora = ""
    is_loading: bool = True
    
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

    def handle_submit(self, form_data: dict):
        self.fecha = form_data["select"]
        
    
    def insertar_usuario(self, form_data: dict):
        for i in self.total_info:
            if i.hora == self.seleccionar_hora and i.fecha == self.fecha_seleccion_horarios:
                supabase.agregar_usuario_a_horario(i.id, self.user_clase, False)
        
    def remover_usuario(self, form_data: dict):
        for i in self.total_info:
            if i.hora == self.seleccionar_hora and i.fecha == self.fecha_seleccion_horarios and self.user_clase in i.mails:
                supabase.eliminar_usuario_a_horario(i.id, self.user_clase, False)
        
    def load_data(self):
        try:
            self.is_loading = False
        except Exception as e:
            self.is_loading = True
        
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
            if i.fullname == self.obtener_user:
                result = i.recuperar 
        return result
    
    @rx.var
    def check_cant_clases(self) -> int:
        result = 0
        for i in self.usuarios_info:
            if i.fullname == self.obtener_user:
                result = i.clases_disponibles 
        return result
    
    @rx.var
    def check_trigger_alert(self) -> int:
        result = 0
        for i in self.usuarios_info:
            if i.fullname == self.obtener_user:
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
    
        if self.user_cookie:
            return self.user_cookie

        user_info = supabase.supabase.auth.get_user()
        if user_info:
            self.user_cookie =  user_info.user.user_metadata["fullname"]
            return self.user_cookie
        return ""

    
    def actualizar_user(self):
        user = self.obtener_user
        if user:
            self.user_cookier = user  
        self.user_cookie = None
    
    @rx.var
    def user_list(self) -> list[Usuarios]:
        total_info = self.usuarios_info
        
        total_list_sorted = sorted(total_info, key=lambda data: data.fullname)
        
        return total_list_sorted
    
    @rx.var
    def in_clase(self):
        result = []
        for i in self.total_info:
            if self.user_cookie in i.mails:
                result.append(i)
        return result
    
    @rx.var
    def hay_clases(self) -> list[Total]:
        result=[]
        my_set= set()
        for i in self.total_info:
            if i.lugar_disponible > 0 and i.semana == self.semana and i.lugar_disponible not in my_set:
                result.append(i)
                my_set.add(i.lugar_disponible)
        return result
    
    @rx.var
    def is_mujer(self):
        for i in self.usuarios_info:
            if i.fullname == self.obtener_user:
                if i.sexo == "mujer":
                    return True
                else:
                    return False
                
    @rx.var
    def list_personas(self) -> list[str]:

        result = [i.fullname for i in self.usuarios_info]
        result.sort()
        return result   

    
    def add_usuario(self, nuevo_usuario: Usuarios):

        self.usuarios_info.append(nuevo_usuario)
        self.usuarios_info.sort(key=lambda x: x.fullname) 
        

                

        
class ReservaCancela(rx.State):
    
    async def reset_database(self):
        reset = reset_databasee()
        return reset
    
    async def eliminar_usuario_de_bd(self, id, user_uid):
        eliminar = eliminar_usuario_de_bdd(id, user_uid)
        return eliminar
    
    async def eliminar_usuario(self, id, user, parametro):
        eliminar = eliminar_usuarioo(id, user, parametro)
        return eliminar

    async def agregar_usuario(self, id, user, parametro):
        agregar = agregar_usuarioo(id, user, parametro)
        return agregar

    
    async def sign_out(self):
        out = sign_outt()
        return out
    
    async def desplazando_izquierda(self):
        izquierda = desplazando_izquierda()
        return izquierda
    
    async def desplazando_derecha(self):
        derecha = desplazando_derecha()
        return derecha
    
def reset_databasee():
    supabase.reset_data_base()

def eliminar_usuario_de_bdd(id, user_uid):
    supabase.eliminar_usuario_de_bd(id, user_uid)
    
def eliminar_usuarioo(id, user, parametro):
    supabase.eliminar_usuario_a_horario(id, user, parametro)

def agregar_usuarioo(id, user, parametro):
    supabase.agregar_usuario_a_horario(id, user, parametro)

def sign_outt():
    supabase.sign_out()

def desplazando_izquierda():
    supabase.desplazando_izquierda()
    
def desplazando_derecha():
    supabase.desplazando_derecha()


class ButtonState(rx.State):

    show_text_lunes: bool = False
    show_text_martes: bool = False
    show_text_miercoles: bool = False
    show_text_jueves: bool = False
    show_text_viernes: bool = False

    def toggle_text(self, dia):
        if dia == "lunes":
            self.show_text_lunes = not self.show_text_lunes
            self.show_text_martes = False
            self.show_text_miercoles = False
            self.show_text_jueves = False
            self.show_text_viernes = False
        elif dia == "martes":
            self.show_text_lunes = False
            self.show_text_martes = not self.show_text_martes
            self.show_text_miercoles = False
            self.show_text_jueves = False
            self.show_text_viernes = False
        elif dia == "miercoles":
            self.show_text_lunes = False
            self.show_text_martes = False
            self.show_text_miercoles = not self.show_text_miercoles
            self.show_text_jueves = False
            self.show_text_viernes = False
        elif dia == "jueves":
            self.show_text_lunes = False
            self.show_text_martes = False
            self.show_text_miercoles = False
            self.show_text_jueves = not self.show_text_jueves
            self.show_text_viernes = False
        elif dia == "viernes":
            self.show_text_lunes = False
            self.show_text_martes = False
            self.show_text_miercoles = False
            self.show_text_jueves = False
            self.show_text_viernes = not self.show_text_viernes
        

class Login(rx.State):

    mi_cookie: str = rx.Cookie(name="cookie")
    palabras = []
    
    #errores
    error_de_crear = ""
    error_login = ""
    error_cond_login = False
    error_cond_crear = False
    check_cond_crear = False
    mensaje_contraseña = False
    
    #fullname propiedades
    fullname_value = ""
    fullname= "Ingrese nombre y apellido"
    fullname_width = "0px"
    fullname_underline = "2px solid white"
    fullname_underline_color = "white" 
    
    # email propiedades  
    email_width_register = "0px"
    email_width_login = "0px"
    email = "Ingrese su mail"
    email_value_register = ""
    email_value_login = ""
    email_underline = "2px solid white"
    email_underline_color = "white"  
    
    # password propiedades
    password_width_register = "0px"
    password_width_login = "0px"
    password = "Ingrese su contraseña"
    password_value_register = ""
    password_value_login = ""
    password_underline = "2px solid white"
    password_underline_color = "white"  
    
    
    # password confirm propiedades
    password_width_confirm = "0px"
    password_confirm = "Confirme su contraseña"
    password_value_confirm = ""
    password_underline_confirm = "2px solid white"
    password_underline_color_confirm = "white"  
    cond_create_user = False
    
    #cambiar contraseña propiedades
    contraseña_width_register = "0px"
    contraseña_width_login = "0px"
    contraseña = "Ingrese su contraseña"
    contraseña_value_register = ""
    contraseña_value_login = ""
    contraseña_underline = "2px solid white"
    contraseña_underline_color = "white"  
    cond_contraseña_fall = False
    cond_contraseña_check = False
    cond_contraseña = False
    contraseña_alert =  ""
    
    #cambiar contraseña confirm propiedades
    contraseña_width_confirm = "0px"
    contraseña_confirm = "Confirme su contraseña"
    contraseña_value_confirm = ""
    contraseña_underline_confirm = "2px solid white"
    contraseña_underline_color_confirm = "white"  
    

    box_width_register = "60px"
    box_height_register = "60px"
    box_width_login = "60px"
    box_height_login = "60px"
    box_width_contraseña = "60px"
    box_height_contraseña = "60px"

    result_sign_in = ""
    result_pos = "transform(0px, 0px)"
    result_opacity = "0%"
    result_color = ""
    
    def close_box_contraseña(self):
        self.box_width_contraseña = "0px"
        self.contraseña_width_register = "0px"
        self.contraseña_width = "0px"
        self.contraseña_width_confirm = "0px"
        self.error_cond_login = False
        self.error_cond_crear = False
        self.check_cond_crear = False
        self.cond_create_user = False
        self.cond_contraseña_fall = False
        self.cond_contraseña_check = False
        self.cond_contraseña = False
        self.mensaje_contraseña = False
        box_width_register = "60px"
        box_height_register = "60px"
        box_width_login = "60px"
        box_height_login = "60px"
        box_width_contraseña = "60px"
        box_height_contraseña = "60px"
        
        
    def open_box_contraseña(self):
        self.box_width_contraseña = "210px"
        self.contraseña_width_register = "155px"
        self.contraseña_width = "155px"

    def open_box_register(self):
        self.box_width_register = "350px"
        self.fullname_width_register = "300px"
        self.fullname_width = "300px"
        
    def open_box_login(self):
        self.box_width_login = "350px"
        self.email_width_login = "300px"
        
    def on_fullname(self, fullname):
        
        self.fullname_value= fullname
        
        self.palabras = fullname.split()
        if fullname == "":
            self.fullname_underline_color = "white"
            self.box_height_register = "60px"     
        elif len(self.palabras) > 1:
            self.fullname_underline_color = "green"
            self.box_height_register = "110px"
            self.email_width_register = "300px"
            self.email_underline = "2px solid white"
        else:
            self.fullname_underline_color = "red"
            self.box_height_register = "60px"
        

    def on_check_email_register(self, email_value_register):
        self.email_value_register = email_value_register
        if self.email_value_register == "":
            self.email_underline_color = "white"
            self.box_height_register = "110px"
        elif any(
            domain in self.email_value_register
            for domain in ("@gmail.com", "@hotmail.com", "@live.com", "@yahoo.com", "@edenor.com")
        ):
            self.email_underline_color = "green"
            self.box_height_register = "165px"
            self.password_width_register = "300px"
            self.password_underline = "2px solid white"
        else:
            self.email_underline_color = "red"
            self.box_height_register = "110px"
    
    def on_check_email_login(self, email_value_login):
        self.email_value_login = email_value_login
        if self.email_value_login == "":
            self.email_underline_color = "white"
            self.box_height_login = "60px"
        elif any(
            domain in self.email_value_login
            for domain in ("@gmail.com", "@hotmail.com", "@live.com", "@yahoo.com", "@edenor.com")
        ):
            self.email_underline_color = "green"
            self.box_height_login = "120px"
            self.password_width_login = "300px"
            self.password_underline = "2px solid white"
        else:
            self.email_underline_color = "red"
            self.box_height_login = "60px"
    
    def on_check_password_contraseña(self, contraseña_value):
        self.contraseña_value_register = contraseña_value
        if self.contraseña_value_register == "":
            self.contraseña_underline_color = "white"
            self.box_height_contraseña = "60px"
            self.contraseña_width_confirm = "0px" 
        elif len(contraseña_value) >= 6:
            self.contraseña_underline_color = "black"
            self.box_height_contraseña = "110px"
            self.contraseña_width_confirm = "155px" 
        else:
            self.contraseña_underline_color = "red"
            self.box_height_contraseña = "60px"
            self.contraseña_width_confirm = "0px"  
        
    def on_check_password_register(self, password_value):
        self.password_value_register = password_value
        
        if self.password_value_register == "":
            self.password_underline_color = "white"
            self.box_height_register = "165px"
            self.password_width_confirm = "0px"  
            self.mensaje_contraseña = False
        elif len(password_value) >= 6:
            self.password_underline_color = "green"
            self.box_height_register = "210px"
            self.password_width_confirm = "300px" 
            self.mensaje_contraseña = False
        else:
            self.mensaje_contraseña = True
            self.password_underline_color = "red"
            self.box_height_register = "165px"
            self.password_width_confirm = "0px"  
    
    def on_check_password_confirm_contraseña(self, contraseña_value_confirm):
        self.contraseña_value_confirm = contraseña_value_confirm
        if self.contraseña_value_confirm == "":
            self.contraseña_underline_color_confirm = "white"
            self.box_height = "110px"
        elif self.contraseña_value_confirm == self.contraseña_value_register:
            self.contraseña_underline_color_confirm = "black"
            self.box_height_register = "155px"
            self.cond_contraseña = True
        else:
            self.contraseña_underline_color_confirm = "red"
            self.box_height = "110px"
    
    def on_check_password_login(self, password_value_login):
        self.password_value_login = password_value_login
        if self.password_value_login == "":
            self.password_underline_color = "white"
            self.box_height_login = "120px"
            self.password_width_confirm = "0px"  
        elif len(password_value_login) >= 6:
            self.password_underline_color = "green"
            self.box_height_login = "210px"
            self.password_width_confirm = "300px" 
        else:
            self.password_underline_color = "red"
            self.box_height_login = "120px"
            self.password_width_confirm = "0px"  
            
    def on_check_password_confirm(self, password_value_confirm):
        self.password_value_confirm = password_value_confirm
        if self.password_value_confirm == "":
            self.password_underline_color_confirm = "white"
            self.box_height_register = "210px"
        elif self.password_value_confirm == self.password_value_register:
            self.password_underline_color_confirm = "green"
            self.box_height_register = "300px"
            self.cond_create_user = True
        else:
            self.password_underline_color_confirm = "red"
            self.box_height_register = "210px"
    
    def user_sign_in(self):

        try:
            data = supabase.supabase.auth.sign_in_with_password({"email": self.email_value_login, "password": self.password_value_login})
            self.mi_cookie = data.user.user_metadata["fullname"]
            return rx.redirect("/")
        except Exception as e:
            self.error_cond_login = True
            self.error_login = "Autenticacion invalida. Verifice mail y/o contraseña"
            print(e)
            
    def cambiar_contraseña(self):
        
        try:
            user = supabase.supabase.auth.get_user()
            for i in supabase.data_usuarios():
                if i.user_uid == user.user.id:
                    response = supabase.supabase.auth.update_user({
                        'password': self.contraseña_value_confirm
                    })
            self.contraseña_alert = "Su contraseña ah sido cambiada con exito"
            self.cond_contraseña_check = True 
            self.cond_contraseña_fall = False
            return check_momentaneo()
        except Exception as e:            
            if str(e) == "'NoneType' object has no attribute 'user'":
                self.contraseña_alert = "Lo sentimos surgió un error, inicie sesión nuevamente para cambiar la contraseña"
                self.cond_contraseña_fall = True
                self.cond_contraseña_check = False 
                print(e)
                return error_momentaneo()
            else:
                self.contraseña_alert = "La contraseña nueva es igual a la anterior"
                self.cond_contraseña_fall = True
                self.cond_contraseña_check = False 
                print(e)
                return error_momentaneo()


    def registrar_user_submit(self):
        fullname = self.fullname_value.title()
        try:
            existing_user = supabase.supabase.table("usuarios").select("*").eq("usuario", self.email_value_register).execute()
            if existing_user.data:
                return False
            
            response = supabase.supabase.auth.sign_up(
                credentials={
                    "email": self.email_value_register,
                    "password": self.password_value_register,
                    "options": {"data": {"fullname": fullname}},
                }
            )
            
            usuarios_data = supabase.data_usuarios()
            ids = [item.id for item in usuarios_data]
            new_id = max(ids) + 1 if ids else 1
            
            supabase.supabase.table("usuarios").insert({
                "id": new_id,
                "usuario": self.email_value_register,
                "fullname": fullname,  
                "user_uid": response.user.user_metadata["sub"],
                "clases_disponibles": 0,
                "recuperar": 0,
                "trigger_alert": 0,
            }).execute()

            PageState.add_usuario(Usuarios(
                id=new_id,
                usuario=self.email_value_register,
                fullname=fullname,
                user_uid=response.user.user_metadata["sub"],
                clases_disponibles=0,
                recuperar=0,
                trigger_alert=0,
            ))

            self.check_cond_crear = True
            self.error_cond_crear = False
            self.error_de_crear = "Revise su correo electronico y haga click en el link para autenticarse"
            return check_momentaneo()

        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            self.check_cond_crear = False
            self.error_cond_crear = True
            self.error_de_crear = "Hubo un problema al registrar el usuario."
            return error_momentaneo()

        

class SupaBase():

    load_dotenv()

    URL: str = os.environ.get("URL")
    KEY: str = os.environ.get("KEY")
    SERVICE_ROLE: str = os.environ.get("SERVICE_ROLE")

    supabase: Client = create_client(URL, KEY)

    def data_total(self) -> list[Total]:
        
        total_class = []

        total = self.supabase.table("total").select("*").execute()
        
        for i in total.data:
            total_class.append(Total(id=i["id"], semana=i["semana"], dia=i["dia"], fecha=i["fecha"], hora=i["hora"], mails=i["mails"], lugar_disponible=i["lugar_disponible"]))
        total_list_sorted = sorted(total_class, key=lambda alumno: alumno.id)
        return total_list_sorted
    
    def decreciente_data_total(self) -> list[Total]:
        
        total_class = []

        total = self.supabase.table("total").select("*").execute()
        
        for i in total.data:
            total_class.append(Total(id=i["id"], semana=i["semana"], dia=i["dia"], fecha=i["fecha"], hora=i["hora"], mails=i["mails"], lugar_disponible=i["lugar_disponible"]))
        total_list_sorted = sorted(total_class, key=lambda alumno: alumno.id)
        total_list_sorted.reverse()
        return total_list_sorted
    
  
    def data_usuarios(self) -> list[Usuarios]:

        usuarios_class = []

        usuarios = self.supabase.table("usuarios").select("*").execute()

        for i in usuarios.data:
            usuarios_class.append(Usuarios(id=i["id"], usuario=i["usuario"],fullname=i["fullname"],user_uid=i["user_uid"], clases_disponibles=i["clases_disponibles"], recuperar=i["recuperar"], trigger_alert=i["trigger_alert"], sexo=i["sexo"]))
        return usuarios_class


    def lista_de_usuarios(self) -> list:
        list_result = []
        for i in self.data_usuarios():
            list_result.append(i.fullname)
        list_result.sort()    
        return list_result
            

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
        dias_habiles_septiembre = [
            '02/09', '03/09', '04/09', '05/09', '06/09',
            '09/09', '10/09', '11/09', '12/09', '13/09',
            '16/09', '17/09', '18/09', '19/09', '20/09',
            '23/09', '24/09', '25/09', '26/09', '27/09',
            '30/09', '01/10', '02/10', '03/10', '04/10',
            '07/10'
        ]
        return dias_habiles_septiembre

    def generar_lista_dias_habiles(self, inicio, fin):
        # Convertir las fechas de inicio y fin en objetos datetime
        fecha_inicio = datetime.strptime(inicio, "%d/%m")
        fecha_fin = datetime.strptime(fin, "%d/%m")

        dias_habiles = []

        # Incluir la fecha de inicio si es un día hábil (lunes a viernes)
        if fecha_inicio.weekday() < 5:  # Si es de lunes (0) a viernes (4)
            if fecha_inicio.weekday() == 0:  # Si es lunes, añadir solo una vez
                dias_habiles.append(fecha_inicio.strftime("%d/%m"))
            else:  # Si es martes a viernes, añadir tres veces
                dias_habiles.extend([fecha_inicio.strftime("%d/%m")] * 3)

        # Iterar sobre los días en el rango, empezando con el día inicial ya ajustado
        while fecha_inicio <= fecha_fin:
            # Si es lunes, añadir solo una vez
            if fecha_inicio.weekday() == 0:  # 0 es lunes
                dias_habiles.append(fecha_inicio.strftime("%d/%m"))
            # Si es de martes a viernes, añadir tres veces
            elif 1 <= fecha_inicio.weekday() <= 4:  # 1 a 4 son martes a viernes
                dias_habiles.extend([fecha_inicio.strftime("%d/%m")] * 3)
            
            # Pasar al día siguiente
            fecha_inicio += timedelta(days=1)

        return dias_habiles



    def check_user_in_semana(self, user, semana):
        check_semana = []
        for i in self.data_usuarios():
            if i.fullname == user and semana in i.semanas:
                check_semana.append(semana)
        if len(check_semana) > 0 :
            return False
        return True
    
            

            
    
    def actualizar_fecha(self, id):
        for index, i in enumerate(self.obtener_fechas_proximas_semanas()):
            if index + 1 == id:
                return i
        
    
    def cant_clases_usuario(self, user):

        try:
            for i in self.data_usuarios():
                if user == i.fullname:
                    return i.clases_disponibles
        except Exception as e:
            print(f"error {e} en la funciopn cant_clases_usuario")
    
    def recuperar_clase(self, user):
        recupera = 0
        for i in self.data_usuarios():
            if user == i.fullname:
                return i.recuperar
                        
    
    def id_usuario(self, user):

        for i in self.data_usuarios():
            if user == i.fullname:
                return i.id

    
        
    def recuperar_con_usuario(self, usuario):
        for i in self.data_usuarios():
            if i.fullname == usuario:
                return i.recuperar
      
    def trigger_alert_con_usuario(self, usuario):
        for i in self.data_usuarios():
            if i.fullname == usuario:
                return i.trigger_alert      
            
    
    def rotar_al_final(self):
        lista1=[]
        for i in self.data_total():
            if i.id == 1 :
                lista1 = i.mails
                response = (self.supabase.table("total").update({"mails":[]}).eq("id", i.id).execute())
            if i.id == 54:
                response = (self.supabase.table("total").update({"mails":lista1}).eq("id", i.id).execute()) 

    def rotar_al_principio(self):
        lista1=[]
        for i in self.decreciente_data_total():
            if i.id == 54 :
                lista1 = i.mails
                response = (self.supabase.table("total").update({"mails":[]}).eq("id", i.id).execute())
            if i.id == 1:
                response = (self.supabase.table("total").update({"mails":lista1}).eq("id", i.id).execute()) 
            
            
    def uno_a_la_izquierda(self):
        for i in self.data_total():
            if i.id > 1:
                self.supabase.table("total").update({"mails":i.mails}).eq("id", i.id -1 ).execute()

    def uno_a_la_derecha(self):
        for i in self.decreciente_data_total():
            self.supabase.table("total").update({"mails":i.mails}).eq("id", i.id + 1 ).execute()

    def desplazando_izquierda(self):
        self.rotar_al_final()
        self.uno_a_la_izquierda()
        
    def desplazando_derecha(self):
        self.uno_a_la_derecha()
        self.rotar_al_principio()  
    
    def agregar_usuario_a_horario(self, id, user, parametro):
        if user :
            for data in self.data_total():
                if data.id == id:
                    if user not in data.mails:
                        if self.cant_clases_usuario(user) > 0 or self.recuperar_clase(user) > 0 or not parametro:
                            alumnos = data.mails
                            alumnos.append(user)
                            lugar_disponible = data.lugar_disponible
                            lugar_disponible -= 1
                            response = (self.supabase.table("total").update({"mails": alumnos}).eq("id", id).execute())
                            if parametro:    
                                response = (self.supabase.table("total").update({"lugar_disponible": lugar_disponible}).eq("id", id).execute())
                            if self.cant_clases_usuario(user) > 0:
                                response = (self.supabase.table("usuarios").update({"clases_disponibles": self.cant_clases_usuario(user) - 1}).eq("id", self.id_usuario(user)).execute())
                            for i in self.data_usuarios():
                                if user == i.fullname and i.recuperar > 0:
                                    response = (self.supabase.table("usuarios").update({"recuperar": self.recuperar_clase(user) - 1}).eq("id", self.id_usuario(user)).execute())
        else: 
            return False
                
    def eliminar_usuario_de_bd(self, id, user_uid):
        
        response = self.supabase.table('usuarios').delete().eq('id', id).execute()
        
        url = f"{self.URL}/auth/v1/admin/users/{user_uid}"
        headers = {
            "Authorization": f"Bearer {self.SERVICE_ROLE}",
            "apikey": self.SERVICE_ROLE, 
            "Content-Type": "application/json"
        }
        response = requests.delete(url, headers=headers)



    def eliminar_usuario_a_horario(self, id, user, parametro):
        
        for data in self.data_total():
            if data.id == id:
                if user in data.mails:
                    alumnos = data.mails
                    alumnos.remove(user)
                    lugar_disponible = data.lugar_disponible
                    lugar_disponible += 1
                    if parametro:
                        response = (self.supabase.table("total").update({"lugar_disponible": lugar_disponible}).eq("id", id).execute())
                    response = (self.supabase.table("total").update({"mails": alumnos}).eq("id", id).execute())
                    if self.fecha_hora_recuperar(id, user) and parametro:
                        response = (self.supabase.table("usuarios").update({"recuperar": self.recuperar_con_usuario(user) + 1}).eq("id", self.id_usuario(user)).execute())
                        if self.trigger_alert_con_usuario(user) > 0 :
                            response = (self.supabase.table("usuarios").update({"trigger_alert": 0}).eq("id", self.id_usuario(user)).execute())
    
   
    
    def sign_out(self):
        return [rx.remove_cookie("mi_cookie"), rx.remove_cookie("user_cookie")]
    
    def agregar_fechas_constantemente(self):
        for index, i in enumerate([
                '02/09', '03/09', '03/09', '03/09', '04/09', '04/09', '04/09',
                '05/09', '05/09', '05/09', '06/09', '06/09', '06/09', '09/09',
                '10/09', '10/09', '10/09', '11/09', '11/09', '11/09', '12/09',
                '12/09', '12/09', '13/09', '13/09', '13/09', '16/09', '17/09',
                '17/09', '17/09', '18/09', '18/09', '18/09', '19/09', '19/09',
                '19/09', '20/09', '20/09', '20/09', '23/09', '24/09', '24/09',
                '24/09', '25/09', '25/09', '25/09', '26/09', '26/09', '26/09',
                '27/09', '27/09', '27/09', '30/09', '01/10', '01/10', '01/10',
                '02/10', '02/10', '02/10', '03/10', '03/10', '03/10', '04/10',
                '04/10', '04/10', '07/10'
            ]):
            response = (self.supabase.table("total").update({"fecha": i }).eq("id", index+1).execute())
                
    
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
    
    def reset_data_base(self):
        for i in self.data_total():
            response = (self.supabase.table("total").update({"mails": []}).eq("id", i.id).execute())
            response = (self.supabase.table("total").update({"lugar_disponible":0}).eq("id", i.id).execute())
            
              
supabase = SupaBase()        


# for i in supabase.data_total():    
#     supabase.supabase.table("total2").update({"semana":i.semana}).eq("id", i.id ).execute()
#     supabase.supabase.table("total2").update({"fecha":i.fecha}).eq("id", i.id  ).execute()
#     supabase.supabase.table("total2").update({"hora":i.hora}).eq("id", i.id ).execute()
#     supabase.supabase.table("total2").update({"dia":i.dia}).eq("id", i.id ).execute()
#     supabase.supabase.table("total2").update({"mails":i.mails}).eq("id", i.id ).execute()
    

    



# def identificar_dia_inicial(mes, año):
#     # Crear una fecha para el primer día del mes
#     fecha = datetime(año, mes, 1)
#     # Retornar el día de la semana (0 = lunes, 6 = domingo)
#     return fecha.weekday()

# now = datetime.now()
# # Ejemplo de uso
# dia_inicial = identificar_dia_inicial(now.month, now.year)

# print(dia_inicial)
# dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
# print(f"El día inicial de {now.month}/{now.year } es {dias_semana[dia_inicial]}.")
@rx.page(
    title="index",
    description="Taller de cerámica",
    on_load= [
              PageState.total,
              PageState.actualizar_user,
              PageState.usuarios,
              PageState.load_data,
              Login.close_box_contraseña
              ]
)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                responsive_picks()
            )
        ),
        footer()
    )



@rx.page(
    route="/turnos", 
    title="turnos",
    description="Taller de ceramica",
    on_load= [
              PageState.total,
              PageState.actualizar_user,
              PageState.usuarios,
              PageState.load_data,
              Login.close_box_contraseña
            ]
)
def turnos() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
        mostrar_conexion(),
        box_marron("Para inscribirse a una clase haga click en un boton que este disponible"),
        margin_top=Size.VERY_SMALL.value
        ),
        rx.center(
            rx.vstack(
                dias_semanales(),
                foreach_hay_clases(),
                width = "100%"
            ),
        margin_top = Size.VERY_SMALL.value
        ),     
    )

@rx.page(
        route="/mis_horarios",
        title="mis horarios ",
        description="Taller de ceramica",
        on_load=[
              PageState.total,
              PageState.actualizar_user,
              PageState.usuarios,
              PageState.load_data,
              Login.close_box_contraseña
            ]
)
def mis_horarios():
    return rx.box(
        rx.center(
            rx.vstack(
                navbar(),
                mostrar_conexion(),
                alert(),
                total_horarios_para_cancelar(),
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
              PageState.actualizar_user,
              PageState.load_data,
              PageState.usuarios,
              Login.close_box_contraseña
            ])
def gestion_horarios():
    return rx.vstack(
        navbar(),
        mostrar_conexion(),
        rx.vstack(
            rx.hstack(
                box_marron("Gestion de horarios"),
            ),
            box_marron("En esta seccion podras agregar o eliminar un usuario de una clase: "),
            form_select_fecha(),
            rx.hstack(
                trigger_mover_usuarios(trigger_desplazar_izquierda(),"Cuidado", "Segura queres mover a todos los alumnos a una clase anterior?", "/gestion_horarios",button_mover_izquierda()),
                trigger_mover_usuarios(trigger_desplazar_derecha(),"Cuidado", "Segura queres mover a todos los alumnos a la clase siguiente?", "/gestion_horarios",button_mover_derecha()),
            ),
            padding_top = "1em",
            margin_x ="1em"
        )
    )
    
@rx.page(
        route="/usuarios",
        title="usuarios ",
        description="Taller de ceramica",
        on_load= [
              PageState.usuarios,
              PageState.load_data,
              Login.close_box_contraseña
            ])
def usuarios():
    return rx.vstack(
        navbar(),
        mostrar_conexion(),
        rx.vstack(
            user_list(),
            margin_x ="1em"
        )
    )       


@rx.page(
    route="/crear_usuario",
    title="crear usuario ",
    description="Taller de ceramica",
    on_load= [
            PageState.actualizar_user,
            PageState.load_data,
            Login.close_box_contraseña
        ])
def crear_usuario():
    return rx.box(
        navbar(),
    rx.center(
        mostrar_conexion(),
        input_create_user(),
        rx.cond(
            Login.error_cond_crear,
            rx.box(
                mensaje_fall(Login.error_de_crear),
                width = Login.box_width_register,
            )
            ),
        rx.cond(
            Login.check_cond_crear,
            rx.box(
                mensaje_check(Login.error_de_crear),
                width = Login.box_width_register
            )
            ),
        display="grid",
        position="relative",
        overflow="hidden",
        place_items="center",
        spacing="1"
    )
)



@rx.page(
    route="/login",
    title="login",
    description="Taller de ceramica",
    on_load= [
        PageState.actualizar_user,
        PageState.load_data,
        Login.close_box_contraseña
        ])
def login():
    return rx.box(
        navbar(),
        mostrar_conexion(),
        inputs(),
        display="grid",
        position="relative",
        overflow="hidden",
        place_items="center",
    )

@rx.page(
    route="/configuracion",
    title="configuracion",
    description="Taller de ceramica",
    on_load= [
        PageState.actualizar_user,
        PageState.load_data,
        Login.close_box_contraseña
        ])
def configuracion():
    return rx.box(
        navbar(),
        rx.vstack(
            mostrar_conexion(),
            rx.cond(Login.mi_cookie,
                rx.box(
                    rx.heading(Login.mi_cookie, margin_top="3em"),
                    input_cambiar_contraseña()
                    ),
                primero_login(), 
            )
        )
    )
    
def mostrar_conexion():
    return rx.box(
        rx.cond(
            PageState.is_loading,
            rx.box(
                mensaje_alerta("Cargando datos, revise conexion de wifi"),
                margin_top="2em"
            )
        ),
    )

def primero_login():
    return rx.box(
        rx.cond(
            Login.mi_cookie,
            rx.heading(Login.mi_cookie, size="8"),
            rx.link(
                rx.heading("¡Primero debes iniciar sesión!", size="8"),
                href="/login"
            )
        ),
        margin_top="3em"
    )

def responsive_picks():
    return rx.center(
            rx.tablet_and_desktop(
                rx.vstack(
                    mostrar_conexion(),
                    picks(),
                    margin_top = "2em",
                    spacing ="4",
                    max_width= "30em"
                )
            ),
            rx.mobile_only(
                rx.vstack(
                    mostrar_conexion(),
                    picks(),
                    margin_top = "2em",
                    spacing ="4",
                    margin_x ="1em"
                )
            ),
        )
        
    
def picks():
    nombre_completo = Login.mi_cookie
    
    return rx.box(
    rx.tablet_and_desktop(
            rx.vstack(
            rx.heading("¡Bienvenido a taller de ceramica ricardo rojas!"),
            rx.hstack(
                rx.cond(Login.mi_cookie,
                        rx.cond(PageState.is_mujer,
                        presentacion_parrafo(f"¡Hola {nombre_completo.split()[0]} y bienvenida a nuestro taller de cerámica, un espacio donde la creatividad se mezcla con la tradición para dar forma a piezas únicas y llenas de vida!","13.5em"),
                        presentacion_parrafo(f"¡Hola {nombre_completo.split()[0]} y bienvenido a nuestro taller de cerámica, un espacio donde la creatividad se mezcla con la tradición para dar forma a piezas únicas y llenas de vida!","13.5em")
                        ),
                    presentacion_parrafo(f"¡Hola y bienvenido/a a nuestro taller de cerámica, un espacio donde la creatividad se mezcla con la tradición para dar forma a piezas únicas y llenas de vida!","13.5em")
                ),
                rx.chakra.box(
                    rx.image(src="/creando.png", height="100%", width="100%", border_radius="10px"),
                    width= "18em", height = "16em"
                )
            ),
            rx.vstack(
                rx.heading("¿Qué hacemos?"),
                rx.hstack(
                    presentacion_parrafo(f"Aquí, en nuestro taller, creamos desde pequeñas piezas decorativas hasta grandes obras de arte, todas con un toque especial y un diseño único.","13.5em"),
                    rx.chakra.box(
                        rx.image(src="/bici.webp", height="100%", width="100%", border_radius="10px"),
                        width= "23em", height = "16em"
                    )
                ),
                rx.hstack(
                    presentacion_parrafo(f"Ofrecemos clases para todos los niveles, desde principiantes hasta expertos, donde podrás aprender las técnicas de modelado, esmaltado y cocción, explorando tus propias ideas y estilo.", "8em"),
                )
            ),
        spacing="4",
        ),
    ),
    rx.mobile_only(
        rx.vstack(
            rx.heading("¡Bienvenido a taller de ceramica ricardo rojas!"),
            rx.vstack(
                rx.cond(Login.mi_cookie,
                    presentacion_parrafo(f"¡Hola {nombre_completo.split()[0]} y bienvenido a nuestro taller de cerámica, un espacio donde la creatividad se mezcla con la tradición para dar forma a piezas únicas y llenas de vida!","11em"),
                    presentacion_parrafo(f"¡Hola y bienvenido a nuestro taller de cerámica, un espacio donde la creatividad se mezcla con la tradición para dar forma a piezas únicas y llenas de vida!","11em")
                ),
                rx.chakra.box(
                    rx.image(src="/creando.png", height="100%", width="100%", border_radius="10px"),
                    width= "18em", height = "26em"
                )
            ),
            rx.vstack(
                rx.heading("¿Qué hacemos?"),
                rx.vstack(
                    presentacion_parrafo(f"Aquí, en nuestro taller, creamos desde pequeñas piezas decorativas hasta grandes obras de arte, todas con un toque especial y un diseño único.","11em"),
                    rx.chakra.box(
                        rx.image(src="/bici.webp", height="100%", width="100%", border_radius="10px"),
                        width= "15em", height = "14em"
                    )
                ),
                rx.vstack(
                    presentacion_parrafo(f"Ofrecemos clases para todos los niveles, desde principiantes hasta expertos, donde podrás aprender las técnicas de modelado, esmaltado y cocción, explorando tus propias ideas y estilo.", "12em"),
                )
            ),
        spacing="4",
        ),
    )
)
    
    
    
def presentacion_parrafo( text, height):
    return rx.box(
        rx.vstack(
            rx.text.strong(text,),
            padding="1em"
        ),
        style=style_presentacion,
        width="100%",
        height = height
    )
    
def imagen(url, text) -> rx.Component:
    return rx.vstack(
    rx.image(
        src=url, 
        width= "20em", 
        height= "auto",
        class_name="animatable"
        ),
    rx.text(text),
    spacing="0"
    )


def hay_clase_foreach(item):
    return rx.box(
            rx.cond(
                item.lugar_disponible > 0,
                box_ceramica_azul(f"Hay clase disponible el dia {item.dia} {item.fecha}"),
            )
        )
    
def foreach_hay_clases():
    return rx.cond(
        PageState.hay_clases.length() == 0,
        box_ceramica_azul("No hay clase disponible esta semana"),
        rx.foreach(
            PageState.hay_clases, 
            hay_clase_foreach
        )
    )

def input_cambiar_contraseña():
    return rx.box(
        rx.vstack(
            horarios_info("Cambiar contraseña",Login.open_box_contraseña()),
            rx.vstack(
                rx.box(
                    rx.chakra.input(
                        value=Login.contraseña_value_register,
                        placeholder="Ingrese contraseña",
                        on_change=lambda contraseña_value_register: Login.on_check_password_contraseña(contraseña_value_register),
                        width=Login.contraseña_width_register,
                        transition="width 0.5s ease 0.65s",
                        font_size="13px",
                        height="28px", 
                        border_radius="4px",
                        letter_spacing="0.5px",
                        margin_bottom="3px",
                        border="none",
                        _focus={
                            "outline": "none",
                            "box_shadow": "none",
                        },
                        type_="password",
                    ),
                    padding="0px",
                    width=Login.contraseña_width_register,
                    border_bottom=f"2px solid {Login.contraseña_underline_color}",
                    transition="width 0.65s ease 0.65s",
                ),
                rx.box(
                    rx.chakra.input(
                        value=Login.contraseña_value_confirm,
                        placeholder="Confirme contraseña",
                        on_change=lambda contraseña_value_confirm: Login.on_check_password_confirm_contraseña(contraseña_value_confirm),
                        width=Login.contraseña_width_confirm,
                        transition="width 0.5s ease 0.65s",
                        font_size="13px",
                        height="28px", 
                        border_radius="4px",
                        letter_spacing="0.5px",
                        margin_bottom="3px",
                        border="none",
                        _focus={
                            "outline": "none",
                            "box_shadow": "none",
                        },
                        type_="password",
                    ),
                    padding="0px",
                    width=Login.contraseña_width_confirm,
                    border_bottom=f"2px solid {Login.contraseña_underline_color_confirm}",
                    transition="width 0.65s ease 0.65s",
                ),
            ),
            rx.spacer(),
            rx.cond(
                Login.cond_contraseña,
                rx.box(
                    rx.button(
                        "Aceptar",
                        width  = Size.MEDIUM.value,
                        height= "2em",
                        on_click= lambda:Login.cambiar_contraseña(),
                        style=style_gris_pizzarra_button
                    ),
                rx.cond(Login.cond_contraseña_check,
                rx.box(
                    mensaje_check(Login.contraseña_alert),
                    min_width="auto",
                    justify_content="center",
                    center_content=True,
                    opacity="1",  
                    transition="opacity 0.65s ease",
                    margin_top="1em",
                    width=Login.box_width_contraseña
                ),
                ),
                rx.cond(Login.cond_contraseña_fall,
                rx.box(
                    mensaje_fall(Login.contraseña_alert),
                    min_width="auto",
                    justify_content="center",
                    center_content=True,
                    opacity="1",  
                    transition="opacity 0.65s ease",
                    margin_top="1em",
                    width="13em"
                ),
                )
            ),
            )
        ),
        margin_top="1em"
    )
    
def inputs():
    return rx.vstack(
        input_box(),
        rx.cond(
            Login.error_cond_login,
            rx.box(
                mensaje_fall(Login.error_login),
            width=Login.box_width_login),
        ),
        margin_top="7em",
    )

def input_box():
    return rx.box(
        rx.heading("Inicia sesión:"),
        rx.box(
        rx.vstack(
            rx.spacer(),
            rx.hstack(
                rx.box(
                    rx.chakra.input(
                        value=Login.email_value_login,
                        placeholder=Login.email,
                        on_change=lambda email_value_login: Login.on_check_email_login(email_value_login),
                        width=Login.email_width_login,
                        transition="width 0.5s ease 0.65s",
                        height="28px", 
                        border_radius="4px",
                        font_size="13px",
                        letter_spacing="0.5px",
                        bg="#1D2330",
                        color="white",
                        type_="text",
                        margin_bottom="3px",
                        margin_left="8px",
                        border="none",
                        _focus={
                            "outline": "none",
                            "box_shadow": "none",
                        },
                    ),
                    padding="0px",
                    width=Login.email_width_login,
                    border_bottom=f"2px solid {Login.email_underline_color}",
                    transition="width 0.65s ease 0.65s",
                ),
            ),
            rx.spacer(),
            rx.hstack(
                rx.box(
                    rx.chakra.password(
                        value=Login.password_value_login,
                        placeholder=Login.password,
                        on_change=lambda password_value_login: Login.on_check_password_login(password_value_login),
                        width=Login.password_width_login,
                        transition="width 0.5s ease 0.65s",
                        font_size="13px",
                        height="28px", 
                        border_radius="4px",
                        bg="#1D2330",
                        color="white",
                        letter_spacing="0.5px",
                        margin_left="8px",
                        margin_bottom="3px",
                        border="none",
                        _focus={
                            "outline": "none",
                            "box_shadow": "none",
                        },
                    ),
                    padding="0px",
                    width=Login.password_width_login,
                    border_bottom=f"2px solid {Login.password_underline_color}",
                    transition="width 0.65s ease 0.65s",
                ),
            ),
            rx.spacer(),
            rx.box(
                rx.hstack(
                    rx.button(
                        "Iniciar sesion",
                        width  = "10.5em",
                        height= "3em",
                        color_scheme="blue",
                        on_click= lambda:Login.user_sign_in(),
                        style=style_gris_pizzarra_button
                    )
                ),
                min_width= "auto",
                height="50px",
                justify_content = "center",
                center_content = True,
            ),
        ),
        width=Login.box_width_login,
        height=Login.box_height_login,
        bg="#1D2330",
        border_radius="5px",
        padding="8px",
        display="grid",
        position="relative",
        overflow="hidden",
        transition="width 0.65s, height 0.65s cubic-bezier(0.175, 0.885, 0.32, 1.275)",
        on_click=lambda: Login.open_box_login()
    )
    )
    
def input_create_user():
    return rx.box(
        rx.heading("Crea tu usuario:"),
        rx.box(
        rx.vstack(
            rx.spacer(),
            rx.vstack(
                rx.box(
                    rx.chakra.input(
                        value=Login.fullname_value,
                        placeholder=Login.fullname,
                        on_change=lambda fullname: Login.on_fullname(fullname),
                        required=True,
                        width=Login.fullname_width,
                        transition="width 0.5s ease 0.65s",
                        height="28px", 
                        border_radius="4px",
                        font_size="13px",
                        letter_spacing="0.5px",
                        bg="#1D2330",
                        color="white",
                        type="text",
                        margin_bottom="3px",
                        margin_left="8px",
                        border="none",
                        _focus={
                            "outline": "none",
                            "box_shadow": "none",
                        },
                    ),
                    padding="0px",
                    width=Login.fullname_width,
                    border_bottom=f"2px solid {Login.fullname_underline_color}",
                    transition="width 0.65s ease 0.65s",
                ),
                rx.box(
                    rx.chakra.input(
                        value=Login.email_value_register,
                        placeholder=Login.email,
                        on_change=lambda email_value_register: Login.on_check_email_register(email_value_register),
                        width=Login.email_width_register,
                        transition="width 0.5s ease 0.65s",
                        height="28px", 
                        border_radius="4px",
                        font_size="13px",
                        letter_spacing="0.5px",
                        bg="#1D2330",
                        color="white",
                        type="text",
                        margin_bottom="3px",
                        margin_left="8px",
                        border="none",
                        _focus={
                            "outline": "none",
                            "box_shadow": "none",
                        },
                    ),
                    padding="0px",
                    width=Login.email_width_register,
                    border_bottom=f"2px solid {Login.email_underline_color}",
                    transition="width 0.65s ease 0.65s",
                ),
            ),
            rx.spacer(),
            rx.vstack(
                rx.box(
                    rx.chakra.input(
                        value=Login.password_value_register,
                        placeholder=Login.password,
                        on_change=lambda password_value_register: Login.on_check_password_register(password_value_register),
                        width=Login.password_width_register,
                        transition="width 0.5s ease 0.65s",
                        font_size="13px",
                        height="28px", 
                        border_radius="4px",
                        bg="#1D2330",
                        color="white",
                        letter_spacing="0.5px",
                        margin_left="8px",
                        margin_bottom="3px",
                        border="none",
                        _focus={
                            "outline": "none",
                            "box_shadow": "none",
                        },
                        type_="password",
                    ),
                    padding="0px",
                    width=Login.password_width_register,
                    border_bottom=f"2px solid {Login.password_underline_color}",
                    transition="width 0.65s ease 0.65s",
                ),
                rx.box(
                    rx.chakra.input(
                        value=Login.password_value_confirm,
                        placeholder=Login.password_confirm,
                        on_change=lambda password_value_confirm: Login.on_check_password_confirm(password_value_confirm),
                        width=Login.password_width_confirm,
                        transition="width 0.5s ease 0.65s",
                        font_size="13px",
                        height="28px", 
                        border_radius="4px",
                        bg="#1D2330",
                        color="white",
                        letter_spacing="0.5px",
                        margin_left="8px",
                        margin_bottom="3px",
                        border="none",
                        _focus={
                            "outline": "none",
                            "box_shadow": "none",
                        },
                        type_="password",
                    ),
                    padding="0px",
                    width=Login.password_width_confirm,
                    border_bottom=f"2px solid {Login.password_underline_color_confirm}",
                    transition="width 0.65s ease 0.65s",
                ),
            ),
            rx.spacer(),
            rx.cond(
                Login.cond_create_user,
                rx.box(
                    rx.button(
                        "Crear usuario",
                        width  = "10.5em",
                        height= "3em",
                        on_click= lambda:Login.registrar_user_submit(),
                        style=style_gris_pizzarra_button
                    ),
                min_width="auto",
                height="50px",
                justify_content="center",
                center_content=True,
                opacity="1",  
                transition="opacity 0.65s ease",
            ),
            )
        ),
        width=Login.box_width_register,
        height=Login.box_height_register,
        bg="#1D2330",
        border_radius="5px",
        padding="8px",
        display="grid",
        position="relative",
        overflow="hidden",
        transition="width 0.65s, height 0.65s cubic-bezier(0.175, 0.885, 0.32, 1.275)",
        on_click=lambda: Login.open_box_register()
    ),
    rx.cond(Login.mensaje_contraseña,
            rx.box(
                mensaje_alerta("La contraseña debe tener mas de 6 caracteres"),
                margin_top=Size.VERY_SMALL.value
                )
            ),
    margin_top="7em",
    )


def user_list():
    return rx.foreach(
        PageState.user_list,
        box_marron_eliminar_user  
    )
    
    
def box_marron_eliminar_user(item):
    return rx.hstack(
    box_marron(item.fullname),
    trigger_eliminar_usuario(trigger_eliminar(), "¿Segura que desea eliminar este usuario?", "El usuario sera eliminado de la base de datos","/usuarios",item.id, item.user_uid),
    spacing="1")
    
def trigger_eliminar():
    return rx.button(
        rx.text("Eliminar"),
        style=style_ceramica_roja_button,
        width = Size.MEDIUM.value
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
        rx.cond(item.mails,
                rx.cond(item.mails.length() == 1,
                    rx.cond(
                        PageState.fecha.to_string() == item.fecha.to_string(),
                        rx.box(box_ceramica_azul(f"El dia  {item.dia} {item.fecha} a las {item.hora} viene: {item.mails}"),
                            rx.hstack(
                                trigger_insertar_usuario(item),
                                trigger_remover_usuario(item)
                            )
                        )
                    ),
                    rx.cond(
                        PageState.fecha.to_string() == item.fecha.to_string(),
                        rx.box(box_ceramica_azul(f"El dia  {item.dia} {item.fecha} a las {item.hora} vienen: {item.mails}"),
                            rx.hstack(
                                trigger_insertar_usuario(item),
                                trigger_remover_usuario(item)
                            )
                        )
                    )
                ),
            rx.cond(
                PageState.fecha.to_string() == item.fecha.to_string(),
                rx.box(box_ceramica_azul(f"El dia  {item.dia} {item.fecha} a las {item.hora} no viene ningun alumno"),
                    rx.hstack(
                        trigger_insertar_usuario(item),
                    )
                )
            )
        ),
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


def foreach_fechas():
    return rx.vstack(
        rx.foreach(
        PageState.filtered_list_fecha,
        mostrar_clases
    ))

def total_horarios_para_cancelar():

    horarios = PageState.total_info
    
    return rx.vstack(
        rx.cond(Login.mi_cookie,
            rx.cond(PageState.in_clase,
                rx.foreach(
                    horarios,
                    lambda item, index: text_box_para_cancelar(item, index)
                ),
                mensaje_alerta("Todavia no tiene ningun horario asignado")
            )
        ),
        padding_top= "3em"
    )

def total_horarios():

    horarios = PageState.total_info
    
    return rx.vstack(
        rx.cond(horarios,
            rx.box(
                rx.foreach(
                    horarios,
                    lambda item, index: text_box(item, index)
                ),
            margin_top="1em"),
            rx.heading("Todavia no esta inscripto en ninguna clase", size= "4"),
        ),
    )
    
def mensaje_alerta(text):
    return rx.box(
        rx.hstack(
            rx.icon(tag="triangle-alert", padding = "0px"),
            rx.text.strong(text),
            spacing="1",
        ),
        style=style_perla_box
    )

def horarios_info(text, function):
    return rx.box(
        rx.hstack(
            rx.text.strong(text, on_click=function),
            spacing="1",
            margin_left = "7px",
            _hover={
                "color": "#808080",
            },
        ),
        style=style_perla_box
    )
    
    
def mensaje_fall(text):
    return rx.box(
        rx.hstack(
            rx.text.strong(text),
            spacing="1",
        ),
        style=style_ceramica_roja_box,
    ),

def mensaje_check(text):
    return rx.box(
        rx.hstack(
            rx.text.strong(text),
            spacing="1"
        ),
        style=style_verde_esmeralda_button
    )
    
def error_momentaneo():
    return rx.toast.error("Error!", z_index=100, use_portal=True)

def check_momentaneo():
    return rx.toast.success("Success!", z_index=100, use_portal=True)

def text_box_para_cancelar(item, index):
   
    return rx.cond(item.mails.contains(Login.mi_cookie),
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
                trigger_alert(button_red(item), "Cancelacion exitosa", f"Se ha cancelado la clase del dia {item.dia} {item.fecha} a las {item.hora}. Se ha generado un credito para que puedas recuperar la clase." , "/mis_horarios", check_momentaneo),
                trigger_alert(button_red(item), "Cancelacion exitosa", f"Se ha cancelado la clase del dia {item.dia} {item.fecha} a las {item.hora}. Ten en cuenta que no podras recuperar esta clase ya que no cumple con la condicion de cancelar con 24hs de anticipacion" , "/mis_horarios", None)    
            )
        )
    )

def text_box(item, index):
   
    return rx.cond(
        item.mails.contains(Login.mi_cookie),
        rx.heading(f"{item.dia} {item.fecha} a las {item.hora}", size="4"),
    )

def proxima_clase_info():
    return rx.cond(Login.mi_cookie,
        box_perla(PageState.tiempo_hasta_proxima_clase),
        mensaje_alerta("Para ver los horarios de tus clases debes iniciar sesion")
    )
            
def submit_button():
    return rx.button(
        rx.text("Buscar", color= "black"),
        type= "submit",
        width = "9em",
        style=style_perla_button
    )

def dias_semanales():

    return rx.center(
        rx.vstack(
            rx.foreach(
                PageState.filtered_list_semana,
                button_prueba_dias
            ),
            rx.hstack(
                rx.button(rx.icon("arrow-left", color = "black"), on_click=PageState.anterior, style= style_perla_button, width = Size.SMALL.value),
                rx.button(rx.icon("arrow-right", color = "black"), on_click=PageState.siguiente, style= style_perla_button, width = Size.SMALL.value),
            ),
            width = "100%"
        ),
    )

def alert():
    return rx.vstack(
        box_marron("Antes de cancelar una clase por favor lea atentamente haciendo click en las condiciones:"),
        trigger_alert(button_rubi(),"Recuperar clase",  "Para poder recuperar una clase es indispensable cancelar con 24hs de anticipacion de lo contrario no podra ser recuperada", "/mis_horarios", None),
    )



def trigger_alert(button, title, dialogo,rute,on_click):
    return rx.alert_dialog.root(
            rx.alert_dialog.trigger(
                button,
                on_click=on_click
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

def trigger_eliminar_usuario(button, title, dialogo, rute , id, user_uid):
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
                        button_eliminar_user(rute, id, user_uid),
                    ),
                    rx.alert_dialog.cancel(
                        button_cancel(),
                    ),
                    spacing="3",
                ),
            ),
        )
    
def trigger_mover_usuarios(button, title, dialogo, rute, mover_usuario):
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
                        mover_usuario,
                    ),
                    rx.alert_dialog.cancel(
                        button_cancel_desplazamiento(),
                    ),
                    spacing="3",
                ),
            ),
        )
    
def trigger_insertar_usuario(item):
    
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button(
            rx.text.strong("Insertar usuario", color = "black"), 
            style=style_perla_button, 
            width = Size.BUTTON_TRIGGER.value,
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
                    rx.select(
                        PageState.list_personas,
                        value=PageState.user_clase,
                        placeholder= "usuario",
                        on_change=PageState.set_user_clase,
                    ),
                    rx.cond(PageState.fecha.to_string() == item.fecha.to_string(),
                        rx.select(
                        [item.fecha],
                        value=PageState.fecha_seleccion_horarios,
                        placeholder= "fecha",
                        on_change= PageState.set_fecha_seleccion_horarios
                        )
                    ),
                    rx.cond(
                        PageState.fecha.to_string() == item.fecha.to_string(),
                        rx.select(
                        [item.hora],
                        placeholder= "hora",
                        value=PageState.seleccionar_hora,
                        on_change= PageState.set_seleccionar_hora
                        )
                    ),      
                ),rx.hstack(
                    rx.flex(
                        rx.alert_dialog.action(
                            rx.button(
                                rx.text.strong("Aceptar", color= "black"), 
                                type="submit", width ="10em",
                                style=style_perla_button,
                                on_click=rx.redirect("/gestion_horarios")
                            ),
                        ),
                        rx.alert_dialog.cancel(
                            rx.button(
                            rx.text.strong("cancelar", color= "black"),
                            width="10em",
                            style=style_perla_button
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

def trigger_remover_usuario(item):
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button(
            rx.text.strong("Remover usuario", color = "black"), 
            style=style_perla_button, 
            width = Size.BUTTON_TRIGGER.value,
            margin_top ="3px",
        ),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Remover usuario de la clase:"),
        rx.alert_dialog.description(
            rx.vstack( 
        rx.form.root(
            rx.vstack(
                rx.hstack(
                    rx.cond(PageState.fecha.to_string() == item.fecha.to_string(),
                        rx.select(
                            PageState.list_personas,
                            value=PageState.user_clase,
                            placeholder= "usuario",
                            on_change=PageState.set_user_clase,
                        )
                    ),
                    rx.cond(PageState.fecha.to_string() == item.fecha.to_string(),
                        rx.select(
                        [item.fecha],
                        value=PageState.fecha_seleccion_horarios,
                        placeholder= "fecha",
                        on_change= PageState.set_fecha_seleccion_horarios
                        )
                    ),
                    rx.cond(
                        PageState.fecha.to_string() == item.fecha.to_string(),
                        rx.select(
                        [item.hora],
                        placeholder= "hora",
                        value=PageState.seleccionar_hora,
                        on_change= PageState.set_seleccionar_hora
                        )
                    ),
                ),rx.hstack(
                    rx.flex(
                        rx.alert_dialog.action(
                            rx.button(
                                rx.text.strong("Aceptar", color= "black"), 
                                type="submit", width ="10em",
                                style=style_perla_button,
                                on_click=rx.redirect("/gestion_horarios")
                            ),
                        ),
                        rx.alert_dialog.cancel(
                            rx.button(
                            rx.text.strong("cancelar", color= "black"),
                            width="10em",
                            style=style_perla_button
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



def box_marron(item):
    return rx.hstack(
    rx.box(
        rx.text.strong(item, color = "black"),     
        style=style_marron_box
    ),
)



def box_perla(text):
    return rx.vstack(
        rx.box(
            rx.text.strong(text, color = "black"),
            
            style=style_perla_box
        )
    )

def box_ceramica_azul(text):
    return rx.vstack(
        rx.box(
            rx.text.strong(text, color = "black"),
            
            style=style_ceramica_azul_box
        )
    )

def box_gris_pizzarra(text):
    return rx.vstack(
        rx.box(
            rx.text.strong(text, color = "black"),
            style=style_gris_pizzarra_box
        )
    )

def trigger_desplazar_derecha():
    return rx.box(
        rx.tablet_and_desktop(
            rx.button(
            rx.hstack(
                rx.text("Mover todos a la clase siguiente"),
                rx.icon("arrow-right", color = "black"),

                ), 
            style= style_perla_button, 
            width = "19em",
            ),
        ),
        rx.mobile_only(
            rx.button(
            rx.text("Mover todos a la clase siguiente"),
            style= style_perla_button, 
            width = "11em"
            ),
        ),
        padding_top="3em"
    )

def trigger_desplazar_izquierda():
    return rx.box(
        rx.tablet_and_desktop(
            rx.button(
            rx.hstack(
                rx.icon("arrow-left", color = "black"),
                rx.text("Mover todos a la clase anterior")
                ), 
            style= style_perla_button, 
            width = "19em"
            )
        ),
        rx.mobile_only(
            rx.button(
            rx.text("Mover todos a la clase anterior"),
            style= style_perla_button, 
            width = "11em"
            ),
        ),
        padding_top="3em"
    )

def button_mover_derecha():
    return rx.button(
        rx.text.strong("Aceptar", color="black"),
        on_click=[ReservaCancela.desplazando_derecha(), rx.redirect("/gestion_horarios/")],
        width="15em",
        style=style_marron_button
        )
    
    
def button_mover_izquierda():
    return rx.button(
        rx.text.strong("Aceptar", color="black"),
        on_click=[ReservaCancela.desplazando_izquierda(), rx.redirect("/gestion_horarios/")],
        width="15em",
        style=style_marron_button
        )

def button_clase(item : Total):    

    return rx.center(
        rx.cond(item.semana == PageState.semana,  
                rx.cond(
                    item.lugar_disponible > 0,
                    rx.cond(~ Login.mi_cookie,
                            trigger_alert(button_green(item), "Accede a tu Cuenta", "Para poder inscribirte a una clase debes iniciar sesión", "/turnos", error_momentaneo),
                        rx.cond(
                                item.mails.contains(Login.mi_cookie),
                                trigger_alert(button_green(item), "Ya tenes clase este dia!", "No puedes inscribirte dos veces en la misma clase", "/turnos", error_momentaneo),                            
                            rx.cond(
                                    (PageState.check_cant_clases > 0) | (PageState.check_recuperar > 0),
                                    trigger_alert(button_green(item), "Incripcion exitosa", f"se ha inscripto exitosamente a la clase el dia {item.dia} {item.fecha} a las {item.hora}", "/turnos", check_momentaneo),                            rx.cond(
                                    (PageState.check_cant_clases == 0) & (PageState.check_recuperar == 0) & (PageState.check_trigger_alert == 0 ),
                                    trigger_alert(button_green(item), "No puedes sumarte a esta clase", 'Ya tienes todas tus clases asignadas del mes, consultalo en "mis horarios" ', "/turnos", error_momentaneo),
                                    rx.cond(
                                        (PageState.check_trigger_alert > 0 ),
                                        trigger_alert(button_green(item), "No puedes sumarte a esta clase", "Para recuperar una clase debes cancelar con 24hs de anticipacion", "/turnos", error_momentaneo),
                                    )
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


def button_green(item) -> rx.Component:
        return rx.button(
                rx.text(f"{item.dia} {item.fecha} a las {item.hora}"),
                on_click=ReservaCancela.agregar_usuario(item.id, Login.mi_cookie , True),
                style=style_verde_esmeralda_button,
                border_radius="6px",
                width= "14.5em",
            )
        
        
def button_red(item) -> rx.Component:
        return rx.button(
                    rx.text("cancelar"),
                    on_click=ReservaCancela.eliminar_usuario(item.id, Login.mi_cookie, True),
                    style=style_ceramica_roja_button,
                )

def button_cancel():
    return rx.button(
        rx.text.strong("Cancelar", color="black"),
        style=style_perla_button,
        width=Size.MEDIUM.value
    )
    
def button_cancel_desplazamiento():
    return rx.button(
        rx.text.strong("Cancelar", color="black"),
        style=style_marron_button,
        width="15em"
    )

def button_eliminar_user(rute, id, user_uid):
    return rx.link(
    rx.button(
        rx.text.strong("Eliminar", color="black"),
        style=style_perla_button,
        width = Size.MEDIUM.value,
        on_click=ReservaCancela.eliminar_usuario_de_bd(id, user_uid)
        ),
    href=rute
    )

def button_disabled(item) -> rx.Component:
    return rx.center(
        rx.button(
            rx.text(f"{item.dia} {item.fecha} a las {item.hora}"),
            disabled=True,
            bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
            border_radius="6px",
            padding="5px",
            width= "14.5em",
        )
    ) 

def crear_usuario_button():
    return rx.center(
        rx.mobile_only(
            rx.link(
                rx.button(
                    rx.text("Crear usuario"),
                    style=style_gris_pizzarra_button,
                    width = Size.MEDIUM.value,
                    height = Size.LOGIN_BUTTONS_MOBIL.value
                ),
                href="/crear_usuario"
            )
        ),
        rx.tablet_and_desktop(
            rx.link(
                rx.button(
                    rx.text("Crear usuario"),
                    style=style_gris_pizzarra_button,
                    width = Size.MEDIUM.value,
                    height = Size.LOGIN_BUTTONS_DESKTOP.value
                ),
                href="/crear_usuario"
            )
        )
    )

def iniciar_sesion_button():
    return rx.center(
        rx.mobile_only(
            rx.link(
                rx.button(
                    rx.text("Iniciar sesion"),
                    style=style_gris_pizzarra_button,
                    width = Size.MEDIUM.value,
                    height = Size.LOGIN_BUTTONS_MOBIL.value
                ),
                href="/login"
            )
        ),
        rx.tablet_and_desktop(
            rx.link(
                rx.button(
                    rx.text("Iniciar sesion"),
                    style=style_gris_pizzarra_button,
                    width = Size.MEDIUM.value,
                    height = Size.LOGIN_BUTTONS_DESKTOP.value
                ),
                href="/login"
            )
        )
    )
    
def button_sign_out():
    return rx.link(
        rx.button(
            rx.text("Cerrar sesion"),
            on_click=[
                rx.remove_cookie("cookie"),
                rx.remove_cookie("user_cookie")
                ],
            style=style_gris_pizzarra_button,
            width = Size.MEDIUM.value
        ),
        href="/"
    )

def footer() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.box(
            rx.center(
                rx.chakra.responsive_grid(
                    contacto("/instagram-brands-solid.svg", "taller_ceramica_ricardo_rojas", "https://www.instagram.com/taller_ceramica_ricardo_rojas"),
                    contacto("/whatsapp-brands-solid.svg", "1532820164", "https://wa.me/1532820164"),
                    columns=[1,2],
                    width= "35em",
                    margin_top="2em",
                    margin_left="5em",
                ),
            ),
            height = "6em",
            widht="100%",
            background="#1F2828",
            margin_top="3em"
        )
        ),
    rx.mobile_only(
        rx.box(
            rx.center(
                rx.chakra.responsive_grid(
                    contacto("/instagram-brands-solid.svg", "taller_ceramica_ricardo_rojas", "https://www.instagram.com/taller_ceramica_ricardo_rojas"),
                    contacto("/whatsapp-brands-solid.svg", "1532820164", "https://wa.me/1532820164"),
                    columns=[1,2],
                    width= "15em",
                    spacing="4",
                    margin_top="1em",
                    margin_right="5em",
                ),
            ),
            height = "7em",
            widht="100%",
            background="#1F2828",
            margin_top="3em"
        )
    )
    )
    
def contacto(imagen, text, url):
    return rx.link(
        rx.hstack(
            rx.image(
            src=imagen,
            width= "2em",
            height= "2em"
            ),
            rx.text.strong(text, color="white", margin_top="3px"),
            spacing="1"
        ),
        href=url,
        is_external=True
    )


def navbar() -> rx.Component:
    return rx.box(
            rx.hstack(
                rx.box(
                    rx.hstack(
                        rx.mobile_only(
                            rx.link(
                                rx.text("Taller de ceramica",
                                    white_space="normal",
                                    width ="4.5em",
                                    _hover={"color": "linear-gradient(145deg, #708090, #4e5964)"}
                                ),
                                href="/",
                                color =  "#FCFDFD"
                            )
                        ),
                        rx.tablet_and_desktop(
                            rx.link(
                                rx.text("Taller de ceramica",
                                    padding_left=Size.VERY_SMALL.value,
                                    white_space="normal",
                                    _hover={"color":"#4e5964"}
                                ),
                                href="/",
                                color =  "#FCFDFD",
                                width ="9em"
                            )
                        ),
                    options_button(),
                    desplegable_button()
                    )
                ),
                rx.spacer(),
            rx.box(
                rx.cond(
                    Login.mi_cookie,
                    rx.box(
                        rx.hstack(
                        button_sign_out(),
                        width = "100%",
                        align_items="end")
                    ),
                    rx.chakra.responsive_grid(
                        crear_usuario_button(),
                        iniciar_sesion_button(),
                        width = "100%",
                        align_items="end",
                        columns=[1, 2],
                        spacing="1",
                        margin_right = Size.VERY_SMALL.value
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

def options_button():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.button(
                rx.icon("align-justify", color="white"),
                variant="ghost",
                size="2",
                width="2em",
                height= "2em",
                padding_x="0px",
                style={
                    "background_color": "#808080"
                }
            ),
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.cond(Login.mi_cookie,
                        rx.box(
                            rx.heading(Login.mi_cookie, size="8"),
                            rx.cond(PageState.in_clase,
                                rx.heading("Tenes clase los dias:", size="5", margin_top="2em"),
                                rx.heading("No tiene ningun horario asignado", size="5", margin_top="2em")
                            ),
                            total_horarios(),
                        ),
                        rx.link(
                            rx.heading("¡Primero debes iniciar sesión!", size="8"),
                            href="/login"
                        )
                    )
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="2em",
                background_color=rx.color("gray", 1),
                z_index="6",
            )
        ),
        direction="left",
    )

def desplegable_button():
    return rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.icon("chevron-down", color="white"),
                    variant="ghost",
                    size="2",
                    width="2em",
                    height= "2em",
                    style={
                        "background_color": "#808080"
                    }
                ),
            ),
            rx.menu.content(
                button_menu("Turnos", "/turnos"),
                button_menu("Mis horarios", "/mis_horarios"),
                button_menu("Configuracion", "/configuracion"),
                rx.cond((Login.mi_cookie == "Manuel Navarro") | (Login.mi_cookie == "Ivanna Risaro"),
                    rx.box(
                        rx.vstack(
                            button_menu("gestion horarios", "/gestion_horarios"),
                            button_menu("alumnos/as", "/usuarios"),
                            spacing="0"
                        )
                    )
                ),
            ),
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
                style=style_gris_pizzarra_button, 
                width =Size.BUTTON_DAYS.value ,
                on_click=ButtonState.toggle_text(item.dia),
            )
        ),
        dias_clases(ButtonState.show_text_lunes,"lunes",PageState.filtered_list_lunes,item),
        dias_clases(ButtonState.show_text_martes,"martes",PageState.filtered_list_martes,item),
        dias_clases(ButtonState.show_text_miercoles,"miercoles",PageState.filtered_list_miercoles,item),
        dias_clases(ButtonState.show_text_jueves,"jueves",PageState.filtered_list_jueves,item),
        dias_clases(ButtonState.show_text_viernes,"viernes",PageState.filtered_list_viernes,item),
    )
    
def dias_clases(cond, dia, foreach, item):
    return rx.cond(cond,
            rx.cond(
                (item.dia == dia) & (item.semana == PageState.semana),
                rx.vstack(
                    rx.foreach(
                        foreach,
                        button_clase
                    )
                )
            )
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
    },
    rx.link: {
        "color": "#FCFDFD",
        "text_decoration": "none",
        "_hover": {
            "color": "#13171B"
        }
    }
}

style_presentacion =  dict(
    bg="#DFC57B", 
    border="1px solid #ddd", 
    border_radius="10px",  
    box_shadow="2px 2px 5px rgba(0, 0, 0, 0.1)",  
    font_size="1.2em",  
    # color="#333",  
)

style_ceramica_azul_button = dict(
    bg="linear-gradient(145deg, #a7c7d9, #89a5b7)",
    border="2px solid #6b8399",
    border_radius="5px",
    box_shadow="1px 1px 2px #5a6f80, -1px -1px 2px #ffffff",
    color="#2c4b6b",
    font_weight="bold",
    padding="5px",
    _hover={
        "bg": "linear-gradient(145deg, #89a5b7, #a7c7d9)",
        "box_shadow": "inset 5px 5px 10px #5a6f80, inset -5px -5px 10px #ffffff",
    },
    _focus={
        "outline": "none",  # Elimina el borde de enfoque
        "box_shadow": "none",  # Elimina la sombra de enfoque
    },
    _active={
        "outline": "none",  # Elimina el borde de enfoque al presionar
        "box_shadow": "none",  # Elimina la sombra de enfoque al presionar
    },
    _webkit_tap_highlight_color= "transparent",
)

style_ceramica_azul_box = dict(
    bg="linear-gradient(145deg, #a7c7d9, #89a5b7)",
    border="2px solid #6b8399",
    border_radius="5px",
    box_shadow="1px 1px 2px #5a6f80, -1px -1px 2px #ffffff",
    color="#2c4b6b",
    font_weight="bold",
    padding="5px"
)

style_verde_esmeralda_button = dict(
    bg="#B6FF99", 
    border="2px solid #B6FF99",  
    font_weight="bold",
    border_radius="7px",
    padding="5px",
    _hover={
        "bg": "linear-gradient(145deg, #27ae60, #2ecc71)",  
        "box_shadow": "inset 1px 1px 3px #1c6c41, inset -5px -5px 10px #3ccf8e",  
    },
    _focus={
        "outline": "none",  # Elimina el borde de enfoque
        "box_shadow": "none",  # Elimina la sombra de enfoque
    },
    _active={
        "outline": "none",  # Elimina el borde de enfoque al presionar
        "box_shadow": "none",  # Elimina la sombra de enfoque al presionar
    },
    _webkit_tap_highlight_color= "transparent",
)

style_verde_esmeralda_box = dict(
    bg="#B6FF99",  
    border="2px solid #B6FF99",  
    box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
    border_radius="5px",
    font_weight="bold",
    padding="5px",
)

style_marron_button = dict(
    bg="linear-gradient(145deg, #f0e4d7, #e6d0b8)",
    border="2px solid #d4b594",
    box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
    border_radius="5px",
    font_weight="bold",
    padding="5px",
    _hover={
        "bg": "linear-gradient(145deg, #e6d0b8, #f0e4d7)",
        "box_shadow": "inset 1px 1px 3px #c1a684, inset -5px -5px 10px #ffffff",
    },
    _focus={
        "outline": "none",  # Elimina el borde de enfoque
        "box_shadow": "none",  # Elimina la sombra de enfoque
    },
    _active={
        "outline": "none",  # Elimina el borde de enfoque al presionar
        "box_shadow": "none",  # Elimina la sombra de enfoque al presionar
    },
    _webkit_tap_highlight_color= "transparent",
)

style_marron_box = dict(
    bg="linear-gradient(145deg, #f0e4d7, #e6d0b8)",
    border="2px solid #d4b594",
    border_radius="5px",
    font_weight="bold",
    padding="5px",
)

style_perla_button = dict(
    bg="linear-gradient(145deg, #d3d3d3, #b0b0b0)",
    border="2px solid #a9a9a9",
    border_radius="5px",
    box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
    color="#333333",
    font_weight="bold",
    padding="5px",
    _hover={
        "bg": "linear-gradient(145deg, #b0b0b0, #d3d3d3)",
        "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #dcdcdc",
        "transition": "background-color 1s ease"
    },
    _focus={
        "outline": "none",  # Elimina el borde de enfoque
        "box_shadow": "none",  # Elimina la sombra de enfoque
    },
    _active={
        "outline": "none",  # Elimina el borde de enfoque al presionar
        "box_shadow": "none",  # Elimina la sombra de enfoque al presionar
    },
    _webkit_tap_highlight_color= "transparent",
)

style_perla_box = dict(
    bg="linear-gradient(145deg, #d3d3d3, #b0b0b0)",
    border="2px solid #a9a9a9",
    border_radius="5px",
    box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
    color="#333333",
    font_weight="bold",
    padding="5px"
)


style_negro_mate_button= dict(
    bg="linear-gradient(145deg, #2e2e2e, #1a1a1a)",
    border="2px solid #1a1a1a",
    border_radius="5px",
    box_shadow="1px 1px 2px #151515, -1px -1px 2px #333333",
    color="#a9a9a9",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease",
    width= "11em",
    _hover={
        "bg": "linear-gradient(145deg, #1a1a1a, #2e2e2e)",
        "box_shadow": "inset 2px 2px 5px #151515, inset -2px -2px 5px #333333",
    },
    _focus={
        "outline": "none",  # Elimina el borde de enfoque
        "box_shadow": "none",  # Elimina la sombra de enfoque
    },
    _active={
        "outline": "none",  # Elimina el borde de enfoque al presionar
        "box_shadow": "none",  # Elimina la sombra de enfoque al presionar
    },
    _webkit_tap_highlight_color= "transparent",
)

style_negro_mate_box= dict(
    bg="linear-gradient(145deg, #2e2e2e, #1a1a1a)",
    border="2px solid #1a1a1a",
    border_radius="5px",
    box_shadow="1px 1px 2px #151515, -1px -1px 2px #333333",
    color="#a9a9a9",
    font_weight="bold",
    padding="5px"
)

style_gris_pizzarra_button= dict(
    bg="linear-gradient(145deg, #708090, #4e5964)",
    border="2px solid #2f4f4f",
    border_radius="5px",
    box_shadow="1px 1px 2px #2f4f4f, -1px -1px 2px #778899",
    color="#ffffff",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease",
    _hover={
        "bg": "linear-gradient(145deg, #4e5964, #708090)",
        "box_shadow": "inset 1px 1px 2px #2f4f4f, inset -1px -1px 2px #778899",
    },
    _focus={
        "outline": "none",  # Elimina el borde de enfoque
        "box_shadow": "none",  # Elimina la sombra de enfoque
    },
    _active={
        "outline": "none",  # Elimina el borde de enfoque al presionar
        "box_shadow": "none",  # Elimina la sombra de enfoque al presionar
    },
    _webkit_tap_highlight_color= "transparent",
)

style_gris_pizzarra_box= dict(
    bg="linear-gradient(145deg, #708090, #4e5964)",
    border="2px solid #2f4f4f",
    border_radius="5px",
    box_shadow="1px 1px 2px #2f4f4f, -1px -1px 2px #778899",
    color="#ffffff",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease"
    )

style_gris_pizzarra_dark_button = dict(
    bg="linear-gradient(145deg, #2f4f4f, #4a4f4f)",
    border="2px solid #4e5964",
    border_radius="5px",
    box_shadow="1px 1px 2px #1c1c1c, -1px -1px 2px #4e5964",
    color="#dcdcdc",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease",
    _hover={
        "bg": "linear-gradient(145deg, #274040, #2f4f4f)",
        "box_shadow": "inset 1px 1px 2px #4e5964, inset -1px -1px 2px #1c1c1c",
    },
    _focus={
        "outline": "none",  # Elimina el borde de enfoque
        "box_shadow": "none",  # Elimina la sombra de enfoque
    },
    _active={
        "outline": "none",  # Elimina el borde de enfoque al presionar
        "box_shadow": "none",  # Elimina la sombra de enfoque al presionar
    },
    _webkit_tap_highlight_color= "transparent",
)

style_gris_pizzarra_dark_box = dict(
    bg="linear-gradient(145deg, #2f4f4f, #4a4f4f)",
    border="2px solid #4e5964",
    border_radius="5px",
    box_shadow="1px 1px 2px #1c1c1c, -1px -1px 2px #4e5964",
    color="#dcdcdc",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease"
)

style_ceramica_roja_button= dict(
    bg="linear-gradient(145deg, #e08080, #c06060)",
    border="2px solid #a04040",
    border_radius="7px",
    box_shadow="1px 1px 1px #903030, -1px -1px 1px #ffa0a0",
    color="#ffffff",
    font_weight="bold",
    padding="3px",
    transition="all 0.5s ease",
    width="7em",
    _hover={
        "bg": "linear-gradient(145deg, #A47070, #e08080)",
        "box_shadow": "inset 1px 1px 1px #b05050, inset 0px 0px 1px #ffc0c0",
    },
    _focus={
        "outline": "none",  # Elimina el borde de enfoque
        "box_shadow": "none",  # Elimina la sombra de enfoque
    },
    _active={
        "outline": "none",  # Elimina el borde de enfoque al presionar
        "box_shadow": "none",  # Elimina la sombra de enfoque al presionar
    },
    _webkit_tap_highlight_color= "transparent", 
    )

style_ceramica_roja_box= dict(
    bg="linear-gradient(145deg, #e08080, #c06060)",
    border="2px solid #a04040",
    border_radius="7px",
    box_shadow="1px 1px 1px #903030, -1px -1px 1px #ffa0a0",
    color="#ffffff",
    font_weight="bold",
    padding="3px",
    transition="all 0.5s ease"
    )


def button_rubi():
    return rx.button(
        rx.hstack(
            rx.icon(tag="triangle-alert", size=20, color = "black"),
            rx.text("Condiciones", color= "black"),
            spacing="2"),
        width= "10em",
        style=style_ceramica_roja_button,
        auto_focus=True
    )
    

def terracota():
    return rx.button(
        "Terracota",
        bg="linear-gradient(145deg, #d35400, #e67e22)",
        color="white",
        border="2px solid #c0392b",
        border_radius="5px",
        box_shadow="1px 1px 2px #a04000, -1px -1px 2px #ff8c00",
        padding="5px",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #e67e22, #d35400)",
            "box_shadow": "inset 3px 3px 6px #a04000, inset -3px -3px 6px #ff8c00",
        },
    )


def porcelana():
    return rx.button(
        "Porcelana",
        bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
        color="#333333",
        border="2px solid #bdbdbd",
        border_radius="5px",
        box_shadow="1px 1px 2px #b3b3b3, -1px -1px 2px #ffffff",
        padding="5px",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #e0e0e0, #f5f5f5)",
            "box_shadow": "inset 4px 4px 8px #b3b3b3, inset -4px -4px 8px #ffffff",
        },
    )


def ceramica_verde():
    return rx.button(
        "Cerámica Verde",
        bg="linear-gradient(145deg, #27ae60, #2ecc71)",
        color="white",
        border="2px solid #16a085",
        border_radius="5px",
        box_shadow="1px 1px 2px #1e8449, -1px -1px 2px #36d278",
        padding="5px",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #2ecc71, #27ae60)",
            "box_shadow": "inset 3px 3px 6px #1e8449, inset -3px -3px 6px #36d278",
        },
    )

def azul_y_blanco():
    return rx.button(
        "Azul y Blanco",
        bg="linear-gradient(145deg, #3498db, #2980b9)",
        color="white",
        border="2px solid #1f618d",
        border_radius="5px",
        box_shadow="1px 1px 2px #2874a6, -1px -1px 2px #3ea1e6",
        padding="5px",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #2980b9, #3498db)",
            "box_shadow": "inset 4px 4px 8px #2874a6, inset -4px -4px 8px #3ea1e6",
        },
    )
    

def Cerámica_Verde_Jade():
    return rx.button(
        "Cerámica Verde Jade",
        bg="linear-gradient(145deg, #00a86b, #008c57)",
        border="2px solid #006400",
        border_radius="5px",
        box_shadow="1px 1px 2px #006400, -1px -1px 2px #32cd32",
        color="#ffffff",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #008c57, #00a86b)",
            "box_shadow": "inset 2px 2px 5px #006400, inset -2px -2px 5px #32cd32",
        },
    )


def Cerámica_Verde_Oliva():
    return rx.button(
        "Cerámica Verde Oliva",
        bg="linear-gradient(145deg, #808000, #6b8e23)",
        border="2px solid #556b2f",
        border_radius="5px",
        box_shadow="1px 1px 2px #556b2f, -1px -1px 2px #9acd32",
        color="#ffffff",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #6b8e23, #808000)",
            "box_shadow": "inset 2px 2px 5px #556b2f, inset -2px -2px 5px #9acd32",
        },
    )

def Cerámica_Verde_Menta():
    return rx.button(
        "Cerámica Verde Menta",
        bg="linear-gradient(145deg, #98ff98, #7fff00)",
        border="2px solid #3cb371",
        border_radius="5px",
        box_shadow="1px 1px 2px #3cb371, -1px -1px 2px #98fb98",
        color="#006400",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #7fff00, #98ff98)",
            "box_shadow": "inset 2px 2px 5px #3cb371, inset -2px -2px 5px #98fb98",
        },
    )

def Cerámica_Verde_Bosque():
    return rx.button(
        "Cerámica Verde Bosque",
        bg="linear-gradient(145deg, #228b22, #006400)",
        border="2px solid #004d00",
        border_radius="5px",
        box_shadow="1px 1px 2px #004d00, -1px -1px 2px #2e8b57",
        color="#ffffff",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #006400, #228b22)",
            "box_shadow": "inset 2px 2px 5px #004d00, inset -2px -2px 5px #2e8b57",
        },
    )

def carmica_zafiro():
    return rx.button(
    "Cerámica Zafiro",
    bg="linear-gradient(145deg, #0047AB, #4169E1)",
    border="2px solid #00008B",
    border_radius="5px",
    box_shadow="1px 1px 2px #00008B, 0px 0px 0px #1E90FF",
    color="#ffffff",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease",
    _hover={
        "bg": "linear-gradient(145deg, #4169E1, #0047AB)",
        "box_shadow": "inset 1px 1px 2px #00008B, inset -1px -1px 2px #1E90FF",
    },
)

def ceramica_azul_oscuro():
    return rx.button(
    "Cerámica Azul Oscuro",
    bg="linear-gradient(145deg, #000080, #191970)",
    border="2px solid #00008B",
    border_radius="5px",
    box_shadow="1px 1px 1px #000033, 1px 1px 1px #0000CD",
    color="#E6E6FA",
    font_weight="bold",
    padding="5px",
    width= "11em",
    transition="all 0.3s ease",
    _hover={
        "bg": "linear-gradient(145deg, #191970, #000080)",
        "box_shadow": "inset 2px 2px 5px #000033, inset -2px -2px 5px #0000CD",
    },
)

def CerámicaNegroÉbano(): 
    return rx.button(
        "Cerámica Negro Ébano",
        bg="linear-gradient(145deg, #1c1c1c, #0a0a0a)",
        border="2px solid #000000",
        border_radius="5px",
        box_shadow="1px 1px 2px #000000, -1px -1px 2px #2c2c2c",
        color="#d3d3d3",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #0a0a0a, #1c1c1c)",
            "box_shadow": "inset 2px 2px 5px #000000, inset -2px -2px 5px #2c2c2c",
        },
    )


def CerámicaNegroMate():
    return rx.button(
        "Cerámica Negro Mate",
        bg="linear-gradient(145deg, #2e2e2e, #1a1a1a)",
        border="2px solid #1a1a1a",
        border_radius="5px",
        box_shadow="1px 1px 2px #151515, -1px -1px 2px #333333",
        color="#a9a9a9",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #1a1a1a, #2e2e2e)",
            "box_shadow": "inset 2px 2px 5px #151515, inset -2px -2px 5px #333333",
        },
    )

def CerámicaNegroCarbón():
    return rx.button(
        "Cerámica Negro Carbón",
        bg="linear-gradient(145deg, #363636, #1e1e1e)",
        border="2px solid #2c2c2c",
        border_radius="5px",
        box_shadow="1px 1px 2px #1c1c1c, -1px -1px 2px #3a3a3a",
        color="#c0c0c0",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #1e1e1e, #363636)",
            "box_shadow": "inset 2px 2px 5px #1c1c1c, inset -2px -2px 5px #3a3a3a",
        },
    )

def CerámicaNegroObsidiana():
    return rx.button(
        "Cerámica Negro Obsidiana",
        bg="linear-gradient(145deg, #0f0f0f, #050505)",
        border="2px solid #000000",
        border_radius="5px",
        box_shadow="1px 1px 2px #000000, -1px -1px 2px#1a1a1a",
        color="#e0e0e0",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "11em",
        _hover={
            "bg": "linear-gradient(145deg, #050505, #0f0f0f)",
            "box_shadow": "inset 2px 2px 5px #000000, inset -2px -2px 5px #1a1a1a",
        },
    )    
def CerámicaGrisClaro():
    return rx.button(
        "Cerámica Gris Claro",
        bg="linear-gradient(145deg, #e0e0e0, #c0c0c0)",
        border="2px solid #a9a9a9",
        border_radius="5px",
        box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #ffffff",
        color="#333333",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "15em",
        _hover={
            "bg": "linear-gradient(145deg, #c0c0c0, #e0e0e0)",
            "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #ffffff",
        },
    )


def CerámicaGrisMedio():
    return rx.button(
        "Cerámica Gris Medio",
        bg="linear-gradient(145deg, #a0a0a0, #808080)",
        border="2px solid #696969",
        border_radius="5px",
        box_shadow="1px 1px 2px #696969, -1px -1px 2px #b8b8b8",
        color="#ffffff",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "15em",
        _hover={
            "bg": "linear-gradient(145deg, #808080, #a0a0a0)",
            "box_shadow": "inset 1px 1px 2px #696969, inset -1px -1px 2px #b8b8b8",
        },
    )

def CerámicaGrisPizarra():
    return rx.button(
        "Cerámica Gris Pizarra",
        bg="linear-gradient(145deg, #708090, #4e5964)",
        border="2px solid #2f4f4f",
        border_radius="5px",
        box_shadow="1px 1px 2px #2f4f4f, -1px -1px 2px #778899",
        color="#ffffff",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "15em",
        _hover={
            "bg": "linear-gradient(145deg, #4e5964, #708090)",
            "box_shadow": "inset 1px 1px 2px #2f4f4f, inset -1px -1px 2px #778899",
        },
    )

def CerámicaGrisPerla():
    return rx.button(
        "Cerámica Gris Perla",
        bg="linear-gradient(145deg, #d3d3d3, #b0b0b0)",
        border="2px solid #a9a9a9",
        border_radius="5px",
        box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
        color="#333333",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "15em",
        _hover={
            "bg": "linear-gradient(145deg, #b0b0b0, #d3d3d3)",
            "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #dcdcdc",
        },
    )

def CerámicaGrisCarbón():
    return rx.button(
        "Cerámica Gris Carbón",
        bg="linear-gradient(145deg, #4d4d4d, #333333)",
        border="2px solid #2b2b2b",
        border_radius="5px",
        box_shadow="1px 1px 2px #2b2b2b, -1px -1px 2px #555555",
        color="#e0e0e0",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width= "15em",
        _hover={
            "bg": "linear-gradient(145deg, #333333, #4d4d4d)",
            "box_shadow": "inset 2px 2px 5px #2b2b2b, inset -2px -2px 5px #555555",
        },
    )

def ceramica_button_rojo():
    return rx.button(
        "Cerámica Roja",
        bg="linear-gradient(145deg, #ff6b6b, #d64545)",
        border="2px solid #c13e3e",
        border_radius="5px",
        box_shadow="1px 1px 2px #c13e3e, -1px -1px 2px #ff7373",
        color="#ffffff",
        font_weight="bold",
        padding="5px",
        transition="all 0.3s ease",
        width="15em",
        _hover={
            "bg": "linear-gradient(145deg, #d64545, #ff6b6b)",
            "box_shadow": "inset 2px 2px 5px #c13e3e, inset -2px -2px 5px #ff7373",
        },
    )
    
def CerámicarojaTerracota():
    return rx.button(
    "Cerámica Roja Terracota",
    background_image="linear-gradient(144deg,#CD5C5C,#A52A2A 50%,#8B4513)",
    border="2px solid #A52A2A",
    border_radius="5px",
    box_shadow="1px 1px 2px #8B4513, -1px -1px 2px #CD5C5C",
    color="white",
    font_weight="bold",
    padding="5px",
    width="15em",
    _hover={
        "opacity": 0.5,
    },
)
    
def Cerámica_Roja_Clara():
    return rx.button(
    "Cerámica Roja Clara",
    background_image="linear-gradient(144deg,#FF6347,#FF4500 50%,#FF8C00)",
    border="2px solid #FF4500",
    border_radius="5px",
    box_shadow="1px 1px 2px #FF4500, -1px -1px 2px #FFA07A",
    color="white",
    font_weight="bold",
    padding="5px",
    width="15em",
    _hover={
        "opacity": 0.5,
    },
)
    

def ceramica_button_rojo4():
    return rx.button(
                "Ceramic Button 4",
                style={
                    "background": "linear-gradient(to bottom, #ff6b6b, #ee5253)",
                    "color": "white",
                    "border": "2px solid #ee5253",
                    "padding": "10px 25px",
                    "border-radius": "10px",
                    "box-shadow": "0 6px 8px rgba(0, 0, 0, 0.1)",
                    "font-size": "16px",
                    "font-weight": "bold",
                    "cursor": "pointer",
                    "transition": "transform 0.3s ease",
                },
                hover={
                    "transform": "scale(1.1)",
                },
        width= "15em",
            )
        

app = rx.App(
    style=BASE_STYLE,
    )
app.add_page(index)
app.add_page(turnos)
app.add_page(mis_horarios)
app.add_page(gestion_horarios)
app.add_page(crear_usuario)
app.add_page(login)

    
