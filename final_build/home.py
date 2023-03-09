import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
import os
import torch
from building_classes import model_1, model_2

root = tk.Tk()

root.geometry("800x500")

root.title("caption_creater")


def get_name(name):
    l= len(name)
    file_name=""
    i=0
    while i<=l:
        if name[l-i-1]=='/':
            return file_name[::-1] 
        file_name+=name[l-i-1]
        i+=1
    return file_name[::-1] 



def select_file():
    
    file_path = filedialog.askopenfilename(initialdir='/', title="select a file", filetypes=(("png files", "*.png"),("jpej files", "*.jpej"), ("jpg files", "*.jpg") ))
    
    return file_path


def main_function():
    file_path = select_file()
    # print(file_path)
    # frame = tk.Frame(root, width=600, height=400)
    # frame.pack()
    # frame.place(anchor='center', relx=0.5, rely=0.5)
    # img =ImageTk.PhotoImage(Image.open(file_path))
    # label = tk.Label(frame, image = img)
    # label.pack()

    short_name = get_name(file_path)
    
    img = Image.open(file_path)
    rough_img = img
    rough_img=rough_img.save("saved_images/"+get_name(file_path))
    rough_img_2 = img
    rough_img_2= rough_img_2.save("saved_images_2/"+get_name(file_path))

    img=img.resize((250,250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel=tk.Label(root,  image=img)
    panel.image=img
    panel.pack()
    

def caluclate():
    path = os.listdir('saved_images/')[0]
    # feature_extractor= torch.load("models_1/feature_extractor.pt")

    # tokenizer = torch.load("models_1/tokenizer.pt")
    # model = torch.load("models_1/vision_encoder.pt")

    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    final_path = "saved_images/"+path
    my_model = model_1(final_path)
    
    ans = my_model.ret_caption()
    final_ans = "output of model_1 :"+ ans
    panels = tk.Label(root,text=final_ans).pack()
    os.remove(final_path)


def get_file_name():
    input= input_text.get("1.0", "end-1c")
    with open("text/first.txt", 'w') as f:
        f.write(input)
    

def read_input():
    get_file_name()
    f=  open("text/first.txt", 'r')
    text = f.readline()
    path = os.listdir("saved_images_2/")[0]
    # Secondmodel = model_2()
    actual_path ="saved_images_2/"+path
    second_model = model_2(actual_path, text)
    ans= second_model.ret_caption()
    final_ans = "output for model_2 :"+ ans
    panels = tk.Label(root,text=final_ans).pack()
    os.remove(actual_path)



buttonUpload = tk.Button(root, text="upload", command=main_function)
buttonUpload.pack(pady=10, padx=10)

buttonCal= tk.Button(root, text="create description model_!", command=caluclate).pack(padx=15, pady=15)



input_text = tk.Text(root, height=1, width=25, bg="light cyan")
input_text.pack()
buttonModel2= tk.Button(root, text="create description model_2",command=read_input)
buttonModel2.pack()

testbutton = tk.Button(root,text='test button', command=read_input ).pack()

# lbl = tk.Label(root, text="")
# lbl.pack()



root.mainloop()

