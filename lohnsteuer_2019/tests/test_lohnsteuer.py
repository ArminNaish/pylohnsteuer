import pytest

from decimal import Decimal
from ..parameters import wage_tax_inputs, wage_tax_internals, wage_tax_outputs
from ..lohnsteuer import calculate_wage_tax

# todo: check code coverage
# todo: add "allgemeine Jahreslohnsteuer" for Steuerklasse 2-6
# todo: add "besondere Jahreslohnsteuer" for Steuerklasse 1-6

@pytest.mark.parametrize('re4,expected', [
    (Decimal(500000), Decimal(0)),
    (Decimal(750000), Decimal(0)),
    (Decimal(1000000), Decimal(0)),
    (Decimal(1250000), Decimal(0)),
    (Decimal(1500000), Decimal(30700)),
    (Decimal(1750000), Decimal(75100)),
    (Decimal(2000000), Decimal(130400)),
    (Decimal(2250000), Decimal(184200)),
    (Decimal(2500000), Decimal(238500)),
    (Decimal(2750000), Decimal(294700)),
    (Decimal(3000000), Decimal(352800)),
    (Decimal(3250000), Decimal(412800)),
    (Decimal(3500000), Decimal(474700)),
    (Decimal(3750000), Decimal(538500)),
    (Decimal(4000000), Decimal(604100)),
    (Decimal(4250000), Decimal(671700)),
    (Decimal(4500000), Decimal(741200)),
    (Decimal(4750000), Decimal(812500)),
    (Decimal(5000000), Decimal(885700)),
    (Decimal(5250000), Decimal(960900)),
    (Decimal(5500000), Decimal(1039800)),
    (Decimal(5750000), Decimal(1127600)),
    (Decimal(6000000), Decimal(1217700)),
    (Decimal(6250000), Decimal(1310200)),
    (Decimal(6500000), Decimal(1405000)),
    (Decimal(6750000), Decimal(1502000)),
    (Decimal(7000000), Decimal(1599600)),
    (Decimal(7250000), Decimal(1697100)),
    (Decimal(7500000), Decimal(1794700)),
    (Decimal(7750000), Decimal(1892300)),
    (Decimal(8000000), Decimal(1989900)),
    (Decimal(8250000), Decimal(2093700)),
    (Decimal(8500000), Decimal(2198700)),
    (Decimal(8750000), Decimal(2303700)),
    (Decimal(9000000), Decimal(2408700))
])
def test_lohnsteuer_steuerklasse_1(re4, expected):
    # arrange
    wage_tax_inputs.update({
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 1,              # Steuerklasse
        'KRV': 0,               # Gesetzliche RV -> BBG West
        'PKV': 0,               # gesetzlich krankenversicherte Arbeitnehmer
        'KVZ': Decimal(0.90),   # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,               # Zuschlag zur Pflegeversicherung für Kinderlose
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    })
    # act
    calculate_wage_tax(wage_tax_inputs, wage_tax_internals, wage_tax_outputs)
    # assert
    assert wage_tax_outputs['LSTLZZ'] == expected