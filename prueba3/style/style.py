# import reflex as rx

# def ceramica_button():    
#     return rx.button(
#         "Botón Cerámica",
#         bg="linear-gradient(145deg, #f0e4d7, #e6d0b8)",
#         border="2px solid #d4b594",
#         border_radius="5px",
#         box_shadow="5px 5px 10px #c1a684, -1px -1px 2px #ffffff",
#         color="#6b4c2c",
#         font_weight="bold",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #e6d0b8, #f0e4d7)",
#             "box_shadow": "inset 5px 5px 10px #c1a684, inset -5px -5px 10px #ffffff",
#         },
#     )

# def ceramica_azul_button():
#     return rx.button(
#     "ceramica azul",
#     bg="linear-gradient(145deg, #a7c7d9, #89a5b7)",
#     border="2px solid #6b8399",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #5a6f80, -1px -1px 2px #ffffff",
#     color="#2c4b6b",
#     font_weight="bold",
#     padding="5px",
#     width= "11em",
#     _hover={
#         "bg": "linear-gradient(145deg, #89a5b7, #a7c7d9)",
#         "box_shadow": "inset 5px 5px 10px #5a6f80, inset -5px -5px 10px #ffffff",
#     },
# )

# style_ceramica_azul = dict(
#     bg="linear-gradient(145deg, #a7c7d9, #89a5b7)",
#     border="2px solid #6b8399",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #5a6f80, -1px -1px 2px #ffffff",
#     color="#2c4b6b",
#     font_weight="bold",
#     padding="5px",
#     _hover={
#         "bg": "linear-gradient(145deg, #89a5b7, #a7c7d9)",
#         "box_shadow": "inset 5px 5px 10px #5a6f80, inset -5px -5px 10px #ffffff",
#     },
# )
# style_box_marron = dict(
#     bg="linear-gradient(145deg, #f0e4d7, #e6d0b8)",
#     border="2px solid #d4b594",
#     border_radius="5px",
#     # box_shadow="5px 5px 10px #c1a684, -2px -2px 3px #ffffff",
#     color="#6b4c2c",
#     font_weight="bold",
#     padding="5px",
#     position= "sticky",  
#     top= '0',           
#     _hover={
#         "bg": "linear-gradient(145deg, #e6d0b8, #f0e4d7)",
#         "box_shadow": "inset 1px 1px 3px #c1a684, inset -5px -5px 10px #ffffff",
#     }
# )

# style_perla= dict(
#     bg="linear-gradient(145deg, #d3d3d3, #b0b0b0)",
#     border="2px solid #a9a9a9",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
#     color="#333333",
#     font_weight="bold",
#     padding="5px",
#     transition="all 0.3s ease",
#     _hover={
#         "bg": "linear-gradient(145deg, #b0b0b0, #d3d3d3)",
#         "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #dcdcdc",
#     }
#     )

# style_negro_mate= dict(
#     bg="linear-gradient(145deg, #2e2e2e, #1a1a1a)",
#     border="2px solid #1a1a1a",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #151515, -1px -1px 2px #333333",
#     color="#a9a9a9",
#     font_weight="bold",
#     padding="5px",
#     transition="all 0.3s ease",
#     width= "11em",
#     _hover={
#         "bg": "linear-gradient(145deg, #1a1a1a, #2e2e2e)",
#         "box_shadow": "inset 2px 2px 5px #151515, inset -2px -2px 5px #333333",
#     }
# )

# style_gris_pizzarra= dict(
#     bg="linear-gradient(145deg, #708090, #4e5964)",
#     border="2px solid #2f4f4f",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #2f4f4f, -1px -1px 2px #778899",
#     color="#ffffff",
#     font_weight="bold",
#     padding="5px",
#     transition="all 0.3s ease",
#     _hover={
#         "bg": "linear-gradient(145deg, #4e5964, #708090)",
#         "box_shadow": "inset 1px 1px 2px #2f4f4f, inset -1px -1px 2px #778899",
#     }
#     )

# style_gris_pizzarra_dark = dict(
#     bg="linear-gradient(145deg, #2f4f4f, #4a4f4f)",
#     border="2px solid #4e5964",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #1c1c1c, -1px -1px 2px #4e5964",
#     color="#dcdcdc",
#     font_weight="bold",
#     padding="5px",
#     transition="all 0.3s ease",
#     _hover={
#         "bg": "linear-gradient(145deg, #274040, #2f4f4f)",
#         "box_shadow": "inset 1px 1px 2px #4e5964, inset -1px -1px 2px #1c1c1c",
#     }
# )

# style_ceramica_roja= dict(
#     bg="linear-gradient(145deg, #e08080, #c06060)",
#     border="2px solid #a04040",
#     border_radius="7px",
#     box_shadow="1px 1px 1px #903030, -1px -1px 1px #ffa0a0",
#     color="#ffffff",
#     font_weight="bold",
#     padding="3px",
#     transition="all 0.5s ease",
#     width="7em",
#     _hover={
#         "bg": "linear-gradient(145deg, #A47070, #e08080)",
#         "box_shadow": "inset 1px 1px 1px #b05050, inset 0px 0px 1px #ffc0c0",
#     }
#     )

# def button_rubi():
#     return rx.button(
#         rx.hstack(
#             rx.icon(tag="triangle-alert", size=20, color = "black"),
#             rx.text("Condiciones", color= "black"),
#             spacing="2"),
#         width= "10em",
#         style=style_ceramica_roja,
#     )
    

# def terracota():
#     return rx.button(
#         "Terracota",
#         bg="linear-gradient(145deg, #d35400, #e67e22)",
#         color="white",
#         border="2px solid #c0392b",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #a04000, -1px -1px 2px #ff8c00",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #e67e22, #d35400)",
#             "box_shadow": "inset 3px 3px 6px #a04000, inset -3px -3px 6px #ff8c00",
#         },
#     )


# def porcelana():
#     return rx.button(
#         "Porcelana",
#         bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
#         color="#333333",
#         border="2px solid #bdbdbd",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #b3b3b3, -1px -1px 2px #ffffff",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #e0e0e0, #f5f5f5)",
#             "box_shadow": "inset 4px 4px 8px #b3b3b3, inset -4px -4px 8px #ffffff",
#         },
#     )


# def ceramica_verde():
#     return rx.button(
#         "Cerámica Verde",
#         bg="linear-gradient(145deg, #27ae60, #2ecc71)",
#         color="white",
#         border="2px solid #16a085",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #1e8449, -1px -1px 2px #36d278",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #2ecc71, #27ae60)",
#             "box_shadow": "inset 3px 3px 6px #1e8449, inset -3px -3px 6px #36d278",
#         },
#     )

# def azul_y_blanco():
#     return rx.button(
#         "Azul y Blanco",
#         bg="linear-gradient(145deg, #3498db, #2980b9)",
#         color="white",
#         border="2px solid #1f618d",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #2874a6, -1px -1px 2px #3ea1e6",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #2980b9, #3498db)",
#             "box_shadow": "inset 4px 4px 8px #2874a6, inset -4px -4px 8px #3ea1e6",
#         },
#     )
    

# def Cerámica_Verde_Jade():
#     return rx.button(
#         "Cerámica Verde Jade",
#         bg="linear-gradient(145deg, #00a86b, #008c57)",
#         border="2px solid #006400",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #006400, -1px -1px 2px #32cd32",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #008c57, #00a86b)",
#             "box_shadow": "inset 2px 2px 5px #006400, inset -2px -2px 5px #32cd32",
#         },
#     )


# def Cerámica_Verde_Oliva():
#     return rx.button(
#         "Cerámica Verde Oliva",
#         bg="linear-gradient(145deg, #808000, #6b8e23)",
#         border="2px solid #556b2f",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #556b2f, -1px -1px 2px #9acd32",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #6b8e23, #808000)",
#             "box_shadow": "inset 2px 2px 5px #556b2f, inset -2px -2px 5px #9acd32",
#         },
#     )

# def Cerámica_Verde_Menta():
#     return rx.button(
#         "Cerámica Verde Menta",
#         bg="linear-gradient(145deg, #98ff98, #7fff00)",
#         border="2px solid #3cb371",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #3cb371, -1px -1px 2px #98fb98",
#         color="#006400",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #7fff00, #98ff98)",
#             "box_shadow": "inset 2px 2px 5px #3cb371, inset -2px -2px 5px #98fb98",
#         },
#     )

# def Cerámica_Verde_Bosque():
#     return rx.button(
#         "Cerámica Verde Bosque",
#         bg="linear-gradient(145deg, #228b22, #006400)",
#         border="2px solid #004d00",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #004d00, -1px -1px 2px #2e8b57",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #006400, #228b22)",
#             "box_shadow": "inset 2px 2px 5px #004d00, inset -2px -2px 5px #2e8b57",
#         },
#     )

# def carmica_zafiro():
#     return rx.button(
#     "Cerámica Zafiro",
#     bg="linear-gradient(145deg, #0047AB, #4169E1)",
#     border="2px solid #00008B",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #00008B, 0px 0px 0px #1E90FF",
#     color="#ffffff",
#     font_weight="bold",
#     padding="5px",
#     transition="all 0.3s ease",
#     _hover={
#         "bg": "linear-gradient(145deg, #4169E1, #0047AB)",
#         "box_shadow": "inset 1px 1px 2px #00008B, inset -1px -1px 2px #1E90FF",
#     },
# )

# def ceramica_azul_oscuro():
#     return rx.button(
#     "Cerámica Azul Oscuro",
#     bg="linear-gradient(145deg, #000080, #191970)",
#     border="2px solid #00008B",
#     border_radius="5px",
#     box_shadow="1px 1px 1px #000033, 1px 1px 1px #0000CD",
#     color="#E6E6FA",
#     font_weight="bold",
#     padding="5px",
#     width= "11em",
#     transition="all 0.3s ease",
#     _hover={
#         "bg": "linear-gradient(145deg, #191970, #000080)",
#         "box_shadow": "inset 2px 2px 5px #000033, inset -2px -2px 5px #0000CD",
#     },
# )

# def CerámicaNegroÉbano(): 
#     return rx.button(
#         "Cerámica Negro Ébano",
#         bg="linear-gradient(145deg, #1c1c1c, #0a0a0a)",
#         border="2px solid #000000",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #000000, -1px -1px 2px #2c2c2c",
#         color="#d3d3d3",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #0a0a0a, #1c1c1c)",
#             "box_shadow": "inset 2px 2px 5px #000000, inset -2px -2px 5px #2c2c2c",
#         },
#     )


# def CerámicaNegroMate():
#     return rx.button(
#         "Cerámica Negro Mate",
#         bg="linear-gradient(145deg, #2e2e2e, #1a1a1a)",
#         border="2px solid #1a1a1a",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #151515, -1px -1px 2px #333333",
#         color="#a9a9a9",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #1a1a1a, #2e2e2e)",
#             "box_shadow": "inset 2px 2px 5px #151515, inset -2px -2px 5px #333333",
#         },
#     )

# def CerámicaNegroCarbón():
#     return rx.button(
#         "Cerámica Negro Carbón",
#         bg="linear-gradient(145deg, #363636, #1e1e1e)",
#         border="2px solid #2c2c2c",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #1c1c1c, -1px -1px 2px #3a3a3a",
#         color="#c0c0c0",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #1e1e1e, #363636)",
#             "box_shadow": "inset 2px 2px 5px #1c1c1c, inset -2px -2px 5px #3a3a3a",
#         },
#     )

# def CerámicaNegroObsidiana():
#     return rx.button(
#         "Cerámica Negro Obsidiana",
#         bg="linear-gradient(145deg, #0f0f0f, #050505)",
#         border="2px solid #000000",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #000000, -1px -1px 2px#1a1a1a",
#         color="#e0e0e0",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #050505, #0f0f0f)",
#             "box_shadow": "inset 2px 2px 5px #000000, inset -2px -2px 5px #1a1a1a",
#         },
#     )    
# def CerámicaGrisClaro():
#     return rx.button(
#         "Cerámica Gris Claro",
#         bg="linear-gradient(145deg, #e0e0e0, #c0c0c0)",
#         border="2px solid #a9a9a9",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #ffffff",
#         color="#333333",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #c0c0c0, #e0e0e0)",
#             "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #ffffff",
#         },
#     )


# def CerámicaGrisMedio():
#     return rx.button(
#         "Cerámica Gris Medio",
#         bg="linear-gradient(145deg, #a0a0a0, #808080)",
#         border="2px solid #696969",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #696969, -1px -1px 2px #b8b8b8",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #808080, #a0a0a0)",
#             "box_shadow": "inset 1px 1px 2px #696969, inset -1px -1px 2px #b8b8b8",
#         },
#     )

# def CerámicaGrisPizarra():
#     return rx.button(
#         "Cerámica Gris Pizarra",
#         bg="linear-gradient(145deg, #708090, #4e5964)",
#         border="2px solid #2f4f4f",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #2f4f4f, -1px -1px 2px #778899",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #4e5964, #708090)",
#             "box_shadow": "inset 1px 1px 2px #2f4f4f, inset -1px -1px 2px #778899",
#         },
#     )

# def CerámicaGrisPerla():
#     return rx.button(
#         "Cerámica Gris Perla",
#         bg="linear-gradient(145deg, #d3d3d3, #b0b0b0)",
#         border="2px solid #a9a9a9",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
#         color="#333333",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #b0b0b0, #d3d3d3)",
#             "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #dcdcdc",
#         },
#     )

# def CerámicaGrisCarbón():
#     return rx.button(
#         "Cerámica Gris Carbón",
#         bg="linear-gradient(145deg, #4d4d4d, #333333)",
#         border="2px solid #2b2b2b",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #2b2b2b, -1px -1px 2px #555555",
#         color="#e0e0e0",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #333333, #4d4d4d)",
#             "box_shadow": "inset 2px 2px 5px #2b2b2b, inset -2px -2px 5px #555555",
#         },
#     )

# def ceramica_button_rojo():
#     return rx.button(
#         "Cerámica Roja",
#         bg="linear-gradient(145deg, #ff6b6b, #d64545)",
#         border="2px solid #c13e3e",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #c13e3e, -1px -1px 2px #ff7373",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width="15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #d64545, #ff6b6b)",
#             "box_shadow": "inset 2px 2px 5px #c13e3e, inset -2px -2px 5px #ff7373",
#         },
#     )
    
# def CerámicarojaTerracota():
#     return rx.button(
#     "Cerámica Roja Terracota",
#     background_image="linear-gradient(144deg,#CD5C5C,#A52A2A 50%,#8B4513)",
#     border="2px solid #A52A2A",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #8B4513, -1px -1px 2px #CD5C5C",
#     color="white",
#     font_weight="bold",
#     padding="5px",
#     width="15em",
#     _hover={
#         "opacity": 0.5,
#     },
# )
    
# def Cerámica_Roja_Clara():
#     return rx.button(
#     "Cerámica Roja Clara",
#     background_image="linear-gradient(144deg,#FF6347,#FF4500 50%,#FF8C00)",
#     border="2px solid #FF4500",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #FF4500, -1px -1px 2px #FFA07A",
#     color="white",
#     font_weight="bold",
#     padding="5px",
#     width="15em",
#     _hover={
#         "opacity": 0.5,
#     },
# )
    

# def ceramica_button_rojo4():
#     return rx.button(
#                 "Ceramic Button 4",
#                 style={
#                     "background": "linear-gradient(to bottom, #ff6b6b, #ee5253)",
#                     "color": "white",
#                     "border": "2px solid #ee5253",
#                     "padding": "10px 25px",
#                     "border-radius": "10px",
#                     "box-shadow": "0 6px 8px rgba(0, 0, 0, 0.1)",
#                     "font-size": "16px",
#                     "font-weight": "bold",
#                     "cursor": "pointer",
#                     "transition": "transform 0.3s ease",
#                 },
#                 hover={
#                     "transform": "scale(1.1)",
#                 },
#         width= "15em",
#             )
    
    
    
# def colores():
#     return rx.vstack(
#         ceramica_azul_button(),    
#         ceramica_button(),
#         terracota(),
#         ceramica_button_rojo(),
#         Cerámica_Roja_Clara(),
#         CerámicarojaTerracota(),
#         ceramica_button_rojo4(),
#         ceramica_verde(),
#         azul_y_blanco(),
#         Cerámica_Verde_Bosque(),
#         Cerámica_Verde_Jade(),
#         Cerámica_Verde_Oliva(),
#         Cerámica_Verde_Menta(),
#         ceramica_azul_oscuro(),
#         CerámicaNegroCarbón(),
#         CerámicaNegroMate(),
#         CerámicaNegroObsidiana(),
#         CerámicaNegroÉbano(),
#         CerámicaGrisCarbón(),
#         CerámicaGrisClaro(),
#         CerámicaGrisMedio(),
#         CerámicaGrisPerla(),
#         CerámicaGrisPizarra(),
#     )
        