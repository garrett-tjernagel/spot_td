import tkinter as tk
import tkinter.ttk as ttk

# Colors
c_spotify_green = '#1DB954'
c_black = '#000000'
c_white = '#FFFFFF'

class pages(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("SpotTD Dev")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (HomePage, SettingsPage, ConnectionsPage, NavPage, PlayPage):
            frame = F(container, self)
            frame.configure(
                bg=c_black
            )
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
        
        home_page_label = tk.Label(
            self,
            text="Home Page",
            bg=c_black,
            fg=c_spotify_green
        )
        
        #Main Menu Container
        home_nav_container = tk.Frame(self)
        #------------------------------------------------------------
        connections_disp_ctrl_container = tk.Frame(master=home_nav_container)

        go_to_connections_page_b = tk.Button(
            master=connections_disp_ctrl_container,
            text="Go to the Connections Page",
            width=25,
            command=lambda: controller.show_frame(ConnectionsPage),
        )
        go_to_connections_page_b.pack(side="left", fill=tk.X)
        go_to_connections_page_l = tk.Label(
            master=connections_disp_ctrl_container,
            text="Connections Info Display"
        )
        go_to_connections_page_l.pack(side="left", fill=tk.X)
        
        connections_disp_ctrl_container.pack(side="top", fill=tk.X)
        #------------------------------------------------------------
        settings_disp_ctrl_container = tk.Frame(master=home_nav_container)
    
        go_to_settings_page_b = tk.Button(
            master=settings_disp_ctrl_container,
            text="Go to the Settings Page",
            width=25,
            command=lambda: controller.show_frame(SettingsPage),
        )
        go_to_settings_page_b.pack(side="left", fill=tk.X)

        go_to_settings_page_l = tk.Label(
            master=settings_disp_ctrl_container,
            text="Settings Info Display",
        )
        go_to_settings_page_l.pack(side="left", fill=tk.X)

        settings_disp_ctrl_container.pack(side="top", fill=tk.X)
        #------------------------------------------------------------
        nav_disp_ctrl_container = tk.Frame(master=home_nav_container)

        go_to_nav_page_b = tk.Button(
            master=nav_disp_ctrl_container,
            text="Go to the Nav Page",
            width=25,
            command=lambda: controller.show_frame(NavPage),
        )
        go_to_nav_page_b.pack(side="left", fill=tk.X)
        go_to_nav_page_l = tk.Label(
            master=nav_disp_ctrl_container,
            text="Nav Info Display"
        )
        go_to_nav_page_l.pack(side="left", fill=tk.X)
        
        nav_disp_ctrl_container.pack(side="top", fill=tk.X)
        #------------------------------------------------------------
        
        #Kill Button
        kill_button = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )

        # Frame Packing order 
        home_page_label.pack(side="top",fill=tk.X)
        
        home_nav_container.pack(side='top',fill=tk.X)

        kill_button.pack(side="top", fill=tk.X)

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

        kill_button = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )
        kill_button.pack(side="bottom", fill=tk.X)

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

        kill_button = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )
        kill_button.pack(side="bottom", fill=tk.X)

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

        kill_button = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )
        kill_button.pack(side="bottom", fill=tk.X)

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

        kill_button = tk.Button(
            self,
            text="KILL",
            bg=c_black,
            fg=c_spotify_green,
            command=controller.destroy,
        )
        kill_button.pack(side="bottom", fill=tk.X)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        go_to_nav_page_b = tk.Button(
            self,
            text="Go to the Nav Page",
            command=lambda: controller.show_frame(NavPage),
        )
        go_to_nav_page_b.pack(side="bottom", fill=tk.X)

# Launches Main
app = pages()
app.mainloop()
