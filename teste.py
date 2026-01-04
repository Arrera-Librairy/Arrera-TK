import customtkinter as ctk

# Set the appearance mode
ctk.set_appearance_mode("dark")


tk = ctk.CTk()

tk.title("Material 3 Expressive")
tk.geometry("400x500")
tk.configure(fg_color="#141218") # M3 Dark Surface

# 1. Large, Expressive Button (FAB style)
fab_button = ctk.CTkButton(
    tk,
    text="+",
    width=56,
    height=56,
    corner_radius=16, # M3 uses 'squircle' shapes
    fg_color="#D0BCFF",
    text_color="#381E72",
    hover_color="#E8DEF8",
    font=("Roboto", 24, "bold")
)
fab_button.pack(pady=20, padx=20, side="bottom", anchor="e")

# 2. Elevated Card
card = ctk.CTkFrame(
    tk,
    corner_radius=28, # Very rounded for 'Expressive' style
    fg_color="#49454F"
)
card.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(
    card,
    text="Material 3 Card",
    font=("Roboto", 20)
)
label.pack(pady=20)
tk.mainloop()

