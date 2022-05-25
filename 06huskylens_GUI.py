# -*- coding: utf-8 -*-

import tkinter as tk
import time
import json
from huskylib import HuskyLensLibrary
from tkinter import ttk
from tkinter.filedialog import askopenfile


algorthimsByteID = {
    "ALGORITHM_OBJECT_TRACKING": "0100",
    "ALGORITHM_FACE_RECOGNITION": "0000",
    "ALGORITHM_OBJECT_RECOGNITION": "0200",
    "ALGORITHM_LINE_TRACKING": "0300",
    "ALGORITHM_COLOR_RECOGNITION": "0400",
    "ALGORITHM_TAG_RECOGNITION": "0500",
    "ALGORITHM_OBJECT_CLASSIFICATION": "0600",
    "ALGORITHM_QR_CODE_RECOGNITION": "0700",
    "ALGORITHM_BARCODE_RECOGNITION": "0800",
}

def parsed_data(obj):
    count=1
    parsed_data = ''
    if(type(obj)==list):
        for i in obj:
            parsed_data += "\t "+ ("BLOCK_" if i.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(i.__dict__)
            count+=1
    else:
        parsed_data += "\t "+ ("BLOCK_" if i.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(i.__dict__)
    return parsed_data


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x280')
        self.title('huskylens GUI')
        self.update_period = 2000
        self.hl = HuskyLensLibrary("SERIAL", "/dev/serial0",9600)
        time.sleep(1)
        #self.hl = HuskyLensLibrary("SERIAL", "/dev/ttyUSB1", 3000000)

        self.canvas = tk.Canvas(self, width=500, height=250, background='black')
        self.canvas.grid(row=0, column=0, rowspan=9)
        self.text = self.canvas.create_text((100, 50), text="Hello", fill='white')

        self.face_recognition_button = tk.Button(self, text="人脸识别",
                                                 command=lambda: self.switch_algorithm('ALGORITHM_FACE_RECOGNITION'))
        self.face_recognition_button.grid(column=1, row=0, sticky='w')

        self.color_recognition_button = tk.Button(self, text="颜色识别",
                                                 command=lambda: self.switch_algorithm('ALGORITHM_COLOR_RECOGNITION'))
        self.color_recognition_button.grid(column=1, row=1, sticky='w')

        self.object_tracking_button = tk.Button(self, text="物体追踪",
                                                 command=lambda: self.switch_algorithm('ALGORITHM_OBJECT_TRACKING'))
        self.object_tracking_button.grid(column=1, row=2, sticky='w')

        self.QRcode_recognition_button = tk.Button(self, text="QR二维码识别",
                                                 command=lambda: self.switch_algorithm('ALGORITHM_QR_CODE_RECOGNITION'))
        self.QRcode_recognition_button.grid(column=1, row=3, sticky='w')

        self.after(2000, self.request_data)


    def request_data(self):
        # 实时更新数据
        data = self.hl.requestAll()
        self.canvas.itemconfig(self.text, text=parsed_data(data))
        self.after(self.update_period, self.request_data)


    def switch_algorithm(self, algorithm):
        self.hl.algorthim(algorithm)
        print("switch_algorithm:{}".format(algorithm))

    def search_history(self):
        print("show history")

app = Application()
app.mainloop()
