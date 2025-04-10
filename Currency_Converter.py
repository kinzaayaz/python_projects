print("Welcome to Simple Currency Converter")
print("Available currencies: USD, CAD, EUR")

amount=int(input("Enter the amount: "))
source_currency=input("Source currency(USD, CAD, EUR): ").upper()
target_currency=input("Taregt currency(USD, CAD, EUR): ").upper()

if source_currency=="USD" and target_currency=="CAD":
    cad_amount = amount * 1.42
    print(f'{amount} USD = {cad_amount} CAD')
elif source_currency=="USD" and target_currency=="EUR":
    eur_amount=amount*0.92
    print(f'{amount} USD = {eur_amount} EUR')
    
elif source_currency=="CAD" and target_currency=="USD":
    usd_amount=amount*0.74
    print(f'{amount} CAD = {usd_amount} USD')
elif source_currency=="CAD" and target_currency=="EUR":
    eur_amount=amount*0.64
    print(f'{amount} CAD = {eur_amount} EUR')
    
elif source_currency=="EUR" and target_currency=="USD":
    usd_amount=amount*1.10
    print(f'{amount} EUR = {usd_amount} USD')
elif source_currency=="EUR" and target_currency=="CAD":
    cad_amount=amount*1.55
    print(f'{amount} EUR = {cad_amount} CAD')
elif source_currency==source_currency:
    print("No conversion needed")
else:
    ("currency conversion not available")

