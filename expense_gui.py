import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import os

class Expense:
    all_expenses = []

    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category
        Expense.all_expenses.append(self)

def load_data():
    filename = 'expenses.txt'
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        title, amount_str, category = parts
                        amount = float(amount_str.replace('₹', ''))
                        Expense(title, amount, category)
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load data: {e}")

def save_data():
    filename = 'expenses.txt'
    try:
        with open(filename, 'w') as f:
            for e in Expense.all_expenses:
                f.write(f"{e.title},{e.amount},{e.category}\n")
    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save data: {e}")

class ExpenseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker GUI")
        self.root.geometry("700x600")
        
        # Load data
        load_data()
        
        self.setup_ui()
    
    def setup_ui(self):
        # Input frame
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(input_frame, text="Title:").grid(row=0, column=0, sticky=tk.W)
        self.title_entry = ttk.Entry(input_frame, width=20)
        self.title_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(input_frame, text="Amount:").grid(row=0, column=2, sticky=tk.W)
        self.amount_entry = ttk.Entry(input_frame, width=15)
        self.amount_entry.grid(row=0, column=3, padx=5)
        
        ttk.Label(input_frame, text="Category:").grid(row=0, column=4, sticky=tk.W)
        self.category_entry = ttk.Entry(input_frame, width=15)
        self.category_entry.grid(row=0, column=5, padx=5)
        
        ttk.Button(input_frame, text="Add Expense", command=self.add_expense).grid(row=0, column=6, padx=10)
        
        ttk.Button(input_frame, text="Delete by Title", command=self.delete_expense).grid(row=0, column=7, padx=5)
        
        # Buttons frame
        btn_frame = ttk.Frame(self.root, padding="10")
        btn_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        ttk.Button(btn_frame, text="View All", command=self.view_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Total Amount", command=self.show_total).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Filter Category", command=self.filter_category).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear Output", command=self.clear_output).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Save & Exit", command=self.on_exit).pack(side=tk.RIGHT, padx=5)
        
        # Output
        self.output_text = scrolledtext.ScrolledText(self.root, height=25, width=80)
        self.output_text.grid(row=2, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Status
        self.status_label = ttk.Label(self.root, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.grid(row=3, column=0, sticky=(tk.W, tk.E), padx=10)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)
    
    def update_status(self, msg):
        self.status_label.config(text=msg)
    
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
    
    def add_expense(self):
        try:
            title = self.title_entry.get().strip()
            amount = float(self.amount_entry.get())
            category = self.category_entry.get().strip()
            
            if not title or not category or amount <= 0:
                raise ValueError("Invalid input")
            
            Expense(title, amount, category)
            save_data()
            self.update_status(f"Added: {title} - ₹{amount} ({category})")
            self.clear_entries()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    
    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
    
    def view_all(self):
        self.clear_output()
        if not Expense.all_expenses:
            self.output_text.insert(tk.END, "No expenses recorded.\n")
            return
        
        for e in Expense.all_expenses:
            self.output_text.insert(tk.END, f"{e.title} | ₹{e.amount} | {e.category}\n")
        self.update_status(f"Showing {len(Expense.all_expenses)} expenses")
    
    def show_total(self):
        self.clear_output()
        total = sum(e.amount for e in Expense.all_expenses)
        self.output_text.insert(tk.END, f"Total Expenses: ₹{total:.2f}\n\n")
        
        # Category totals
        cat_totals = {}
        for e in Expense.all_expenses:
            cat_totals[e.category] = cat_totals.get(e.category, 0) + e.amount
        
        self.output_text.insert(tk.END, "By Category:\n")
        for cat, amt in cat_totals.items():
            self.output_text.insert(tk.END, f"  {cat}: ₹{amt:.2f}\n")
        
        self.update_status("Totals displayed")
    
    def filter_category(self):
        cat = self.category_entry.get().strip().lower()
        if not cat:
            messagebox.showwarning("Input", "Enter category to filter")
            return
        
        self.clear_output()
        found = False
        for e in Expense.all_expenses:
            if cat in e.category.lower():
                self.output_text.insert(tk.END, f"{e.title} | ₹{e.amount} | {e.category}\n")
                found = True
        
        if not found:
            self.output_text.insert(tk.END, "No expenses in this category.\n")
        self.update_status(f"Filtered by '{cat}'")
    
    def delete_expense(self):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Input", "Enter title to delete")
            return
        
        for e in Expense.all_expenses[:]:
            if e.title.lower() == title.lower():
                Expense.all_expenses.remove(e)
                save_data()
                self.update_status(f"Deleted: {title}")
                self.clear_entries()
                return
        
        messagebox.showinfo("Not Found", f"No expense with title '{title}'")
    
    def on_exit(self):
        save_data()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseGUI(root)
    root.mainloop()
