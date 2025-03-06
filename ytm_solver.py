import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Step 1: Define bond price calculation
def bond_price(c, fv, y, t):
    pv = sum(c / (1 + y)**i for i in range(1, t + 1))  # Coupon payments
    pv += fv / (1 + y)**t  # Face value
    return pv

# Step 2: Define YTM solver using Newton-Raphson
def solve_ytm(p, c, fv, t, max_iter=100, tol=1e-6):
    y = 0.05  # Initial guess
    hist = [y]
    for _ in range(max_iter):
        price = bond_price(c, fv, y, t)
        diff = price - p
        if abs(diff) < tol:
            break
        deriv = sum(-i * c / (1 + y)**(i + 1) for i in range(1, t + 1)) - t * fv / (1 + y)**(t + 1)
        y -= diff / deriv  # Newton step
        hist.append(y)
    return y, hist

# Step 3: Define GUI update logic
def refresh_output():
    try:
        p = float(e1.get())  # Bond price
        c = float(e2.get())  # Coupon
        fv = float(e3.get())  # Face value
        t = int(e4.get())  # Time periods

        # Step 4: Validate inputs
        if p <= 0 or c < 0 or fv <= 0 or t <= 0:
            raise ValueError("Price, face value, and time must be positive; coupon cannot be negative")

        # Step 5: Compute YTM and convergence history
        ytm, hist = solve_ytm(p, c, fv, t)
        lbl_ytm.config(text=f"YTM: {ytm:.4%}")

        # Step 6: Generate plot data
        iters = list(range(len(hist)))
        yy = hist

        # Step 7: Update plot
        ax.clear()
        ax.plot(iters, yy, color='#FF6B6B', lw=2, label='YTM Convergence')
        ax.axhline(ytm, color='#4ECDC4', ls='--', alpha=0.6, label=f'YTM={ytm:.4%}')
        ax.set_xlabel('Iteration', color='white')
        ax.set_ylabel('Yield', color='white')
        ax.set_title('YTM Solver Convergence', color='white')
        ax.set_facecolor('#2B2B2B')
        fig.set_facecolor('#1E1E1E')
        ax.grid(True, ls='--', color='#555555', alpha=0.5)
        ax.legend(facecolor='#333333', edgecolor='white', labelcolor='white')
        ax.tick_params(colors='white')
        canv.draw()

    except ValueError as err:
        messagebox.showerror("Error", str(err))

# Step 8: Initialize GUI
root = tk.Tk()
root.title("YTM Solver")
root.configure(bg='#1E1E1E')

frm = ttk.Frame(root, padding=10)
frm.pack()
frm.configure(style='Dark.TFrame')

# Step 9: Set up plot
fig, ax = plt.subplots(figsize=(7, 5))
canv = FigureCanvasTkAgg(fig, master=frm)
canv.get_tk_widget().pack(side=tk.LEFT)

# Step 10: Build input panel
pf = ttk.Frame(frm)
pf.pack(side=tk.RIGHT, padx=10)
pf.configure(style='Dark.TFrame')

# Dark theme styling
style = ttk.Style()
style.theme_use('default')
style.configure('Dark.TFrame', background='#1E1E1E')
style.configure('Dark.TLabel', background='#1E1E1E', foreground='white')
style.configure('TButton', background='#333333', foreground='white')
style.configure('TEntry', fieldbackground='#333333', foreground='white')

ttk.Label(pf, text="Bond Price:", style='Dark.TLabel').pack(pady=3)
e1 = ttk.Entry(pf); e1.pack(pady=3); e1.insert(0, "950")
ttk.Label(pf, text="Coupon:", style='Dark.TLabel').pack(pady=3)
e2 = ttk.Entry(pf); e2.pack(pady=3); e2.insert(0, "50")
ttk.Label(pf, text="Face Value:", style='Dark.TLabel').pack(pady=3)
e3 = ttk.Entry(pf); e3.pack(pady=3); e3.insert(0, "1000")
ttk.Label(pf, text="Periods:", style='Dark.TLabel').pack(pady=3)
e4 = ttk.Entry(pf); e4.pack(pady=3); e4.insert(0, "10")

ttk.Button(pf, text="Calculate", command=refresh_output).pack(pady=10)

lbl_ytm = ttk.Label(pf, text="YTM: ", style='Dark.TLabel'); lbl_ytm.pack(pady=2)

# Step 11: Run initial calculation and start GUI
refresh_output()
root.mainloop()