import tkinter as tk
from tkinter import messagebox
import datetime

# Sample data for flu vaccine schedule
VACCINE_SCHEDULE = [
    {"year": 2024, "recommended_date": "2024-09-15"},
    {"year": 2025, "recommended_date": "2025-09-15"},
    {"year": 2026, "recommended_date": "2026-09-15"}
]

vaccination_history = []  # List to track vaccination dates


# Functions
def record_vaccination():
    date_str = entry_date.get()
    try:
        vaccine_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        vaccination_history.append(vaccine_date)
        messagebox.showinfo("Success", f"Vaccination recorded on {vaccine_date}.")
        entry_date.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")


def view_vaccination_history():
    if vaccination_history:
        history = "\n".join(f"- Vaccinated on: {date}" for date in vaccination_history)
        messagebox.showinfo("Vaccination History", history)
    else:
        messagebox.showinfo("Vaccination History", "No vaccination history found.")


def view_upcoming_vaccinations():
    today = datetime.date.today()
    vaccinated_years = {date.year for date in vaccination_history}
    upcoming = []
    for entry in VACCINE_SCHEDULE:
        year = entry["year"]
        recommended_date = datetime.datetime.strptime(entry["recommended_date"], "%Y-%m-%d").date()
        if year not in vaccinated_years and recommended_date >= today:
            upcoming.append(f"- Year {year}: Recommended Date - {recommended_date}")

    if upcoming:
        messagebox.showinfo("Upcoming Vaccinations", "\n".join(upcoming))
    else:
        messagebox.showinfo("Upcoming Vaccinations", "No upcoming vaccinations found.")


# GUI Setup
root = tk.Tk()
root.title("Flu Vaccine Tracker")

# Widgets
label_title = tk.Label(root, text="Flu Vaccine Tracker", font=("Arial", 16))
label_date = tk.Label(root, text="Enter Vaccination Date (YYYY-MM-DD):")
entry_date = tk.Entry(root, width=20)

button_record = tk.Button(root, text="Record Vaccination", command=record_vaccination)
button_history = tk.Button(root, text="View Vaccination History", command=view_vaccination_history)
button_upcoming = tk.Button(root, text="View Upcoming Vaccinations", command=view_upcoming_vaccinations)
button_exit = tk.Button(root, text="Exit", command=root.quit)

# Layout
label_title.grid(row=0, column=0, columnspan=2, pady=10)
label_date.grid(row=1, column=0, padx=10, pady=5)
entry_date.grid(row=1, column=1, padx=10, pady=5)

button_record.grid(row=2, column=0, columnspan=2, pady=5)
button_history.grid(row=3, column=0, columnspan=2, pady=5)
button_upcoming.grid(row=4, column=0, columnspan=2, pady=5)
button_exit.grid(row=5, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()