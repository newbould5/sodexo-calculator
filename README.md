# sodexo-calculator
Calculate how much you spent after a given transaction.

## What does it do

These scripts allow you to calculate how much you spent on your sodexo lunch pass card. It will download an export of all your transactions and then calculate your expenses.

## How does it work

First off all you will need to complete your credentials in config.py.

```
email='example@test.com'
password='test'
```

The script takes one argument, the transaction up until you want to calculate. Execute the script like so:

```
python calculator.py 1234
```


## Dependencies

mechanize
