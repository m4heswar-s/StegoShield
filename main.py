import tkinter as tk
from tkinter import ttk
from ui.tab_analysis import setup_analysis_tab
from ui.tab_decode import setup_decode_tab
from ui.tab_encode import setup_encode_tab
from ui.tab_logs import setup_logs_tab

window =tk.Tk()
window.title("StegoShield Security & Forensics Suite")
window.geometry("900x700")
window.config(bg="#0f172a")

#Header Banner
title_frame= tk.Frame(window, bg="#1e293b",bd=2, relief="groove", highlightbackground="#6366f1")
title_frame.pack(fill=tk.X,padx=15,pady=15)
tk.Label(title_frame, text="StegoShield Security Suite", font=("Arial",18,"bold"),bg="#1e293b",fg="white",).pack()


#Notebook Container for Tabs
tabCollection = ttk.Notebook(window)

# #Initialize and configure ttk styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook",background="#0f172a",borderwidth=0)
style.configure("TNotebook.Tab", font=("Segoe UI", 11, "bold"), padding=[15, 8], background="#1e293b", foreground= "#f8fafc",borderwidth=1,relief="flat")
style.map("TNotebook.Tab", background=[("selected", "#6366f1"), ("active", "#334155")], foreground=[("selected", "#f8fafc"),("active", "#f8fafc")],focuscolor=[("selected", "#6366f1"), ("active", "#1e293b")])

tabCollection.pack(fill=tk.BOTH, expand=True)

# Create individual frames for each tab
tab1 = tk.Frame(tabCollection,bd=2, relief="solid",highlightbackground="#334155", bg="#1e293b")
tab2 = tk.Frame(tabCollection,bd=2, relief="solid",highlightbackground="#334155", bg="#1e293b")
tab3 = tk.Frame(tabCollection,bd=2, relief="solid",highlightbackground="#334155", bg="#1e293b")
tab4 = tk.Frame(tabCollection,bd=2, relief="solid",highlightbackground="#334155", bg="#1e293b")

# Add them to the notebook control
tabCollection.add(tab1, text="  Encode  ")
tabCollection.add(tab2, text="  Decode  ")
tabCollection.add(tab3, text="  Forensic Analysis  ")
tabCollection.add(tab4, text="  Audit Logs  ")


setup_encode_tab(tab1)
setup_decode_tab(tab2)
setup_analysis_tab(tab3)
setup_logs_tab(tab4)

if __name__ == "__main__":
  window.mainloop()