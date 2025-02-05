import tkinter as tk
from tkinter import filedialog, messagebox
import json
from makeMrpReport import generate_mrp_report  # Import your MRP report script
from makeSccReport import generate_scc_report  # Import your SCC report script

def select_file(report_type):
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if report_type == "mrp":
        mrp_file_path_label.config(text=file_path)
    elif report_type == "scc":
        scc_file_path_label.config(text=file_path)
    return file_path

def convert_to_pdf(report_type):
    if report_type == "mrp":
        file_path = mrp_file_path_label.cget("text")
        if not file_path:
            messagebox.showerror("Error", "Please select a valid MRP JSON file")
            return

        # Output PDF file name for MRP
        output_pdf = file_path.rsplit('.', 1)[0] + "_mrp_report.pdf"

        try:
            # Call the MRP report generation function
            generate_mrp_report(file_path, output_pdf)
            messagebox.showinfo("Success", f"MRP PDF saved as {output_pdf}")
        except Exception as e:
            messagebox.showerror("Error", f"Error generating MRP report: {e}")

    elif report_type == "scc":
        file_path = scc_file_path_label.cget("text")
        if not file_path:
            messagebox.showerror("Error", "Please select a valid SCC JSON file")
            return

        # Output PDF file name for SCC
        output_pdf = file_path.rsplit('.', 1)[0] + "_scc_report.pdf"

        try:
            # Call the SCC report generation function
            generate_scc_report(file_path, output_pdf)
            messagebox.showinfo("Success", f"SCC PDF saved as {output_pdf}")
        except Exception as e:
            messagebox.showerror("Error", f"Error generating SCC report: {e}")

# Setup main window
root = tk.Tk()
root.title("JSON to PDF Converter")

# Create UI elements for MRP
select_mrp_file_button = tk.Button(root, text="Select MRP JSON File", command=lambda: select_file("mrp"))
select_mrp_file_button.pack(pady=10)

mrp_file_path_label = tk.Label(root, text="No MRP file selected", width=50)
mrp_file_path_label.pack(pady=10)

convert_mrp_button = tk.Button(root, text="Convert MRP to PDF", command=lambda: convert_to_pdf("mrp"))
convert_mrp_button.pack(pady=20)

# Create UI elements for SCC
select_scc_file_button = tk.Button(root, text="Select SCC JSON File", command=lambda: select_file("scc"))
select_scc_file_button.pack(pady=10)

scc_file_path_label = tk.Label(root, text="No SCC file selected", width=50)
scc_file_path_label.pack(pady=10)

convert_scc_button = tk.Button(root, text="Convert SCC to PDF", command=lambda: convert_to_pdf("scc"))
convert_scc_button.pack(pady=20)

# Run the application
root.mainloop()
