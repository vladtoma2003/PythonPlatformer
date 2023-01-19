Constantinescu Andrei-Alexandru 324CD
Iliescu Vlad-Toma 324CD
Stoian Georgiana-Amalia 324CD


Aplicatia implementata este un joc de tip platformer. Acest joc are un singur nivel creat cu ajutorul aplicatiei Tiled. 
Obiectivul acestui nivel este de a ajunge la final si a atinge cadoul.

In directorul code este codul efectiv al programului:
- in background.py se randeaza backgroundul jocului
- in enemy.py este facuta animatia inamicului
- in game_data.py se afla un vector ce contine locatiile fisierelor .csv, folosite pentru nivel
- in level.py este facuta interactiunea playerului atat cu mediul cat si cu inamicii
- in main.py se ruleaza jocul. Aici se afla loop-ul principal
- in particles.py sunt facute particulele cand aterizeaza pe pamant
- in player.py sunt facute animatiile player-ului (alergat, sarit), actiunile sale si se calculeaza pozitia sa
- in screen.py se afla setarile ecranului
- support.py este un fisier care ajuta cu gasitul fisierelor grafice
- in tiles.py este facut: pamantul, punctele (gogosile si pizza) si decoratiunile
- in ui.py se afiseaza pe ecran nr de puncte/bani, viata si obiectivul

In directorul graphics se afla poze necesare pentru generarea nivelului.

In directorul levels se afla fisierele .CSV cu ajutorul carora se genereaza nivelul.

Am folosit biblioteca .pygame pentru crearea jocului si aplicatia Tiled pentru crearea nivelului.

Jocul merge rulat doar pe Linux cu interfata grafica(din Makefile). Pentru a rula jocul trebuie executate urmatoarele comenzi:
- make build
- make run
exista si make clean pentru a sterge virtual environmentul creat. 

Fiecare membru al echipei a avut o contributie egala in ceea ce priveste implementarea proiectului.
Realizarea desginului caracterelor si creearea propriu-zisa a nivelului (cu ajutor aplicatiei Tiled) au fost realizate de catre
Iliescu Vlad-Toma. Pentru a avea un desgin care sa placa tuturor membrilor echipei, am ales impreuna imaginile folosite
in crearea nivelului.

Pe partea de implementare, codul a fost realizat in modul urmator:
- setup-ul ferestrei(Stoian Georgiana-Amalia)
- cum se misca jucatorul(actiuni si animatii(miscarea: sarit, mers inainte-inapoi))(Stoian Georgiana-Amalia + Iliescu Vlad-Toma + Constantinescu Andrei-Alexandru)
- cum se misca inamicul(Stoian Georgiana-Amalia)
- modurile in care se poate incheia jocul(gameover/you won/you won + congrats) (Constantinescu Andrei-Alexandru)
- stats-urile(numar de monede & bara de viata) + schimbarea nivelului vietii cand interactioneaza cu inamicul 
si incrementarea numarului de monede cand culege pizza si gogoase(pizza = gogoasa = 1 moneda)(Constantinescu Andrei-Alexandru)
- crearea nivelului(imbinarea hartii create de Vlad cu codul proiectului) si importarea imaginilor in nivel (Stoian Georgiana-Amalia)
- in fisierul level.py sunt imbinate majoritatea actiunilor din cadrul jocului(miscarea player-ului, inamicilor, interactiunile dintre inamic si player, verificarea
castigarii/pierderii jocului, coliziunile dintre player si obiectele de colectat, miscarea hartii jocului etc) (Stoian Georgiana-Amalia + Iliescu Vlad-Toma + Constantinescu Andrei-Alexandru)

Dificultati intampinate:
- gasirea unui mod in care player-ul sa se poata misca pe toata harta nivelului, desi doar o parte din aceasta harta putea aparea in fereastra dedicata jocului.
Rezolvarea a fost prin determinarea miscarii hartii, in directia opusa de deplasarea a player-ului(astfel inducandu-se iluzia ca se misca de fapt player-ul) in 
momentul in care player-ul a ajuns la o anumita coordonata x a ferestrei
- invatarea utilizarii aplicatie Tiled
