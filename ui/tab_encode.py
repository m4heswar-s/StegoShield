import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from core.logger import logs
from core.stego import encodeImage, getImageCapacity


def setup_encode_tab(tab1):
    # Tab1 Encode Secret Message
    tab1_frame = tk.LabelFrame(tab1, text=" Encode Secret Message ",font=("Arial",15,"bold"),bg="#1e293b", fg="#f8fafc", relief="solid")
    tab1_frame.pack(fill=tk.BOTH,expand=True, padx=10, pady=10)

    #Tab1 functions
    def browse_encodeimg_src():
        path= filedialog.askopenfilename(filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")])
        if path:
            encodeimg_src_entry.delete(0, tk.END)
            encodeimg_src_entry.insert(0, path)
            capacity = getImageCapacity(path)
            capacity_lbl.config(text=f"Max Capacity: {capacity:,} characters", fg="#10b981")

    def browse_encodeimg_out():
        path = filedialog.asksaveasfilename( defaultextension=".png", filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")])
        if path:
            encodeimg_out_entry.delete(0, tk.END)
            encodeimg_out_entry.insert(0, path)

    def reset_encfields():
        encodeimg_src_entry.delete(0,tk.END)
        encodeimg_out_entry.delete(0,tk.END)
        secretText_box.delete("1.0",tk.END)
        capacity_lbl.config(text="Max Capacity: Select an image", fg="#94a3b8")

    def run_encode():
        src_path = encodeimg_src_entry.get().strip()
        out_path = encodeimg_out_entry.get().strip()
        messg = secretText_box.get("1.0", tk.END).strip()
        if not src_path or not out_path or not messg:
            messagebox.showerror("Error", "All fields (Source, Output, Message) are required!")
            return
        try:
            encodeImage(src_path, out_path, messg)
            logs("ENCODE", src_path, "SUCCESS")
            messagebox.showinfo("Success", f"Stego image successfully created and saved as:\n{out_path}")
        except Exception as e:
            logs("ENCODE", src_path, f"FAILED: {e}")
            messagebox.showerror("Encoding Failed", str(e))


    #Source path
    tk.Label(tab1_frame, text="Source Image Path:", font=("Arial", 12), bg="#1e293b", fg="#f8fafc").grid(row=0,column=0,sticky="w",padx=10,pady=5)
    encodeimg_src_entry = tk.Entry(tab1_frame, width=50, font=("Arial", 10), bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", relief="solid", highlightthickness=2,highlightbackground="#98C4F9",highlightcolor="#6366f1")
    encodeimg_src_entry.grid(row=0, column=1,sticky="w", padx=10, pady=5)
    tk.Button(tab1_frame, text="Browse", command=browse_encodeimg_src, bg="#06b6d4", fg="#0f172a", font=("Arial", 10, "bold"), relief="flat").grid(row=0,column=2,padx=5)

    #capacity
    capacity_lbl = tk.Label(tab1_frame, text="Max Capacity: Select an image",fg="#94a3b8",font=("Arial", 11, "italic"), bg="#1e293b")
    capacity_lbl.grid(row=1,column=1, padx=10)

    #output path
    tk.Label(tab1_frame, text="Output Image Path:", font=("Arial",12), bg="#1e293b", fg="#f8fafc").grid(row=2,column=0,sticky="w",padx=10,pady=5)
    encodeimg_out_entry = tk.Entry(tab1_frame, width=50, font=("Arial",10), bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", relief="solid", highlightthickness=2,highlightbackground="#98C4F9",highlightcolor="#6366f1")
    encodeimg_out_entry.grid(row=2, column=1,sticky="w", padx=10, pady=5)
    tk.Button(tab1_frame, text="Browse", command=browse_encodeimg_out, bg="#06b6d4", fg="#0f172a", font=("Arial", 10, "bold"), relief="flat").grid(row=2, column=2, padx=5)

    #text box for secret message
    tk.Label(tab1_frame, text="Secret Message:", font=("Arial", 12), bg="#1e293b", fg="#f8fafc").grid(row=3,column=0,sticky="nw",padx=10,pady=5)
    secretText_box = scrolledtext.ScrolledText(tab1_frame, width=50, height=6, font=("Arial",10), bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", relief="solid", highlightthickness=2,highlightbackground="#98C4F9",highlightcolor="#6366f1")
    secretText_box.grid(row=3,column=1,sticky="w",padx=10,pady=5)

    #button to encode and reset
    btn_frame1 = tk.Frame(tab1_frame, bg=tab1_frame["bg"])
    btn_frame1.grid(row=4,column=1,sticky="w", columnspan=2, pady=15)
    tk.Button(btn_frame1, text="Encode",command=run_encode,bg="#6366f1", fg="#f8fafc", font=("Arial", 11, "bold"),padx=10, pady=5, relief="flat").pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame1, text="Reset", command=reset_encfields, bg="#475569", fg="#f8fafc", font=("Arial", 11, "bold"), padx=10, pady=5, relief="flat").pack(side=tk.LEFT, padx=5)