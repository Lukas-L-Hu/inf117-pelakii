import stripe
stripe.api_key = ""
import json

import address_ui
import tkinter as tk
import createMockAddress
import printRecieptConsole

# Comments that don't start with a space are removed Debug code
if __name__ == "__main__":
  root = tk.Tk()
  app = address_ui.UserAddress(root)
  root.mainloop()

  print(app.address_current)

  try:
    #createMockAddress.writeToJson

    # Reads the address dictionary
    '''
    with open('checkout.json', 'r') as json_file:
      curCheckout = json.load(json_file)'''


    # Creates a mock calculation for a snack box on the Stripe Pelakii server
    curCheckout = {"address":{"line1": app.address_current[0], "city": app.address_current[1], "state": app.address_current[2], "postal_code": app.address_current[3], "country": app.address_current[4]}, 
                   "cart": [{"amount": 515,"tax_code": "txcd_99999999","reference": "Pelakii Snack Box"}],
                   "shipping":300}

    calc_1 = stripe.tax.Calculation.create(
      currency="usd",
      line_items=curCheckout["cart"],
      shipping_cost={"amount": curCheckout["shipping"]},
      expand=["line_items"],
      customer_details={
        "address": curCheckout["address"],
        "address_source": "shipping",
      },
    )

    print(calc_1.tax_amount_inclusive)
  except stripe._error.customer_tax_location_invalid:

    # Calculates some numbers not given directly by stripe tax
    subtotal = calc_1.amount_total - calc_1.tax_amount_exclusive
    taxPercent = calc_1.tax_amount_exclusive/(subtotal-calc_1.shipping_cost["amount"])
    formatted_taxPercent = float("%.3f" % taxPercent)*100

    # Takes transaction info into a dictionary to be written to JSON file
    transactionDict= {
      "item cost": (subtotal-calc_1.shipping_cost["amount"]),
      "shipping": calc_1.shipping_cost["amount"],
      "subtotal":subtotal,
      "taxPercent":taxPercent,
      "taxAmnt": calc_1.tax_amount_exclusive,
      "total":calc_1.amount_total
      }
    
    printRecieptConsole.printReceipt(transactionDict)
    
    # Writes transaction to JSON file, to be sent to front end
    with open('receipt.json', 'w') as json_file:
        json.dump(transactionDict, json_file)

   



