import Tkinter
from ScrolledText import *

class App:
    def __init__(self):
       self.master = Tkinter.Tk()
       self.master.title("PORT NUMBER")

       self.iptext= Tkinter.Label(self.master, text="IP Address:")
       self.iptext.grid(row=1,column=0)

       self.ip = Tkinter.StringVar()
       self.ipAdd = Tkinter.Entry(self.master, textvariable=self.ip)
       self.ipAdd.grid(row=1, column=1)
       
       self.portno = Tkinter.Label(self.master, text="Port:")
       self.portno.grid(row=2,column=0)

       self.port = Tkinter.StringVar()
       self.myentry = Tkinter.Entry(self.master, textvariable=self.port)
       self.myentry.grid(row=2, column=1)

       self.clientext = Tkinter.Label(self.master, text="Cient Name:")
       self.clientext.grid(row=3,column=0)

       self.client = Tkinter.StringVar()
       self.clientname = Tkinter.Entry(self.master, textvariable=self.client)
       self.clientname.grid(row=3, column=1)

       self.mybutton = Tkinter.Button(self.master, text="Connect", command=self.printMessage)
       self.mybutton.grid(row=4, column=1)

       self.textPad = ScrolledText(self.master, wrap=Tkinter.WORD, width=40, height=25)
       self.textPad.grid(row=5, column=1)

       self.quitbutton = Tkinter.Button(self.master, text="Leave Conversation", command=self.master.destroy)
       self.quitbutton.grid(row=6, column=1)


       self.textinput = Tkinter.Text(master=self.master, wrap=Tkinter.WORD, width=40, height=4)
       self.textinput.grid(row=7, column=1)

       #self.ui_messages.insert(Tkinter.END, "Adding a message to the text field...\n")
       #self.textinput.insert(Tkinter.END, "<Enter message>")
       
       # Bind the button-1 click of the Entry to the handler
       #self.textinput.bind('<Button-1>', self.eventInputClick)
       
       self.sendbutton = Tkinter.Button(self.master, text="Send Message", command=self.sendMsg)
       self.sendbutton.grid(row=8, column=1)
       #self.sendbutton.pack(padx=5, pady=10, side="LEFT")
       

       self.counter = 0
       self.master.mainloop()

    def printMessage(self):
       print self.ip.get()
       print self.port.get()
       print self.client.get()
       
       self.counter = self.counter+1;

       if self.counter>=1:
          self.mybutton.config(state='disabled')

    # SEND button pressed
    def sendMsg(self):
        print "Send Message"
        #print self.textinput.get()
        # Get user input (minus newline character at end)
        msg = self.textinput.get("0.0", Tkinter.END+"-1c")

        print msg
        print("UI: Got text: '%s'" % msg)

        # Add this data to the message window
        self.textPad.insert(Tkinter.INSERT, "%s\n" % (msg))
        self.textPad.yview(Tkinter.END)  # Auto-scrolling
        
        # Clean out input field for new data
        self.textinput.delete("0.0", Tkinter.END)
    '''
    # Event handler - User clicked inside the "ui_input" field
    def eventInputClick(self, event):
        if(self.first_click):
            # If this is the first time the user clicked,
            # clear out the tutorial message currently in the box.
            # Otherwise, ignore it.
            self.textinput.delete("0.0", Tkinter.END)
            self.first_click = False;
    '''          
App()
   
