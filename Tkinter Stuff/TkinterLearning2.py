import tkinter as tk
import tkinter.ttk as ttk
import PIL.Image as im
import PIL.ImageTk as imtk



# Colors
c_spotify_green = '#1DB954'
c_black = '#000000'
c_white = '#FFFFFF'
c_grey = '#6B6B6B'

button_pad = 10
label_pad = 10

header_label_height = 3
header_label_width = 40

info_label_height = 3
info_label_width = 20

button_image_size = 50

class pages(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("SpotTD Dev")

        # creating a frame and assigning it to container
        container = tk.Frame(self)

        # specifying the region where the frame is packed in root
        container.pack(expand=True,fill=tk.BOTH)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (HomePage, SettingsPage, ConnectionsPage, NavPage, PlayPage):
            frame = F(container, self)
            #frame.configure(bg=c_black)
            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

class HomePage(tk.Frame):  # Can go to Connections, Nav, and Settings
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Images
        self.btlImg = im.open("C:/Data/spot_td/Tkinter Stuff/Pictures/btlogo.png").resize((button_image_size, button_image_size), im.ANTIALIAS)
        self.navImg = im.open("C:/Data/spot_td/Tkinter Stuff/Pictures/playpause.png").resize((button_image_size, button_image_size), im.ANTIALIAS)
        self.setImg = im.open("C:/Data/spot_td/Tkinter Stuff/Pictures/settingwheel.png").resize((button_image_size, button_image_size), im.ANTIALIAS)

        self.btlImg = imtk.PhotoImage(self.btlImg)
        self.navImg = imtk.PhotoImage(self.navImg)
        self.setImg = imtk.PhotoImage(self.setImg)

        #Bins
        btBin = tk.Frame(self)
        settingsBin = tk.Frame(self)
        navBin = tk.Frame(self)

        #Labels
        L_homePage = tk.Label(
            self,
            text="L: Landing Page Label",
            padx=label_pad,
            pady=label_pad/2,
            height=header_label_height,
            width=header_label_width,
            bg=c_grey,
            fg=c_spotify_green
        )
        L_btInfo = tk.Label(
            btBin,
            text="L: BT Info",
            padx=label_pad,
            pady=label_pad/2,
            height=info_label_height,
            width=info_label_width,
            bg=c_grey,
            fg=c_spotify_green
        )
        L_navInfo = tk.Label(
            navBin,
            text="L: Nav Info",
            padx=label_pad,
            pady=label_pad/2,
            height=info_label_height,
            width=info_label_width,
            bg=c_grey,
            fg=c_spotify_green
        )
        L_settingsInfo = tk.Label(
            settingsBin,
            text="L: Settings Info",
            padx=label_pad,
            pady=label_pad/2,
            height=info_label_height,
            width=info_label_width,
            bg=c_grey,
            fg=c_spotify_green
        )

        #Buttons
        B_goToConnectionsPage = tk.Button(
            btBin,
            compound='center',
            text="B: Go to Connections Page",
            #bg=c_black,
            fg=c_spotify_green,
            padx=button_pad,
            pady=button_pad/2,
            height=button_image_size/2,
            width=button_image_size/2,
            image=self.btlImg,
            command=lambda: controller.show_frame(ConnectionsPage),
        )
        B_goToNavigationPage = tk.Button(
            navBin,
            compound='center',
            text="B: Go to Nav Page",
            #bg=c_black,
            fg=c_spotify_green,
            padx=button_pad,
            pady=button_pad/2,
            height=button_image_size,
            width=button_image_size,
            image=self.navImg,
            command=lambda: controller.show_frame(NavPage),
        )
        B_goToSettingsPage = tk.Button(
            settingsBin,
            compound='center',
            text="B: Go to Settings Page",
            #bg=c_black,
            fg=c_spotify_green,
            padx=button_pad,
            pady=button_pad/2,
            height=button_image_size,
            width=button_image_size,
            image=self.setImg,
            command=lambda: controller.show_frame(SettingsPage),
        )
        B_killMaster = tk.Button(
            self,
            text="B: KILL MASTER",
            bg=c_black,
            fg=c_spotify_green,
            padx=button_pad,
            pady=button_pad/2,
            height=header_label_height,
            width=header_label_width,
            command=controller.destroy
        )

        # Grid Layout
        L_homePage.pack(side='top',expand=True,fill=tk.X)

        B_goToConnectionsPage.pack(side='left',expand=True,fill=tk.BOTH)
        L_btInfo.pack(side='right',expand=True,fill=tk.BOTH)
        btBin.pack(side='top',expand=True,fill=tk.BOTH)

        B_goToNavigationPage.pack(side='left',expand=True,fill=tk.BOTH)
        L_navInfo.pack(side='right',expand=True,fill=tk.BOTH)
        navBin.pack(side='top',expand=True,fill=tk.BOTH)

        B_goToSettingsPage.pack(side='left',expand=True,fill=tk.BOTH)
        L_settingsInfo.pack(side='right',expand=True,fill=tk.BOTH)
        settingsBin.pack(side='top',expand=True,fill=tk.BOTH)
        
        B_killMaster.pack(side='top',expand=True,fill=tk.X)

class SettingsPage(tk.Frame):  # Can go to Home
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self,
            text="Settings Page",
                        bg=c_black,
            fg=c_spotify_green
            )
        label.pack(side="top",padx=10, pady=10)

        B_killMaster = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )
        B_killMaster.pack(side="bottom", fill=tk.X)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        go_to_home_page_b = tk.Button(
            self,
            text="Go to the Home Page",
            command=lambda: controller.show_frame(HomePage),
        )
        go_to_home_page_b.pack(side="bottom", fill=tk.X)

class ConnectionsPage(tk.Frame):  # Can go to Home
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self,
            text="Connections Page",
                        bg=c_black,
            fg=c_spotify_green
            )
        label.pack(side="top",padx=10, pady=10)

        B_killMaster = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )
        B_killMaster.pack(side="bottom", fill=tk.X)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        go_to_home_page_b = tk.Button(
            self,
            text="Go to the Home Page",
            command=lambda: controller.show_frame(HomePage),
        )
        go_to_home_page_b.pack(side="bottom", fill=tk.X)

class NavPage(tk.Frame):  # Can go to Home
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self,
            text="Nav Page",
                        bg=c_black,
            fg=c_spotify_green
            )
        label.pack(side="top",padx=10, pady=10)

        B_killMaster = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )
        B_killMaster.pack(side="bottom", fill=tk.X)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        go_to_home_page_b = tk.Button(
            self,
            text="Go to the Home Page",
            command=lambda: controller.show_frame(HomePage),
        )
        go_to_home_page_b.pack(side="bottom", fill=tk.X)

        go_to_play_page = tk.Button(
            self,
            text="Go to the Play Page",
            command=lambda: controller.show_frame(PlayPage),
        )
        go_to_play_page.pack(side="bottom", fill=tk.X)

class PlayPage(tk.Frame):  # Can go to Home and Nav
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, 
            text="Play Page",
                        bg=c_black,
            fg=c_spotify_green
            )
        label.pack(side="top",padx=10, pady=10)

        B_killMaster = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )
        B_killMaster.pack(side="bottom", fill=tk.X)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        B_goToNavigationPage = tk.Button(
            self,
            text="Go to the Nav Page",
            command=lambda: controller.show_frame(NavPage),
        )
        B_goToNavigationPage.pack(side="bottom", fill=tk.X)

# Launches Main
app = pages()
app.mainloop()
