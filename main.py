import address_ui
import stripe
import tkinter as tk


if __name__ == "__main__":
  root = tk.Tk()
  app = address_ui.UserAddress(root)
  root.mainloop()

  #stripe.tax.Settings.retrieve(stripe_account='{{CONNECTED_ACCOUNT_ID}}')
  try:
    stripe.tax.Settings.modify(
    defaults={"tax_code": "txcd_40070005", "tax_behavior": "inclusive"},
    head_office={"address": {"line1":"390 NE 191st St #8129","city":"Miami","state":"FL","postal_code":"33179","country": "US"}},
    )

    calc_1 = stripe.tax.Calculation.create(
      currency="usd",
      line_items=[{"amount": 1000, "reference": "L1"}],
      customer_details={
        "address": {
          "line1": app.address_current[0],
          "city": app.address_current[1],
          "state": app.address_current[2],
          "postal_code": app.address_current[3],
          "country": app.address_current[4],
        },
        "address_source": "shipping",
      },
    )
    print(calc_1.tax_amount_inclusive)
  except stripe._error.customer_tax_location_invalid:
    print("Invalid Address")

