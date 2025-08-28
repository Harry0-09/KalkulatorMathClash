import tkinter as tk

# Funkcja do obliczeń podstawowych i zaawansowanych
def oblicz():
    # Dopasowanie rozmiaru okna przy obliczeniach
    okno.geometry("350x130")
    try:
        liczba1 = float(wpis_liczba1.get())
        liczba2 = float(wpis_liczba2.get())
        operator = zmienna_operator.get()

        if operator == "+":
            wynik = liczba1 + liczba2
        elif operator == "-":
            wynik = liczba1 - liczba2
        elif operator == "*":
            wynik = liczba1 * liczba2
        elif operator == "/":
            if liczba2 == 0:
                wynik = "Nie można dzielić przez 0"
            else:
                wynik = liczba1 / liczba2
        elif operator == "DoPotegi":
            wynik = liczba1 ** liczba2
        elif operator == "√":
            wynik = liczba2 ** (1/liczba1)
        else:
            wynik = "Nieznany operator"

        etykieta_wynik.config(text=f"Wynik: {wynik}")

    except ValueError:
        etykieta_wynik.config(text="Błędne dane")

# Funkcja do zamiany ułamków na liczby dziesiętne
def zamien_na_dziesietne():
    try:
        licznik_str = wpis_licznik.get()
        mianownik_str = wpis_mianownik.get()

        licznik = float(licznik_str)
        mianownik = float(mianownik_str)

        if mianownik == 0:
            return etykieta_wynik_dziesietny.config(text="Dzielenie przez 0")

        wynik_dziesietny = licznik / mianownik
        etykieta_wynik_dziesietny.config(text=f"{wynik_dziesietny}")

    except ValueError:
        etykieta_wynik_dziesietny.config(text="Błędne dane")

# Funkcja do zaokrąglania wyniku do 3 miejsc po przecinku
def zaokraglij_wynik():
    try:
        wynik = float(etykieta_wynik.cget("text").replace("Wynik: ", ""))
        etykieta_wynik.config(text=f"Wynik: {round(wynik, 3)}")
        
        ulamek = float(etykieta_wynik_dziesietny.cget("text"))
        etykieta_wynik_dziesietny.config(text=f"{round(ulamek, 3)}")
    except Exception:
        try:
            ulamek = float(etykieta_wynik_dziesietny.cget("text"))
            etykieta_wynik_dziesietny.config(text=f"{round(ulamek, 3)}")
        except:
            pass
# Tworzenie głównego okna aplikacji
okno = tk.Tk()
okno.title("Kalkulator Math Clash^2")
okno.geometry("400x130")

# Pola do wprowadzania liczb
wpis_liczba1 = tk.Entry(okno, width=10)
wpis_liczba1.grid(row=0, column=0)

zmienna_operator = tk.StringVar()
opcje_operatora = ["+", "-", "*", "/", "DoPotegi", "√"]
zmienna_operator.set("Wybierz działanie")

menu_operatora = tk.OptionMenu(okno, zmienna_operator, *opcje_operatora)
menu_operatora.grid(row=0, column=1)

wpis_liczba2 = tk.Entry(okno, width=10)
wpis_liczba2.grid(row=0, column=2)

# Przycisk obliczania
przycisk_oblicz = tk.Button(okno, text="Oblicz", command=oblicz)
przycisk_oblicz.grid(row=0, column=3)

# Etykieta do wyświetlania wyniku
etykieta_wynik = tk.Label(okno, text="Wynik: ")
etykieta_wynik.grid(row=1, column=0, columnspan=4)

# --- Zamiana ułamków ---
wpis_licznik = tk.Entry(okno, width=7)
wpis_licznik.grid(row=2, column=0)

etykieta_znak = tk.Label(okno, text="=")
etykieta_znak.grid(row=3, column=0, columnspan=3)

wpis_mianownik = tk.Entry(okno, width=7)
wpis_mianownik.grid(row=3, column=0)

przycisk_zamien = tk.Button(okno, text="Przelicz ułamek", command=zamien_na_dziesietne)
przycisk_zamien.grid(row=2, column=2, columnspan=5)

etykieta_wynik_dziesietny = tk.Label(okno, text="UD*")
etykieta_wynik_dziesietny.grid(row=3, column=0, columnspan=4)

etykieta_oznaczenie = tk.Label(okno, text="UD = Ułamek Dziesiętny")
etykieta_oznaczenie.grid(row=4, column=0)

# Przycisk zaokrąglania
przycisk_zaokraglij = tk.Button(okno, text="Zaokrąglij", command=zaokraglij_wynik)
przycisk_zaokraglij.grid(row=4, column=3)

# Uruchomienie pętli głównej GUI
okno.mainloop()
