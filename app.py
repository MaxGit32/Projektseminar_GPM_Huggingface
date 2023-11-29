import gradio as gr

# Funktion definieren, die Input in Output transformiert
def pap(message, history):
    return message + " Ich bin ein Papageien-Chatbot"

iface = gr.ChatInterface(pap)
iface.launch()

