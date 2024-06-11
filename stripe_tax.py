#This file serves as a way to modifu stripe settings via code

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = ""

print(stripe.tax.Settings.retrieve())

stripe.tax.Settings.modify(
defaults={"tax_code": "txcd_40070005", "tax_behavior": "inclusive"},
head_office={"address": {"line1":"390 NE 191st St #8129","city":"Miami","state":"FL","postal_code":"33179","country": "US"}},
)

'''
stripe.tax.Transaction.create_from_calculation(
  calculation="{{TAX_CALCULATION}}",
  reference='{{PAYMENT_INTENT_ID}}',
  expand=["line_items"],
)

stripe.PaymentIntent.modify(
  '{{PAYMENT_INTENT_ID}}',
  metadata={"tax_transaction": "{{TAX_TRANSACTION}}"},
)

stripe.tax.customer_tax_location_invalid()
'''