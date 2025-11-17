import tkinter as tk
from tkinter import ttk

def show_profile():
    # Create main window
    root = tk.Tk()
    root.title("Professional Profile - Saim Abbas")
    root.geometry("500x350")
    root.configure(bg="#e6ecf0")  # light gray-blue background

    # Title Label
    title_label = tk.Label(
        root,
        text="Personal Profile Summary",
        font=("Helvetica", 18, "bold"),
        fg="#1a1a1a",
        bg="#e6ecf0"
    )
    title_label.pack(pady=20)

    # Frame for details
    frame = tk.Frame(root, bg="white", bd=2, relief="groove")
    frame.pack(padx=30, pady=10, fill="x")

    # Information dictionary
    info = {
        "Name": "Saim Abbas",
        "Age": "20",
        "Religion": "Muslim",
        "Education": "Undergraduate (Software Engineering)",
        "Skill's": "Python,SQL,github",
        "status": "bachelor",
        "Technology": "Peak",
    }

    # Display profile info
    row = 0
    for key, value in info.items():
        tk.Label(frame, text=f"{key}:", font=("Helvetica", 12, "bold"), bg="white").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        tk.Label(frame, text=value, font=("Helvetica", 12), bg="white").grid(row=row, column=1, sticky="w", padx=10, pady=5)
        row += 1

    # Footer
    footer = tk.Label(
        root,
        text="Thank you for reviewing my profile.",
        font=("Helvetica", 10, "italic"),
        fg="#555",
        bg="#e6ecf0"
    )
    footer.pack(side="bottom", pady=15)

    # Keep the window running
    root.mainloop()

# Run GUI
if __name__ == "__main__":
    show_profile()
