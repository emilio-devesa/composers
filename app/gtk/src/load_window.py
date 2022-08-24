# -*- coding: utf-8 -*-

# Emilio Devesa
# https://emiliodevesa.wordpress.com/

import gi, requests, threading, shutil
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib, GdkPixbuf
from window import MainWindow

class LoadWindow(Gtk.Window):
    label=Gtk.Label("Cargando elementos...")
    spinner=Gtk.Spinner()
    box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

    def __init__(self):
        super().__init__(title="")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(60)
        self.set_resizable(False)
        self.set_default_size(120,100)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.spinner.props.active=True

        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)
        self.launch_load()

    def launch_load(self):
        thread=threading.Thread(target=self.load_json, args=())
        thread.start()
    
    def load_json(self):
        response=requests.get("https://raw.githubusercontent.com/emilio-devesa/composers/resources/res/catalog.json")
        json_list=response.json() #Asumimos que la petición se completó con éxito, o fallará si no lo ha hecho
        result=[]
        for json_item in json_list:
            name=json_item.get("name")
            description=json_item.get("description")
            image_url=json_item.get("image_url")
            biography=json.item.get("biography")
            r=requests.get(image_url,stream=True)
            with open("temp.png","wb") as f:
                shutil.copyfileobj(r.raw,f)
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(".temp.png", 200, 200, False)
            result.append({"name":name,"description":description,"gtk_image":pixbuf,"biography":biography})
            GLib.idle_add(self.start_main_window,result)
    
    def start_main_window(self,loaded_items_list):
        win=MainWindow(loaded_items_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()
