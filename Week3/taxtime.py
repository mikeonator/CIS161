#Michael Audi - Week 3 Extra Credit - Tax Table Calculation

tax_table = {
    0000.00:0.1,
    11600.01:0.12,
    47150.01:0.22,
    100525.01:0.24,
    191950.01:0.32,
    243725.01:0.35,
    609350.01:0.37
}

def tax_time(hourly_wage:float):
    gross_annual = (hourly_wage * 40) * 50
    tax_rate = 0.1
    for key, value in tax_table.items():
        if gross_annual >= key:
            tax_rate = value
    get_taxed = tax_rate * gross_annual
    after_tax = gross_annual - get_taxed
    return gross_annual, get_taxed, after_tax
