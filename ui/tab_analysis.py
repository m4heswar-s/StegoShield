import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image
from core.logger import logs


def setup_analysis_tab(tab3):
    #Tab3 Forensic Bit Distribution Analysis
    tab3_frame = tk.LabelFrame(tab3, text=" Forensic Bit Distribution Analysis ", font=("Arial",15,"bold"), bg="#1e293b", fg="#f8fafc", relief="solid")
    tab3_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    top_frame = tk.Frame(tab3_frame, bg="#1e293b")
    top_frame.pack(fill=tk.X, padx=10, pady=5)

    # tab3 functions
    def browse_analyseimg():
        path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")])
        if path:
            anaylsis_entry.delete(0, tk.END)
            anaylsis_entry.insert(0, path)


    def run_analyse():
        imgPath = anaylsis_entry.get().strip()
        if not imgPath:
            messagebox.showerror("Error", "Please select an image to analyze!")
            return

        try:
            for widget in chart_frame.winfo_children():
                widget.destroy()

            img = Image.open(imgPath)
            img_array = np.array(img)
            flat_array = img_array.flatten()

            lsb = flat_array & 1
            total_bit = len(lsb)
            one_count = np.sum(lsb)
            zero_count = total_bit - one_count
            ratio_one = one_count/total_bit

            logs("ANALYSE", imgPath, f"SUCCESS")

            fig, ax = plt.subplots(figsize=(6, 3.2), dpi=100)
            fig.patch.set_facecolor("#1e293b")
            ax.set_facecolor("#dfe6f6")
            bars = ax.bar(["Binary 0s", "Binary 1s"], [zero_count, one_count], color=["#ea0f25", "#4346f4"], width=0.5)
            ax.set_title(f"StegoShield LSB Bit Distribution ({imgPath})\nBit-1 Ratio:"f" {ratio_one:.4f}", fontsize=10, fontweight="bold", color="#f8fafc")
            ax.set_ylabel("Bit Count", fontsize=9, color="#f8fafc")
            ax.tick_params(colors="#f8fafc")
            for spine in ax.spines.values():
                spine.set_color("#475569")
                ax.grid(axis="y", linestyle="--", alpha=0.6, color="#475569")

            for bar in bars:
                y_value = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2.0, y_value/2, f"{y_value:,}", ha="center", va="center", color="#f8fafc", fontweight="bold", fontsize=9)

            fig.tight_layout()

            canvas = FigureCanvasTkAgg(fig, master=chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            logs("ANALYSE", imgPath, f"FAILED: {e}")
            messagebox.showerror("Analysis Failed", str(e))


    #tab3 widgets
    tk.Label(top_frame, text="Image to Scan:", font=("Arial",12), bg="#1e293b", fg="#f8fafc").pack(side=tk.LEFT, padx=5)
    anaylsis_entry = tk.Entry(top_frame, width=45, font=("Arial",10), bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", relief="solid", highlightthickness=2, highlightbackground="#98C4F9", highlightcolor="#6366f1")
    anaylsis_entry.pack(side=tk.LEFT, padx=5)
    tk.Button(top_frame, text="Browse", command=browse_analyseimg, bg="#06b6d4", fg="#0f172a", font=("Arial",10, "bold"), relief="flat").pack(side=tk.LEFT, padx=5)
    tk.Button(top_frame, text="Run Scan", command=run_analyse, bg="#6366f1", fg="#f8fafc", font=("Arial",11, "bold"), relief="flat", padx=10, pady=2).pack(side=tk.LEFT, padx=10)

    chart_frame = tk.Frame(tab3_frame, bg="#1e293b")
    chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)