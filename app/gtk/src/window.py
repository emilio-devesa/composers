# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GdkPixbuf
from cell import Cell
from about_window import AboutWindow

class MainWindow(Gtk.Window):
    flowbox=Gtk.FlowBox()

    def __init__(self,data_source):
        super().__init__(title="Catálogo")
        self.connect("destroy",Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(640,480)
        self.set_position(Gtk.WindowPosition.CENTER)

        header=Gtk.HeaderBar(title="Compositores")
        header.set_subtitle("Grandes compositores europeos de los siglos XV a XX")
        header.props.show_close_button=True
        self.set_titlebar(header)
        scrolled=Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)

        # Creamos la barra de menus, el titulo del menu, el submenu y los elementos hijos
        menu_bar=Gtk.MenuBar()
        menu_help=Gtk.MenuItem("Ayuda")
        menu_help_submenu=Gtk.Menu()
        menu_help_about=Gtk.MenuItem("Acerca De")
        
        # Conectamos entre sí de forma jerárquica los elementos anteriores
        menu_bar.append(menu_help)
        menu_help.set_submenu(menu_help_submenu)
        menu_help_submenu.append(menu_help_about)
        
        # Conectamos las opciones del menu con sus correspondientes funciones
        menu_help_about.connect("activate", self.on_help_about)
        
        # Creamos una caja vertical y añadimos primero el menu y despues la ScrolledWindow que ya teníamos
        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(menu_bar, False, False, 0)
        vbox.pack_start(scrolled, True, True, 0)
        # Y la vBox a la ventana
        self.add(vbox)

        # Para cada elemento del catálogo, construimos su celda y la añadimos al Flowbox
        for item in data_source:
            cell=Cell(item.get("name"),item.get("gtk_image"),item.get("description"),item.get("biography"))
            self.flowbox.add(cell)

    
    def on_help_about(self, widget):
        print("Se ha pulsado la opcion 'Acerca De' del menu 'Ayuda'")
        about_window=AboutWindow()
        about_window.show_all()
        