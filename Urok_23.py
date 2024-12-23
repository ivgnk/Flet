# https://www.youtube.com/watch?v=OcrEMgx7OjE&list=PL0lO_mIqDDFVZr9lLryYHSbAbrn3YJGbE
# Изучение Python UI (GUI Apps) / #1 – Разработка программ с графическим интерфейсом на Питон
import flet as ft

def main(page: ft.Page):
    # Use a breakpoint in the code line below to debug your script.
    page.title="GravMagn"
    # page.theme_mode = 'dark'
    page.theme_mode='light'
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    usr_label = ft.Text('Info', color='#ff0000')
    usr_text  = ft.TextField(value='0', width=150, text_align=ft.TextAlign.CENTER)
    def get_info(e):
        usr_label.value=usr_text.value
        page.update()

    page.add(
        ft.Row([
            ft.IconButton(ft.Icons.HOME, on_click=get_info),
            ft.Icon(ft.Icons.BACK_HAND),
            ft.ElevatedButton(text="Click me Ele", on_click=get_info),
            ft.OutlinedButton(text="Click me Out", on_click=get_info),
            ft.Checkbox(label='Вы согласны?', value=True, on_change=get_info)
        ],
        alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            usr_label,
            usr_text
        ],
            alignment=ft.MainAxisAlignment.CENTER),

    )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)
    ft.app(target=main, view=ft.AppView.FLET_APP_WEB)
