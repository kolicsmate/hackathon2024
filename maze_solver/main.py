with open('maze_solver\input.txt', 'r') as f:
  input = f.read()

print(input)

#Szoval vagy megnezem az osszes utvonalat elagazasoknal külön vagy csak végigmegyek az egyik oldalhoz tapadva és
#biztos eljutoka vegeig ekkor kiveszem az egymast cancelelő utasításokat vagy mar akar a folyamat kozben

#tehat megyek a fal menten amig akadalyba nem ütközök azaz ha visszafordulok ellenorzom hogy ez ellentetes volt-e
#az elozo lepesemmel ha igen torlom a lépés lista utolso ket elemét, aztán megyek tovább a fal menten ha ez ugyan
#arra van emerrol juttem azaz ez a lepes es a listaban az elotte levo egymas ellentete torlom oket azaz eleg 
#mindig csak a lepeslista utolso ket elemet nezni, hogy ütik e egymast

#indexekkel ellenorzes hogy van e egy pontol balra jobbra alatt folott fal: meg kell hataroznom az eloret és 
#ahoz képest kell felírnom
#hogy kikuszoboljem a loopba kerülést csak szimplan falat teszek magam mögé