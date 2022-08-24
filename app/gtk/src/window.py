# -*- coding: utf-8 -*-

# Emilio Devesa
# https://emiliodevesa.wordpress.com/

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GdkPixbuf

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
        self.add(scrolled)

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

    
    def on_help_about(self, widget):
        print("Se ha pulsado la opcion 'Acerca De' del menu 'Ayuda'")