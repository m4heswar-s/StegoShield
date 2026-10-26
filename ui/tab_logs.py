import os
import tkinter as tk
from tkinter import scrolledtext
from core.logger import session_logs


def setup_logs_tab(tab4):
    #Tab4 Active Session Audit Logs
    tab4_frame = tk.LabelFrame(tab4, text=" Active Session Audit Logs ", font=("Arial",15,"bold"), bg="#1e293b", fg="#f8fafc", relief="solid")
    tab4_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    #tab4 functions
    def shrink_path(path_str, max_len=32):
        if len(path_str) <= max_len:
            return path_str
        return path_str[: max_len - 15]+ "..." +path_str[-12:]

    def refresh_logs():
        log_text_box.config(state=tk.NORMAL)
        log_text_box.delete("1.0", tk.END)
        if not session_logs:
            log_text_box.insert(tk.END, "No events logged during this session.")
            log_text_box.config(state=tk.DISABLED)
            return
        header = f"{'TIME':<20} | {'OPERATION':<10} | {'FILE':<35} | {'STATUS'}\n"
        divider = "-" * 80 + "\n"
        log_text_box.insert(tk.END, header + divider)
        for entry in session_logs:
            display_name = shrink_path(entry["FILE"], max_len=35)
            row = (f"{entry['TIME']:<20} | {entry['OPERATION']:<10} |" f" {display_name:<35} | {entry['STATUS']}\n")
            log_text_box.insert(tk.END, row)
        log_text_box.config(state=tk.DISABLED)


    #Tab4 widgets
    tk.Button(tab4_frame, text="Refresh Logs", command=refresh_logs, bg="#6366f1", fg="#f8fafc", font=("Arial",11,"bold"), relief="flat", padx=10, pady=5).pack(anchor="w", padx=10, pady=5)
    log_text_box = scrolledtext.ScrolledText(tab4_frame, width=80, height=14, font=("Consolas",10), bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", relief="solid", highlightthickness=2, highlightbackground="#98C4F9", highlightcolor="#6366f1", state=tk.DISABLED)
    log_text_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)