import csv
class SalesPerson:
    def __init__(self, name, sales):
        self.name = name
        self.sales = sales
        self.commission = 0
        self.bonus = 0

    def calculate_commission(self):
        if self.sales > 500000:
            self.commission = self.sales * 0.30
            self.bonus = 25000
        elif 350000 <= self.sales <= 499999:
            self.commission = self.sales * 0.20
        elif 200000 <= self.sales <= 349999:
            self.commission = self.sales * 0.10
        elif 50000 <= self.sales <= 199999:
            self.commission = self.sales * 0.05
        else:
            self.commission = 0

    def total_earned(self):
        return self.commission + self.bonus

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Total Sales: Ksh {self.sales:,.2f}")
        print(f"Commission Earned: Ksh {self.commission:,.2f}")
        if self.bonus > 0:
            print(f"Bonus: Ksh {self.bonus:,.2f}")
        print(f"Total Payment: Ksh {self.total_earned():,.2f}")
        print("-" * 40)


class PayrollSystem:
    def __init__(self):
        self.salespeople = []

    def add_salesperson(self, salesperson):
        self.salespeople.append(salesperson)

    def calculate_all_commissions(self):
        for sp in self.salespeople:
            sp.calculate_commission()

    def display_all_info(self):
        total_commission = 0
        print("\n--- Payroll Report ---\n")
        for sp in self.salespeople:
            sp.display_info()
            total_commission += sp.commission
        print(f"Total Commission Paid to All Salespersons: Ksh {total_commission:,.2f}")


# ----- Security -----
def authenticate():
    correct_password = "Cosumetke"
    for attempt in range(3):
        password = input("Enter system password: ")
        if password == correct_password:
            print("Access Granted.\n")
            return True
        else:
            print("Incorrect password.")
    print("Access Denied. Too many failed attempts.")
    return False


if authenticate():
    def load_sales_from_csv(filename):
        payroll = PayrollSystem()
        try:
            with open(filename, newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print("🕵️ Raw row keys:", list(row.keys()))
                    name = row.get('Name ') or row.get('Name') or list(row.values())[0]
                    sales = float(row['Sales'])
                    sp = SalesPerson(name, sales)
                    payroll.add_salesperson(sp)
            return payroll
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
        except ValueError:
            print("Error: Ensure all sales values are numeric in the CSV file.")
            return None

    filename = input("Enter CSV filename: ")
    payroll = load_sales_from_csv(filename)
    if payroll:
        payroll.calculate_all_commissions()
        payroll.display_all_info()
