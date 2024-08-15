class FarmIncomeOptimizer:
    def __init__(self):
        self.crops = {}
        self.livestock = {}
        self.total_income = 0
        self.total_expenses = 0

    def add_crop(self, name, quantity_kg, cost_per_kg, price_per_kg):
        total_income = quantity_kg * price_per_kg
        total_expense = quantity_kg * cost_per_kg
        net_income = total_income - total_expense

        self.crops[name] = {
            'quantity_kg': quantity_kg,
            'cost_per_kg': cost_per_kg,
            'price_per_kg': price_per_kg,
            'total_income': total_income,
            'total_expense': total_expense,
            'net_income': net_income
        }
        self.total_income += total_income
        self.total_expenses += total_expense

    def add_livestock(self, name, quantity_kg, cost_per_kg, price_per_kg):
        total_income = quantity_kg * price_per_kg
        total_expense = quantity_kg * cost_per_kg
        net_income = total_income - total_expense

        self.livestock[name] = {
            'quantity_kg': quantity_kg,
            'cost_per_kg': cost_per_kg,
            'price_per_kg': price_per_kg,
            'total_income': total_income,
            'total_expense': total_expense,
            'net_income': net_income
        }
        self.total_income += total_income
        self.total_expenses += total_expense

    def suggest_best_strategy(self):
        best_crop = max(self.crops.items(), key=lambda x: x[1]['net_income'])
        best_livestock = max(self.livestock.items(), key=lambda x: x[1]['net_income'])

        print(f"\nBest Crop to Grow: {best_crop[0]} - Net Income: ₹{best_crop[1]['net_income']:.2f}")
        print(f"Best Livestock to Raise: {best_livestock[0]} - Net Income: ₹{best_livestock[1]['net_income']:.2f}")
        print(f"\nOverall Total Income: ₹{self.total_income:.2f}")
        print(f"Overall Total Expenses: ₹{self.total_expenses:.2f}")
        print(f"Overall Net Income: ₹{self.total_income - self.total_expenses:.2f}")

    def show_summary(self):
        print("\nFarm Summary:")
        print("Crops:")
        for crop, details in self.crops.items():
            print(f" - {crop}: {details['quantity_kg']} kg, Net Income: ₹{details['net_income']:.2f}")
        print("Livestock:")
        for animal, details in self.livestock.items():
            print(f" - {animal}: {details['quantity_kg']} kg, Net Income: ₹{details['net_income']:.2f}")

        self.suggest_best_strategy()


def main():
    farm_optimizer = FarmIncomeOptimizer()

    while True:
        print("\n1. Add Crop")
        print("2. Add Livestock")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter crop name: ")
            quantity_kg = int(input(f"Enter quantity of {name} (in kg): "))
            cost_per_kg = float(input(f"Enter cost per kg of {name} (in ₹): "))
            price_per_kg = float(input(f"Enter selling price per kg of {name} (in ₹): "))
            farm_optimizer.add_crop(name, quantity_kg, cost_per_kg, price_per_kg)

        elif choice == '2':
            name = input("Enter livestock name: ")
            quantity_kg = int(input(f"Enter quantity of {name} (in kg): "))
            cost_per_kg = float(input(f"Enter cost per kg of {name} (in ₹): "))
            price_per_kg = float(input(f"Enter selling price per kg of {name} (in ₹): "))
            farm_optimizer.add_livestock(name, quantity_kg, cost_per_kg, price_per_kg)

        elif choice == '3':
            farm_optimizer.show_summary()

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
