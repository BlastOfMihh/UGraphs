from sys import stdout
from Graph import *


class Menu:
    class MenuEntry:
        def __init__(self, ui, text, function):
            self.text=text
            self.function=function
            self._ui=ui
        def execute(self):
            self.function(self._ui)

    def __init__(self) -> None:
        self._menu_entries={}

    def add_entry(self, ui, text, function):
        self._menu_entries[str(len(self._menu_entries))]=self.MenuEntry(ui, text, function)

    def print_menu(self)->None:
        for i in self._menu_entries:
            entry=self._menu_entries[i]
            print(f"\t{i}){entry.text}")
    
    def _execute_menu_entry(self, entry):
        try:
            self._menu_entries[entry].execute()
        except GraphError as e:
            print("\n\tERROR ",str(e))
        except Exception as e:
            print("INVALID COMMAND ", str(e))

    def _read_menu_entry(self):
        return input("Chose a menu entry > ")

    def start(self):
        print("You can choose one of the following:")
        while True:
            self.print_menu()
            menu_entry=self._read_menu_entry()
            self._execute_menu_entry(menu_entry)
            if menu_entry=="0":
                break


