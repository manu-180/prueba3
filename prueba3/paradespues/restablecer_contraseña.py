    # def restablecer_contraseña_link(self):
    #     try:
    #         response = supabase.supabase.auth.reset_password_email(
    #             self.email_value_login,
    #             options={
    #                 'redirect_to': 'https://ceramica.reflex.run/restablecer_contrasenia'
    #             }
    #         )
    #         self.mensaje_link= f"Se envio un link para restablecer la contraseña a {self.email_value_login}"
    #         self.cond_link_incorrecto = False
    #         self.cond_link_error = False
    #         self.cond_link_correcto = True
            
    #     except Exception as e:
    #         self.mensaje_link=f'Probablemente hayas alcanzado el limite para enviar links, hay que esperar una hora. Pero en concreto el error es: ({e}). Si no dice  "email rate limit exceeded" intenta devuelta, fijate de que no hayan espacios de mas, y por las dudas volve a inicar sesión.'
    #         self.cond_link_correcto = False
    #         self.cond_link_incorrecto = False
    #         self.cond_link_error = True
    
# @rx.page(
#     route="/restablecer_contrasenia",
#     title="restablecer_contraseña",
#     description="Taller de ceramica",
#     on_load= [
#         PageState.total,
#         PageState.actualizar_user,
#         PageState.load_data,
#         Login.close_box_contraseña
#         ])
# def restablecer_contraseña():
#     return rx.box(
#         navbar(),
#         rx.vstack(
#             rx.box(
#                 input_restablecer_contraseña()
#             )
#         )
#     )

# def input_restablecer_contraseña():
#     return rx.box(
#         rx.vstack(
#             horarios_info("Cambiar contraseña",RestablecerContraseña.open_box_contraseña()),
#             rx.vstack(
#                 rx.box(
#                     rx.chakra.input(
#                         value=RestablecerContraseña.email_value_register,
#                         placeholder=RestablecerContraseña.email,
#                         on_change=lambda email_value_register: RestablecerContraseña.on_check_email_register(email_value_register),
#                         width=RestablecerContraseña.email_width_register,
#                         transition="width 0.5s ease 0.65s",
#                         height="28px", 
#                         border_radius="4px",
#                         font_size="13px",
#                         letter_spacing="0.5px",
#                         bg="#1D2330",
#                         color="white",
#                         type="text",
#                         margin_bottom="3px",
#                         margin_left="8px",
#                         border="none",
#                         _focus={
#                             "outline": "none",
#                             "box_shadow": "none",
#                         },
#                     ),
#                     padding="0px",
#                     width=RestablecerContraseña.email_width_register,
#                     border_bottom=f"2px solid {RestablecerContraseña.email_underline_color}",
#                     transition="width 0.65s ease 0.65s",
#                 ),
#                 rx.box(
#                     rx.chakra.input(
#                         value=RestablecerContraseña.contraseña_value_register,
#                         placeholder="Ingrese contraseña",
#                         on_change=lambda contraseña_value_register: RestablecerContraseña.on_check_password_contraseña(contraseña_value_register),
#                         width=RestablecerContraseña.contraseña_width_register,
#                         transition="width 0.5s ease 0.65s",
#                         font_size="13px",
#                         height="28px", 
#                         border_radius="4px",
#                         letter_spacing="0.5px",
#                         margin_bottom="3px",
#                         border="none",
#                         _focus={
#                             "outline": "none",
#                             "box_shadow": "none",
#                         },
#                         type_="password",
#                     ),
#                     padding="0px",
#                     width=RestablecerContraseña.contraseña_width_register,
#                     border_bottom=f"2px solid {RestablecerContraseña.contraseña_underline_color}",
#                     transition="width 0.65s ease 0.65s",
#                 ),
#                 rx.box(
#                     rx.chakra.input(
#                         value=RestablecerContraseña.contraseña_value_confirm,
#                         placeholder="Confirme contraseña",
#                         on_change=lambda contraseña_value_confirm: RestablecerContraseña.on_check_password_confirm_contraseña(contraseña_value_confirm),
#                         width=RestablecerContraseña.contraseña_width_confirm,
#                         transition="width 0.5s ease 0.65s",
#                         font_size="13px",
#                         height="28px", 
#                         border_radius="4px",
#                         letter_spacing="0.5px",
#                         margin_bottom="3px",
#                         border="none",
#                         _focus={
#                             "outline": "none",
#                             "box_shadow": "none",
#                         },
#                         type_="password",
#                     ),
#                     padding="0px",
#                     width=RestablecerContraseña.contraseña_width_confirm,
#                     border_bottom=f"2px solid {RestablecerContraseña.contraseña_underline_color_confirm}",
#                     transition="width 0.65s ease 0.65s",
#                 ),
#             ),
#             rx.spacer(),
#             rx.cond(
#                 RestablecerContraseña.cond_contraseña,
#                 rx.box(
#                     rx.button(
#                         "Aceptar",
#                         width  = Size.MEDIUM.value,
#                         height= "2em",
#                         on_click= lambda:RestablecerContraseña.cambiar_contraseña(),
#                         style=style_gris_pizzarra_button
#                     ),
#                 rx.cond(RestablecerContraseña.cond_contraseña_check,
#                 rx.box(
#                     mensaje_check(RestablecerContraseña.contraseña_alert),
#                     min_width="auto",
#                     justify_content="center",
#                     center_content=True,
#                     opacity="1",  
#                     transition="opacity 0.65s ease",
#                     margin_top="1em",
#                     width=RestablecerContraseña.box_width_contraseña
#                 ),
#                 ),
#                 rx.cond(RestablecerContraseña.cond_contraseña_fall,
#                 rx.box(
#                     mensaje_fall(RestablecerContraseña.contraseña_alert),
#                     min_width="auto",
#                     justify_content="center",
#                     center_content=True,
#                     opacity="1",  
#                     transition="opacity 0.65s ease",
#                     margin_top="1em",
#                     width="13em"
#                 ),
#                 )
#             ),
#             )
#         ),
#         margin_top="1em"
#     )    

    
    
    
    # app.add_page(restablecer_contraseña)
