class RentalProperty:
    def __init__(self, initial_investment, total_property_income_monthly, total_property_expenses_monthly):
        self.initial_investment = initial_investment
        self.total_property_income_monthly = total_property_income_monthly
        self.total_property_expenses_monthly = total_property_expenses_monthly

    def calculate_cash_flow(self):
        cash_flow = self.total_property_income_monthly - self.total_property_expenses_monthly
        return cash_flow

    def calculate_cash_on_cash_roi(self):
        annual_cash_flow = self.calculate_cash_flow() * 12
        cash_on_cash_roi = (annual_cash_flow / self.initial_investment) * 100
        return cash_on_cash_roi

def main():
    initial_investment = float(input("Enter the initial investment into the property: "))
    total_property_income_monthly = float(input("Enter the total property income per month: "))
    total_property_expenses_monthly = float(input("Enter the total property expenses per month: "))
    
    property_roi = RentalProperty(initial_investment, total_property_income_monthly, total_property_expenses_monthly)
    cash_flow = property_roi.calculate_cash_flow()
    cash_on_cash_roi = property_roi.calculate_cash_on_cash_roi()

    print(f"Total Cash Flow per Month: ${cash_flow:.2f}")
    print(f"Cash-on-Cash ROI: {cash_on_cash_roi:.2f}%")

if __name__ == "__main__":
    main()