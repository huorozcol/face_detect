import cv2
import tkinter as tk
from tkinter import messagebox
from threading import Thread
from config import create_direct, faces_folder
import os
from PIL import Image, ImageTk
from Screen import ShowFrame

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconcimiento facial - Sede Principal - Medellín - Cámara IP RTSP - ")
        self.fr = tk.Frame(self.root, width=900, height=200, borderwidth=2, relief="groove")
        self.fr.place(x=10, y=10)
        self.count_fr = 1

        # Entrada para la IP de la cámara
        self.ip_label = tk.Label(self.fr, text="Ingrese la IP de la cámara:")
        self.ip_label.place(x=10, y=20)

        self.ip_entry = tk.Entry(self.fr, width=60)
        self.ip_entry.insert(0,"rtsp://admin:admin@192.168.1.201:1935")
        self.ip_entry.place(x=10, y=40)

        # Botón para conectar
        self.connect_button = tk.Button(self.fr, text="Conectar", command=self.connect_camera)
        self.connect_button.place(x=10, y=70)

        self.disconn_button = tk.Button(self.fr, text="Desconectar", command=self.disconn_camera)
        self.disconn_button.config(state='disabled')
        self.disconn_button.place(x=100, y=70)

        self.label_quality_vid = tk.Label(self.fr, text="Calidad de video")
        self.label_quality_vid.place(x=10,y=128)

        self.qualit_vid = tk.Scale(self.fr, from_=1, to=20, orient="horizontal")
        self.qualit_vid.set(10)
        self.qualit_vid.place(x=140,y=110)

        self.fr_video = tk.Frame(self.root, width=900, height=480, borderwidth=2, relief="groove")
        self.fr_video.place(x=10, y=250)

        # Label para mostrar el video
        self.video_label = tk.Label(self.fr_video)
        self.video_label.pack()

        # Label para mostrar las ultimas fotos
        self.faces_frame = tk.Frame(self.root,width=900, height=722, borderwidth=2, relief="groove")
        self.faces_frame.place(x=950, y=10)

        self.vid = None
        self.is_running = False

    def disconn_camera(self):
        self.vid = None
        self.is_running = False
        self.connect_button.config(state="active")
        self.disconn_button.config(state='disabled')
        self.ip_entry.config(state="normal")

    def connect_camera(self):
        ip = self.ip_entry.get()
        rtsp_url = f"{ip}"  # Modifica según sea necesario

        self.vid = cv2.VideoCapture(rtsp_url)

        if not self.vid.isOpened():
            messagebox.showerror("Error", "No se pudo conectar a la cámara.")
            return

        self.is_running = True
        self.connect_button.config(state="disabled")
        self.disconn_button.config(state='active')
        self.ip_entry.config(state='disabled')
        self.update_video()

    def update_video(self):
        if self.is_running:
            ret, frame = self.vid.read()
            if ret:
                self.count_fr += 1
                #print(self.qualit_vid.get())
                if self.count_fr % self.qualit_vid.get() == 0:
                    # print(self.count_fr)
                    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    #self.show_frame_thr = Thread(name='showActFrame' ,target=ShowFrame, args=(frame,), daemon=True)
                    #print(self.show_frame_thr.is_alive())
                    ShowFrame.showScreen(None, frame)
                    # if not self.show_frame_thr.is_alive():
                    #     self.show_frame_thr.start()

                    #faces(frame)
                    # img = cv2.resize(frame, (900, 480))
                    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    # img = cv2.imencode('.png', img)[1].tobytes()#
                    # self.photo = tk.PhotoImage(data=img)
                    # self.video_label.configure(image=self.photo)
            #self.show_frame_thr.join()
            self.video_label.after(30, self.update_video)
            #self.show_last_faces()



    def close_camera(self):
        self.is_running = False
        if self.vid is not None:
            self.vid.release()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.geometry("1600x900")
    root.protocol("WM_DELETE_WINDOW", app.close_camera)
    create_direct()
    root.mainloop()