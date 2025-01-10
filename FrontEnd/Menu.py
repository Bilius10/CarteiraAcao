import flet as ft

def menu_page():
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/MenuLogo.png",  
                    width=300,  
                    height=300,  
                    fit=ft.ImageFit.CONTAIN,  
                ),

                ft.Container(height=5),

                ft.CupertinoButton(
                    content=ft.Text("Adicionar Ação", color="#f7931a", font_family="MinhaFonte", size=25),
                    width=400, height=55, bgcolor="#ffcb8c"
                ),
                ft.CupertinoButton(
                    content=ft.Text("Carteira", color="#f7931a", font_family="MinhaFonte", size=25),
                    width=400, height=55, bgcolor="#ffcb8c"
                ),
                ft.CupertinoButton(
                    content=ft.Text("Grafico", color="#f7931a", font_family="MinhaFonte", size=25),
                      width=400, height=55, bgcolor="#ffcb8c"
                ),
                ft.CupertinoButton(
                    content=ft.Text("Sair", color="#f7931a", font_family="MinhaFonte", size=25),
                    width=400, height=55, bgcolor="#ffcb8c"
                ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Alinha os elementos ao topo
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,  # Ajuste o espaçamento conforme necessário
        ),
        width=500,
        height=700,
        padding=20,
        border_radius=ft.border_radius.all(50),
        alignment=ft.alignment.center,
        image_src="C:/Users/João Vitor/IdeaProjects/CarteiraAcao/FrontEnd/Imagens/FundoMenu.png"
    )