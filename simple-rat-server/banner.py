
from pystyle import *
import random

def show_banner():
    dark = Col.dark_gray
    light = Col.light_gray
    purple = Colors.StaticMIX((Col.purple, Col.blue))
    bpurple = Colors.StaticMIX((Col.purple, Col.blue, Col.blue))

    banners_list = [
        rf'''

 ▄█    █▄     ▄████████ ███▄▄▄▄    ▄██████▄    ▄▄▄▄███▄▄▄▄   
███    ███   ███    ███ ███▀▀▀██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄ 
███    ███   ███    █▀  ███   ███ ███    ███ ███   ███   ███ 
███    ███  ▄███▄▄▄     ███   ███ ███    ███ ███   ███   ███ 
███    ███ ▀▀███▀▀▀     ███   ███ ███    ███ ███   ███   ███ 
███    ███   ███    █▄  ███   ███ ███    ███ ███   ███   ███ 
███    ███   ███    ███ ███   ███ ███    ███ ███   ███   ███ 
 ▀██████▀    ██████████  ▀█   █▀   ▀██████▀   ▀█   ███   █▀  

 ┎
  ○ Disable Anti Virus ,   ○ Download files ,   ○ Cmd Command
                                                             ┛
                                                             

    ''',
    rf'''


                                                                   
                                         :                         
                   ,;L.                 t#,                        
                 f#i EW:        ,ft    ;##W.                       
               .E#t  E##;       t#E   :#L:WE             ..       :
  t      .DD. i#W,   E###t      t#E  .KG  ,#D           ,W,     .Et
  EK:   ,WK. L#D.    E#fE#f     t#E  EE    ;#f         t##,    ,W#t
  E#t  i#D :K#Wfff;  E#t D#G    t#E f#.     t#i       L###,   j###t
  E#t j#f  i##WLLLLt E#t  f#E.  t#E :#G     GK      .E#j##,  G#fE#t
  E#tL#i    .E#L     E#t   t#K: t#E  ;#L   LW.     ;WW; ##,:K#i E#t
  E#WW,       f#E:   E#t    ;#W,t#E   t#f f#:     j#E.  ##f#W,  E#t
  E#K:         ,WW;  E#t     :K#D#E    f#D#;    .D#L    ###K:   E#t
  ED.           .D#; E#t      .E##E     G#t    :K#t     ##D.    E#t
  t               tt ..         G#E      t     ...      #G      .. 
                                 fE                     j          
                                  ,                                
     ┎
      ○ Disable Anti Virus ,   ○ Download files ,   ○ Cmd Command
                                                                 ┛
''']
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(random.choice(banners_list))))
    

def showbanner_raw():
    dark = Col.dark_gray
    light = Col.light_gray
    purple = Colors.StaticMIX((Col.purple, Col.blue))
    bpurple = Colors.StaticMIX((Col.purple, Col.blue, Col.blue))

    banners_list = [
        rf'''

 ▄█    █▄     ▄████████ ███▄▄▄▄    ▄██████▄    ▄▄▄▄███▄▄▄▄   
███    ███   ███    ███ ███▀▀▀██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄ 
███    ███   ███    █▀  ███   ███ ███    ███ ███   ███   ███ 
███    ███  ▄███▄▄▄     ███   ███ ███    ███ ███   ███   ███ 
███    ███ ▀▀███▀▀▀     ███   ███ ███    ███ ███   ███   ███ 
███    ███   ███    █▄  ███   ███ ███    ███ ███   ███   ███ 
███    ███   ███    ███ ███   ███ ███    ███ ███   ███   ███ 
 ▀██████▀    ██████████  ▀█   █▀   ▀██████▀   ▀█   ███   █▀  


                                                             

    ''',
    rf'''


                                                                   
                                         :                         
                   ,;L.                 t#,                        
                 f#i EW:        ,ft    ;##W.                       
               .E#t  E##;       t#E   :#L:WE             ..       :
  t      .DD. i#W,   E###t      t#E  .KG  ,#D           ,W,     .Et
  EK:   ,WK. L#D.    E#fE#f     t#E  EE    ;#f         t##,    ,W#t
  E#t  i#D :K#Wfff;  E#t D#G    t#E f#.     t#i       L###,   j###t
  E#t j#f  i##WLLLLt E#t  f#E.  t#E :#G     GK      .E#j##,  G#fE#t
  E#tL#i    .E#L     E#t   t#K: t#E  ;#L   LW.     ;WW; ##,:K#i E#t
  E#WW,       f#E:   E#t    ;#W,t#E   t#f f#:     j#E.  ##f#W,  E#t
  E#K:         ,WW;  E#t     :K#D#E    f#D#;    .D#L    ###K:   E#t
  ED.           .D#; E#t      .E##E     G#t    :K#t     ##D.    E#t
  t               tt ..         G#E      t     ...      #G      .. 
                                 fE                     j          
                                  ,                                

''']
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(random.choice(banners_list))))


