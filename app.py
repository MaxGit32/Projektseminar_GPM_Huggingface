import gradio as gr
import os 

os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()

