import tkinter as tk
import random

# --- GUI SETUP ---
root = tk.Tk()
root.title("STEM AI - Biomedical Monitoring Dashboard")
root.geometry("450x400")
root.configure(bg="#1e1e2e")  # Dark theme background

# Title Header
title = tk.Label(root, text="VITAL SIGNS MONITOR (SIMULATION)", font=("Helvetica", 14, "bold"), fg="#cdd6f4", bg="#1e1e2e")
title.pack(pady=15)

# Heart Rate Display Box
hr_frame = tk.Frame(root, bg="#313244", bd=2, relief="groove")
hr_frame.pack(fill="x", padx=20, pady=5)
hr_title = tk.Label(hr_frame, text="HEART RATE", font=("Helvetica", 10, "bold"), fg="#f38ba8", bg="#313244")
hr_title.pack(anchor="w", padx=10, pady=(5,0))
hr_label = tk.Label(hr_frame, text="-- bpm", font=("Helvetica", 22, "bold"), fg="#ffffff", bg="#313244")
hr_label.pack(anchor="e", padx=10, pady=(0,5))

# SpO2 Display Box
spo2_frame = tk.Frame(root, bg="#313244", bd=2, relief="groove")
spo2_frame.pack(fill="x", padx=20, pady=5)
spo2_title = tk.Label(spo2_frame, text="BLOOD OXYGEN (SpO2)", font=("Helvetica", 10, "bold"), fg="#89b4fa", bg="#313244")
spo2_title.pack(anchor="w", padx=10, pady=(5,0))
spo2_label = tk.Label(spo2_frame, text="-- %", font=("Helvetica", 22, "bold"), fg="#ffffff", bg="#313244")
spo2_label.pack(anchor="e", padx=10, pady=(0,5))

# Temperature Display Box
temp_frame = tk.Frame(root, bg="#313244", bd=2, relief="groove")
temp_frame.pack(fill="x", padx=20, pady=5)
temp_title = tk.Label(temp_frame, text="BODY TEMPERATURE", font=("Helvetica", 10, "bold"), fg="#a6e3a1", bg="#313244")
temp_title.pack(anchor="w", padx=10, pady=(5,0))
temp_label = tk.Label(temp_frame, text="-- °C", font=("Helvetica", 22, "bold"), fg="#ffffff", bg="#313244")
temp_label.pack(anchor="e", padx=10, pady=(0,5))

# --- SIMULATED DATA LOOP ---
def update_data():
    # Generate realistic fake medical data entirely in Python
    sim_hr = random.randint(72, 85)
    sim_spo2 = random.randint(96, 100)
    sim_temp = round(random.uniform(36.4, 37.2), 1)

    # Update the GUI labels with the new numbers
    hr_label.config(text=f"{sim_hr} bpm")
    spo2_label.config(text=f"{sim_spo2} %")
    temp_label.config(text=f"{sim_temp} °C")

    # Refresh every 1000 milliseconds (1 second)
    root.after(1000, update_data)

# Start the loop
root.after(500, update_data)
root.mainloop()