import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from core.logger import logs
from core.stego import decodeImage


def setup_decode_tab(tab2):
    #Tab2 Decode Secret Message
    tab2_frame = tk.LabelFrame(tab2, text=" Decode Secret Message ", font=("Arial",15,"bold"), bg="#1e293b", fg="#f8fafc", relief="solid")
    tab2_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    #Tab2 functions
    def browse_decodeimg():
        path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")])
        if path:
            decodeimg_entry.delete(0, tk.END)
            decodeimg_entry.insert(0, path)

    def reset_decfields():
        decodeimg_entry.delete(0,tk.END)
        decode_result_box.config(state=tk.NORMAL)
        decode_result_box.delete("1.0",tk.END)
        decode_result_box.config(state=tk.DISABLED)

    def run_decode():
        path = decodeimg_entry.get().strip()
        if not path:
            messagebox.showerror("Error", "Please select a stego image to decode!")
            return
        try:
            messg = decodeImage(path)
            logs("DECODE", path, "SUCCESS")
            decode_result_box.config(state=tk.NORMAL)
            decode_result_box.delete("1.0", tk.END)
            decode_result_box.insert(tk.END, messg)
            decode_result_box.config(state=tk.DISABLED)
        except Exception as e:
            logs("DECODE", path, f"FAILED: {e}")
            messagebox.showerror("Decoding Failed", str(e))


    #soure path
    tk.Label(tab2_frame, text="Decode Image Path:", font=("Arial",12), bg="#1e293b", fg="#f8fafc").grid(row=0,column=0,sticky="w",padx=10,pady=5)
    decodeimg_entry = tk.Entry(tab2_frame, width=50, font=("Arial",10), bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", relief="solid", highlightthickness=2, highlightbackground="#98C4F9", highlightcolor="#6366f1")
    decodeimg_entry.grid(row=0, column=1,sticky="w", padx=10, pady=5)
    tk.Button(tab2_frame, text="Browse", command=browse_decodeimg, bg="#06b6d4", fg="#0f172a", font=("Arial",10, "bold"), relief="flat").grid(row=0,column=2,sticky="w",padx=5)

    #button to encode and reset
    btn_frame2 = tk.Frame(tab2_frame, bg=tab2_frame["bg"])
    btn_frame2.grid(row=1,column=1,sticky="w", columnspan=2, pady=15)
    tk.Button(btn_frame2, text="Decode", command=run_decode, bg="#6366f1", fg="#f8fafc", font=("Arial",11, "bold"), padx=10, pady=5, relief="flat").pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame2, text="Reset", command=reset_decfields, bg="#475569", fg="#f8fafc", font=("Arial",11, "bold"), padx=10, pady=5, relief="flat").pack(side=tk.LEFT, padx=5)

    #display decoded text
    tk.Label(tab2_frame, text="Decoded Secret Text:", font=("Arial",12), bg="#1e293b", fg="#f8fafc").grid(row=2, column=0, sticky="nw", padx=10, pady=5)
    decode_result_box = scrolledtext.ScrolledText(tab2_frame, width=50, height=8, font=("Arial",10), bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", relief="solid", highlightthickness=2, highlightbackground="#98C4F9", highlightcolor="#6366f1", state=tk.DISABLED)
    decode_result_box.grid(row=2, column=1,sticky="w", padx=10, pady=5)