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