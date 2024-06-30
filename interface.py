# *-* coding: utf-8 *-*
# @Author: @2sayle
# Date: 2024-30-06
# Version: 1.0
# Description: Graphical interface for the Solar Panel Simulator

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from solarpanel import SolarPanel

class SolarPanelInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Solar Panel Simulator")
        self.master.geometry("1200x800")

        self.create_input_frame()
        self.create_plot_frames()

        self.solar_panel = SolarPanel(area=2, efficiency=20, tilt=30, orientation=0)

    def create_input_frame(self):
        input_frame = ttk.Frame(self.master, padding="10")
        input_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(input_frame, text="Area (m²):").grid(row=0, column=0, sticky=tk.W)
        self.area_entry = ttk.Entry(input_frame)
        self.area_entry.grid(row=0, column=1)
        self.area_entry.insert(0, "2")

        ttk.Label(input_frame, text="Efficiency (%):").grid(row=1, column=0, sticky=tk.W)
        self.efficiency_entry = ttk.Entry(input_frame)
        self.efficiency_entry.grid(row=1, column=1)
        self.efficiency_entry.insert(0, "20")

        ttk.Label(input_frame, text="Tilt (°):").grid(row=2, column=0, sticky=tk.W)
        self.tilt_entry = ttk.Entry(input_frame)
        self.tilt_entry.grid(row=2, column=1)
        self.tilt_entry.insert(0, "30")

        ttk.Label(input_frame, text="Orientation (°):").grid(row=3, column=0, sticky=tk.W)
        self.orientation_entry = ttk.Entry(input_frame)
        self.orientation_entry.grid(row=3, column=1)
        self.orientation_entry.insert(0, "0")

        ttk.Button(input_frame, text="Apply", command=self.update_plots).grid(row=4, column=0, columnspan=2)

    def create_plot_frames(self):
        self.irradiance_frame = ttk.Frame(self.master)
        self.irradiance_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.power_frame = ttk.Frame(self.master)
        self.power_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.update_plots()

    def update_plots(self):
        plt.close("all") # Close all previous plots
        try:
            area = float(self.area_entry.get())
            efficiency = float(self.efficiency_entry.get())
            tilt = float(self.tilt_entry.get())
            orientation = float(self.orientation_entry.get())

            self.solar_panel = SolarPanel(area, efficiency, tilt, orientation)

            hour = 15
            latitude = 48.85
            days = list(range(1, 366))
            irradiances = []
            powers = []

            for day in days:
                irradiance = self.solar_panel.computeIrradiance(hour, day, latitude)
                power = self.solar_panel.computePower(irradiance)
                irradiances.append(irradiance)
                powers.append(power)

            self.plot_irradiance(days, irradiances)
            self.plot_power(days, powers)

        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numbers for the input fields.")

    def plot_irradiance(self, days, irradiances):
        for widget in self.irradiance_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(days, irradiances, 'r-')
        ax.set_title("Annual Irradiance")
        ax.set_xlabel("Day of the Year")
        ax.set_ylabel("Irradiance (W/m²)")
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=self.irradiance_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_power(self, days, powers):
        for widget in self.power_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(days, powers, 'b-')
        ax.set_title("Annual Power Production")
        ax.set_xlabel("Day of the Year")
        ax.set_ylabel("Power (W)")
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=self.power_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = SolarPanelInterface(root)
    root.mainloop()