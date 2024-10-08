import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger


def merge_pdfs(pdf_files, output_path="merged_output.pdf"):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Append each PDF in the specified order
    for pdf in pdf_files:
        if os.path.exists(pdf):
            print(f"Adding {pdf} to the merger.")
            merger.append(pdf)
        else:
            print(f"File not found: {pdf}")

    # Write out the merged PDF to the specified output file
    merger.write(output_path)
    merger.close()
    print(f"PDFs merged into {output_path} successfully.")
    messagebox.showinfo("Success", f"PDFs merged into {output_path} successfully.")


class PDFMergerApp:
    def __init__(self, root, files):
        self.root = root
        self.files = list(files)
        self.root.title("PDF Merger")

        # Set window size and position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 400
        window_height = 300

        # Calculate the position to place the window at the top
        x_position = (screen_width - window_width) // 2
        y_position = 0  # Top of the screen

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Keep the window on top of other windows
        self.root.attributes("-topmost", True)

        # Create and place widgets
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        for file in files:
            self.listbox.insert(tk.END, os.path.basename(file))

        self.move_up_button = tk.Button(root, text="Move Up", command=self.move_up)
        self.move_up_button.pack(side=tk.LEFT, padx=5)

        self.move_down_button = tk.Button(
            root, text="Move Down", command=self.move_down
        )
        self.move_down_button.pack(side=tk.LEFT, padx=5)

        self.add_files = tk.Button(root, text="Add Files", command=self.add_files)
        self.add_files.pack(side=tk.LEFT, padx=5)

        self.merge_button = tk.Button(root, text="Merge PDFs", command=self.merge_files)
        self.merge_button.pack(pady=10)

    def move_up(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            if index > 0:
                file = self.files.pop(index)
                self.files.insert(index - 1, file)
                self.listbox.delete(index)
                self.listbox.insert(index - 1, os.path.basename(file))
                self.listbox.select_set(index - 1)

    def move_down(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.files) - 1:
                file = self.files.pop(index)
                self.files.insert(index + 1, file)
                self.listbox.delete(index)
                self.listbox.insert(index + 1, os.path.basename(file))
                self.listbox.select_set(index + 1)

    def add_files(self):
        # Allow users to add more PDF files
        new_files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file in new_files:
            if file not in self.files:
                self.files.append(file)
                self.listbox.insert(tk.END, os.path.basename(file))

    def merge_files(self):
        if not self.files:
            messagebox.showwarning("Warning", "No files to merge.")
            return

        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")]
        )
        if output_file:
            merge_pdfs(self.files, output_file)
            self.root.destroy()


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        for file in files:
            if not file.lower().endswith(".pdf"):
                files.remove(file)
    else:
        files = filedialog.askopenfilenames(
            title="Select PDFs to Merge", filetypes=[("PDF files", "*.pdf")]
        )
        if not files:
            return
    root = tk.Tk()
    app = PDFMergerApp(root, files)
    root.mainloop()


if __name__ == "__main__":
    main()
