from typing import Union, Callable
from .aTk import aTk
from .aTopLevel import aTopLevel

# Objet pour gerer les touche de clavier

class keyboad_manager:
    def __init__(self,master:Union[aTk,aTopLevel]):
        self.__dict_key_fonction = {}# Shema key:fonction
        self.__w = master

    def __gest_keyboad(self, event):
        if event.keycode in self.__dict_key_fonction:
            self.__dict_key_fonction[event.keycode]()

    def add_key(self,key:int,fonction:Callable):
        if not self.__dict_key_fonction:
            self.__w.bind("<Key>",self.__gest_keyboad)

        self.__dict_key_fonction[key] = fonction
