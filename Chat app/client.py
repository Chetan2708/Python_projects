from socket import *
from threading import *
from tkinter import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

try:
    clientSocket.connect((hostIp, portNumber))
except Exception as e:
    print(f"Error connecting to server: {e}")

window = Tk()
window.title("Chat App")
window.geometry("400x500")

# Styling for the text messages display
txtMessages = Text(window, width=50, height=20, wrap=WORD, bg="#f0f0f0", font=("Helvetica", 12))
txtMessages.grid(row=0, column=0, padx=10, pady=10)

# Styling for the input box
txtYourMessage = Entry(window, width=50, font=("Helvetica", 12))
txtYourMessage.insert(0, "Type here...")
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

def onEntryClick(event):
    if txtYourMessage.get() == "Type here...":
        txtYourMessage.delete(0, END)
        txtYourMessage.config(fg='black')

txtYourMessage.bind('<FocusIn>', onEntryClick)

def sendMessage(event=None):
    clientMessage = txtYourMessage.get()
    if clientMessage:  # Only send a non-empty message
        txtMessages.insert(END, "\n" + "You: " + clientMessage)
        clientSocket.send(clientMessage.encode("utf-8"))
        txtYourMessage.delete(0, END)  # Clear the input box after sending the message

# Bind the <Return> key to the sendMessage function
txtYourMessage.bind('<Return>', sendMessage)

# Styling for the send button
btnSendMessage = Button(window, text="Send", width=20, command=sendMessage, bg="#4CAF50", fg="white", font=("Helvetica", 12))
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

def recvMessage():
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        txtMessages.insert(END, "\n" + serverMessage)

recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()
window.mainloop()
