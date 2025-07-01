import os
import tempfile
from tkinter import Tk, Label, filedialog, Button, Radiobutton, IntVar, Frame, Entry, StringVar
from PIL import Image, ImageTk

# config
window = Tk()
window.title('Simple mass ffmpeg')
window.geometry("700x750")
window.resizable(False, False)
for i in range(3):
    window.grid_columnconfigure(i, weight=1)

path_input = ""
path_output = ""
rotation_angle = IntVar()
rotation_angle.set(0)
side = IntVar()
side.set(0)
inputVar = StringVar()
outputVar = StringVar()
pil_image = Image.open("assets/img_preview.jpg")

def update_preview():
    global pil_image, image, image_label
    img = pil_image.copy()
    angle = rotation_angle.get()
    if angle:
        img = img.rotate(-angle, expand=True)
    if side.get() == 1:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif side.get() == 2:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
    image = ImageTk.PhotoImage(img)
    image_label.configure(image=image)
    image_label.image = image

def browseFiles1():
    global path_input
    folder = filedialog.askdirectory()
    button_input.configure(text="Selected folder: " + folder)
    path_input = folder

def browseFiles2():
    global path_output
    folder = filedialog.askdirectory()
    button_output.configure(text="Selected folder: " + folder)
    path_output = folder

def generate_command():
    in_format = inputVar.get()
    out_format = outputVar.get()
    angle = rotation_angle.get()
    flip = side.get()

    vf_filters = []
    if angle == 90:
        vf_filters.append("transpose=1")
    elif angle == 180:
        vf_filters.append("transpose=1,transpose=1")
    elif angle == 270:
        vf_filters.append("transpose=2")
    if flip == 1:
        vf_filters.append("hflip")
    elif flip == 2:
        vf_filters.append("vflip")

    vf_string = ",".join(vf_filters)

    input_path_escaped = path_input.replace("/", "\\")
    output_path_escaped = path_output.replace("/", "\\")

    out_name = "%%~nf_converted." + out_format
    cmd = f'for %%f in ("{input_path_escaped}\\*.{in_format}") do ffmpeg -i "%%f"'
    if vf_filters:
        cmd += f' -vf "{vf_string}"'
    cmd += f' "{output_path_escaped}\\{out_name}"'

    return cmd

def execute_command():
    cmd = generate_command()
    print("Executing command:", cmd)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bat", mode="w", encoding="utf-8") as bat_file:
        bat_file.write(cmd + "\n")
        bat_file_path = bat_file.name
    os.system(f'start cmd /k "{bat_file_path}"')

def install_ffmpeg():
    os.system("start cmd /k winget install ffmpeg")

# structure
header = Label(window, text="Simple mass ffmpeg", font="Helvetica 20 bold", fg="black")
install_button = Button(window, text="Install ffmpeg (winget)", command=install_ffmpeg)
label_1 = Label(window, text="1. Select folder with videos to convert", width=100, height=2, fg="black")
button_input = Button(window, text="Select folder", command=browseFiles1)
label_2 = Label(window, text="2. Select folder where files will be saved", width=100, height=2, fg="black")
button_output = Button(window, text="Select folder", command=browseFiles2)
label_3 = Label(window, text="3. Select actions to do with your videos", width=100, height=2, fg="black")

rotation_frame = Frame(window)
radio_text = Label(rotation_frame, text="Rotate video:")
radio_0 = Radiobutton(rotation_frame, text="0°", variable=rotation_angle, value=0, command=update_preview)
radio_90 = Radiobutton(rotation_frame, text="90°", variable=rotation_angle, value=90, command=update_preview)
radio_180 = Radiobutton(rotation_frame, text="180°", variable=rotation_angle, value=180, command=update_preview)
radio_270 = Radiobutton(rotation_frame, text="270°", variable=rotation_angle, value=270, command=update_preview)
radio_text.pack(side="left")
radio_0.pack(side="left", padx=5)
radio_90.pack(side="left", padx=5)
radio_180.pack(side="left", padx=5)
radio_270.pack(side="left", padx=5)

side_frame = Frame(window)
radio2_text = Label(side_frame, text="Flip video:")
radio_horizontal = Radiobutton(side_frame, text="horizontally", variable=side, value=1, command=update_preview)
radio_vertical = Radiobutton(side_frame, text="vertically", variable=side, value=2, command=update_preview)
radio_none = Radiobutton(side_frame, text="none", variable=side, value=0, command=update_preview)
radio2_text.pack(side="left")
radio_horizontal.pack(side="left", padx=5)
radio_vertical.pack(side="left", padx=5)
radio_none.pack(side="left", padx=5)

format_frame1 = Frame(window)
input_format_label = Label(format_frame1, text="Input files format extension (ex. mp4, avi):")
input_format = Entry(format_frame1, width=5, textvariable=inputVar)
input_format_label.pack(side="left", padx=5)
input_format.pack(side="left", padx=5)

format_frame2 = Frame(window)
output_format_label = Label(format_frame2, text="Output files format extension (ex. mp4, avi):")
output_format = Entry(format_frame2, width=5, textvariable=outputVar)
output_format_label.pack(side="left", padx=5)
output_format.pack(side="left", padx=5)

label_4 = Label(window, text="Preview what will happen with your videos based on image below")
image = ImageTk.PhotoImage(pil_image)
image_label = Label(window, image=image)
image_label.image = image

guzik_exec = Button(window, text="Execute in terminal", command=execute_command)

header.grid(column=1, row=1)
install_button.grid(column=1, row=2)
label_1.grid(column=1, row=3)
button_input.grid(column=1, row=4)
label_2.grid(column=1, row=5)
button_output.grid(column=1, row=6)
label_3.grid(column=1, row=7)
rotation_frame.grid(column=1, row=8)
side_frame.grid(column=1, row=9)
format_frame1.grid(column=1, row=10)
format_frame2.grid(column=1, row=11)
label_4.grid(column=1, row=12)
image_label.grid(column=1, row=13)
guzik_exec.grid(column=1, row=15)

window.mainloop()
