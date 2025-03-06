# Yield-to-Maturity (YTM) Solver

- This project calculates the **Yield-to-Maturity (YTM)** of a bond using the Newton-Raphson method.
- It includes an interactive GUI built with Tkinter, real-time YTM computation, and a visualization of the solver's convergence.

---

## Files
- `ytm_solver.py`: Main script for computing YTM and displaying the GUI with convergence plot.
- `output.png`: Plot.

---

## Libraries Used
- `numpy`
- `matplotlib`
- `tkinter`
- `matplotlib.backends.backend_tkagg`

---

## Features
- **Input**: User provides bond price, coupon payment, face value, and number of periods via a GUI.
- **Output**: Computes YTM and visualizes the Newton-Raphson solver’s convergence in real-time.
- **Visualization**: Displays a plot of YTM estimates over iterations, with the final YTM value highlighted.
- **Error Handling**: Validates inputs (e.g., positive price/face value/periods, non-negative coupon).
