from tkinter import *
from tkinter import messagebox
import random

# Nastavení hlavního okna hry.
okno = Tk()
okno.resizable(False, False)
okno.title("Piškvorky")
okno.iconbitmap("ikona.ico")

# Classa hry.
class Piskvorky:
      def __init__(self): # construktor

            # Skupina hráčů, výběr náhodně začínajícího a herní tabulka.
            self.skup_hracu = ["X", "O"]
            self.hrac = random.choice(self.skup_hracu)
            self.tabulka = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            
            # Informace o průběhu hry.
            self.popis = Label(text="Hraje: " + self.hrac, font=("Comic Sans MS", 25))
            self.popis.pack(side="top")

            ramecek = Frame(okno)
            ramecek.pack()

            # Tvorba herní tabulky / tlačítek.
            for r in range(3):
                  for s in range(3):                                        
                        self.tabulka[r][s] = Button(ramecek, width=3, height=1, text=" ",
                                          font=("Comic Sans MS", 35), bg="#66dbff",
                                          command=lambda radek=r, sloupec=s:
                                          self.dalsi_tah(radek, sloupec))
                        self.tabulka[r][s].grid(row=r, column=s)


      # Střídá tahy hráčů, neustále kontroluje možnosti výhry nebo remízy.
      def dalsi_tah(self, radek, sloupec):
            
            if self.tabulka[radek][sloupec]["text"] == " " and self.kontrola_vitezstvi() is False:

                  if self.hrac == self.skup_hracu[0]:
                        self.tabulka[radek][sloupec]["text"] = self.hrac

                        if self.kontrola_vitezstvi() is False:
                              self.hrac = self.skup_hracu[1]
                              self.popis.config(text="Hraje: " + self.skup_hracu[1])
                        
                        elif self.kontrola_vitezstvi() is True:                       
                              self.popis.config(text="Vyhrál/a! " + self.skup_hracu[0])

                              if messagebox.askyesno("Piškvorky", "Vyhrál/a! " + self.skup_hracu[0] +
                                                     "\nChcete hrát znovu?"):
                                    self.nova_hra()

                              else:
                                    okno.quit()                              

                        elif self.kontrola_vitezstvi() == "Remíza!":
                              self.popis.config(text="Remíza!")

                              if messagebox.askyesno("Piškvorky", "Remíza!\nChcete hrát znovu?"):                                                    
                                    self.nova_hra()

                              else:
                                    okno.quit()

                  else:
                        self.tabulka[radek][sloupec]["text"] = self.hrac

                        if self.kontrola_vitezstvi() is False:
                              self.hrac = self.skup_hracu[0]
                              self.popis.config(text="Hraje: " + self.hrac[0])
                        
                        elif self.kontrola_vitezstvi() is True:
                              self.popis.config(text="Vyhrál/a! " + self.skup_hracu[1])

                              if messagebox.askyesno("Piškvorky", "Vyhrál/a! " + self.skup_hracu[1] +                                                  
                                                     "\nChcete hrát znovu?"):
                                    self.nova_hra()

                              else:
                                    okno.quit()                             

                        elif self.kontrola_vitezstvi() == "Remíza!":
                              self.popis.config(text="Remíza!")

                              if messagebox.askyesno("Piškvorky", "Remíza!\nChcete hrát znovu?"):                                                                                 
                                    self.nova_hra()

                              else:
                                    okno.quit()
                              

      # Kontrola všech možných vítězství a zabarvení vítězné kombinace.                
      def kontrola_vitezstvi(self):
            
            # Kontrola řádků.
            for radek in range(3):
                  if self.tabulka[radek][0]["text"] == self.tabulka[radek][1]["text"] == self.tabulka[radek][2]["text"] != " ":     
                        self.tabulka[radek][0].config(bg="#63db42")
                        self.tabulka[radek][1].config(bg="#63db42")
                        self.tabulka[radek][2].config(bg="#63db42")
                        return True                      

            # Kontrola sloupců.
            for sloupec in range(3):
                  if self.tabulka[0][sloupec]["text"] == self.tabulka[1][sloupec]["text"] == self.tabulka[2][sloupec]["text"] != " ":                                       
                        self.tabulka[0][sloupec].config(bg="#63db42")
                        self.tabulka[1][sloupec].config(bg="#63db42")
                        self.tabulka[2][sloupec].config(bg="#63db42")             
                        return True
                 
            # Kontrola diagonálně.
            if self.tabulka[0][0]["text"] == self.tabulka[1][1]["text"] == self.tabulka[2][2]["text"] != " ":
                  self.tabulka[0][0].config(bg="#63db42")
                  self.tabulka[1][1].config(bg="#63db42")
                  self.tabulka[2][2].config(bg="#63db42")
                  return True
                              
            elif self.tabulka[0][2]["text"] == self.tabulka[1][1]["text"] == self.tabulka[2][0]["text"] != " ":           
                  self.tabulka[0][2].config(bg="#63db42")
                  self.tabulka[1][1].config(bg="#63db42")
                  self.tabulka[2][0].config(bg="#63db42")
                  return True
            
            # Kontrola plné tabulky / remízy.
            elif self.plna_tabulka() is False:
                  for radek in range(3):
                        for sloupec in range(3):
                              self.tabulka[radek][sloupec].config(bg="#ffff99")
                  return "Remíza!"
            
            else:
                  return False
            

      # Kontroluje počet kliknutí / zaplnění herní tabulky.
      def plna_tabulka(self):

            pocet_kliknuti = 9

            for radek in range(3):
                  for sloupec in range(3):
                        if self.tabulka[radek][sloupec]["text"] != " ":
                              pocet_kliknuti -= 1

            if pocet_kliknuti == 0:
                  return False
            
            else:
                  return True

      
      # Spustí novou hru a vymaže herní tabulku / tlačítka.
      def nova_hra(self):

            self.hrac = random.choice(self.skup_hracu)      
            self.popis.config(text="Hraje: " + self.hrac)
           
            for radek in range(3):
                  for sloupec in range(3):
                        self.tabulka[radek][sloupec].config(text=" ", bg="#66dbff")

# Spuštění hry pomocí classy.
piskvorky = Piskvorky()

# Hlavní cyklus.
okno.mainloop()

