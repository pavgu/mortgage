import numpy_financial as npf

npf.pmt(0.036/12, 12*10, 250000)
npf.ppmt(0.036/12, 0, 12*10, 250000)
npf.ipmt(0.036/12, 1, 12*10, 250000)


import numpy as np

principal = 500000.00
years = 20
payments_per_year = 12
total_payments = years * payments_per_year
interest_rate_per_year = 0.036
interest_rate_per_payment = interest_rate_per_year/payments_per_year


per = np.arange(total_payments) + 1
ipmt = npf.ipmt(interest_rate_per_payment, per, total_payments, principal)
ppmt = npf.ppmt(interest_rate_per_payment, per, total_payments, principal)
pmt = npf.pmt(interest_rate_per_payment, total_payments, principal)
np.allclose(ipmt + ppmt, pmt)

//fmt_header = '{0:2s} {1:22s} {2:11s} {3:23s}'
//print(fmt_header.format('#','| Principal repayment ','| Interest ','| Remaining principal |'))
//print('------------------------------------------------------------------')

//fmt = '{0:2d} {1:22.2f} {2:11.2f} {3:23.2f}'

fmt = '{0:2d} {1:8.2f} {2:8.2f} {3:8.2f}'
for payment in per:
	index = payment - 1
	principal = principal + ppmt[index]
	print(fmt.format(payment, ppmt[index], ipmt[index], principal))
