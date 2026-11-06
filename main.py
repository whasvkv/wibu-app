import flet as ft
import requests

def main(page: ft.Page):
    page.title = "MultiStream Indo"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "adaptive"
    
    video_grid = ft.GridView(
        expand=1, runs_count=2, max_extent=200, 
        child_aspect_ratio=0.7, spacing=10, run_spacing=10
    )

    def load_content(endpoint):
        video_grid.controls.clear()
        page.update()
        
        try:
            url = f"https://wibuapi.xyz{endpoint}/latest" 
            res = requests.get(url).json()
            
            for item in res.get("data", []):
                video_grid.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Image(src=item.get("thumbnail"), fit=ft.ImageFit.COVER, height=120, border_radius=8),
                                ft.Text(item.get("title"), max_lines=2, weight=ft.FontWeight.BOLD, size=11),
                                ft.Text(f"Eps: {item.get('episode', '?')}", size=10, color="gray"),
                            ]), padding=6
                        )
                    )
                )
        except:
            video_grid.controls.append(ft.Text("Gagal memuat data. Periksa jaringan.", color="red"))
        page.update()

    source_selector = ft.Row([
        ft.ElevatedButton("Anime", on_click=lambda _: load_content("samehadaku")),
        ft.ElevatedButton("Donghua", on_click=lambda _: load_content("anichin")),
        ft.ElevatedButton("Drakor", on_click=lambda _: load_content("wibusubs")),
    ], alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        ft.Text("MultiStream App v3", size=20, weight=ft.FontWeight.BOLD),
        source_selector,
        ft.Divider(),
        video_grid
    )
    load_content("samehadaku")

ft.app(target=main)
  
