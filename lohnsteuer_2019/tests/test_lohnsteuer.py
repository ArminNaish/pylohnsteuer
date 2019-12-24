import sys
import pytest

from decimal import Decimal
from ..lohnsteuer import calculate_wage_tax

# todo: check code coverage
# todo: implement msonst
# todo: add "besondere Jahreslohnsteuer" for Steuerklasse 1-6


@pytest.mark.parametrize('re4, expected', [
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
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 1,              # Steuerklasse
        'KRV': 0,               # Gesetzliche RV -> BBG West
        'PKV': 0,               # gesetzlich krankenversicherte Arbeitnehmer
        'KVZ': Decimal(0.90),   # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,               # Zuschlag zur Pflegeversicherung für Kinderlose
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000), Decimal(0)),
    (Decimal(750000), Decimal(0)),
    (Decimal(1000000), Decimal(0)),
    (Decimal(1250000), Decimal(0)),
    (Decimal(1500000), Decimal(300)),
    (Decimal(1750000), Decimal(36400)),
    (Decimal(2000000), Decimal(84500)),
    (Decimal(2250000), Decimal(137700)),
    (Decimal(2500000), Decimal(190500)),
    (Decimal(2750000), Decimal(245200)),
    (Decimal(3000000), Decimal(301800)),
    (Decimal(3250000), Decimal(360300)),
    (Decimal(3500000), Decimal(420700)),
    (Decimal(3750000), Decimal(483000)),
    (Decimal(4000000), Decimal(547300)),
    (Decimal(4250000), Decimal(613400)),
    (Decimal(4500000), Decimal(681400)),
    (Decimal(4750000), Decimal(751400)),
    (Decimal(5000000), Decimal(823200)),
    (Decimal(5250000), Decimal(897000)),
    (Decimal(5500000), Decimal(974400)),
    (Decimal(5750000), Decimal(1060500)),
    (Decimal(6000000), Decimal(1148800)),
    (Decimal(6250000), Decimal(1239500)),
    (Decimal(6500000), Decimal(1332500)),
    (Decimal(6750000), Decimal(1427800)),
    (Decimal(7000000), Decimal(1525100)),
    (Decimal(7250000), Decimal(1622700)),
    (Decimal(7500000), Decimal(1720300)),
    (Decimal(7750000), Decimal(1817900)),
    (Decimal(8000000), Decimal(1915400)),
    (Decimal(8250000), Decimal(2019300)),
    (Decimal(8500000), Decimal(2124300)),
    (Decimal(8750000), Decimal(2229300)),
    (Decimal(9000000), Decimal(2334300))
])
def test_lohnsteuer_steuerklasse_2(re4, expected):
    # arrange
    inputs = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 2,              # Steuerklasse
        'KRV': 0,               # Gesetzliche RV -> BBG West
        'PKV': 0,               # gesetzlich krankenversicherte Arbeitnehmer
        'KVZ': Decimal(0.90),   # Zusatzbeitragssatz Krankenkasse
        'PVZ': 0,               # Zuschlag zur Pflegeversicherung für Kinderlose
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(inputs)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4,expected', [
    (Decimal(500000), Decimal(0)),
    (Decimal(750000), Decimal(0)),
    (Decimal(1000000), Decimal(0)),
    (Decimal(1250000), Decimal(0)),
    (Decimal(1500000), Decimal(0)),
    (Decimal(1750000), Decimal(0)),
    (Decimal(2000000), Decimal(0)),
    (Decimal(2250000), Decimal(0)),
    (Decimal(2500000), Decimal(12400)),
    (Decimal(2750000), Decimal(49400)),
    (Decimal(3000000), Decimal(91800)),
    (Decimal(3250000), Decimal(139600)),
    (Decimal(3500000), Decimal(187200)),
    (Decimal(3750000), Decimal(237600)),
    (Decimal(4000000), Decimal(289000)),
    (Decimal(4250000), Decimal(341400)),
    (Decimal(4500000), Decimal(394800)),
    (Decimal(4750000), Decimal(449200)),
    (Decimal(5000000), Decimal(504400)),
    (Decimal(5250000), Decimal(560600)),
    (Decimal(5500000), Decimal(619200)),
    (Decimal(5750000), Decimal(683800)),
    (Decimal(6000000), Decimal(749600)),
    (Decimal(6250000), Decimal(816400)),
    (Decimal(6500000), Decimal(884600)),
    (Decimal(6750000), Decimal(953800)),
    (Decimal(7000000), Decimal(1024200)),
    (Decimal(7250000), Decimal(1095800)),
    (Decimal(7500000), Decimal(1168400)),
    (Decimal(7750000), Decimal(1242400)),
    (Decimal(8000000), Decimal(1317600)),
    (Decimal(8250000), Decimal(1398600)),
    (Decimal(8500000), Decimal(1482200)),
    (Decimal(8750000), Decimal(1566800)),
    (Decimal(9000000), Decimal(1653000))
])
def test_lohnsteuer_steuerklasse_3(re4, expected):
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 3,              # Steuerklasse
        'KRV': 0,               # Gesetzliche RV -> BBG West
        'PKV': 0,               # gesetzlich krankenversicherte Arbeitnehmer
        'KVZ': Decimal(0.90),   # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,               # Zuschlag zur Pflegeversicherung für Kinderlose
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
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
def test_lohnsteuer_steuerklasse_4(re4, expected):
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 4,              # Steuerklasse
        'KRV': 0,               # Gesetzliche RV -> BBG West
        'PKV': 0,               # gesetzlich krankenversicherte Arbeitnehmer
        'KVZ': Decimal(0.90),   # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,               # Zuschlag zur Pflegeversicherung für Kinderlose
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000),  Decimal(42100)),
    (Decimal(750000),  Decimal(70400)),
    (Decimal(1000000), Decimal(98700)),
    (Decimal(1250000), Decimal(127100)),
    (Decimal(1500000), Decimal(168400)),
    (Decimal(1750000), Decimal(261800)),
    (Decimal(2000000), Decimal(359400)),
    (Decimal(2250000), Decimal(449600)),
    (Decimal(2500000), Decimal(525200)),
    (Decimal(2750000), Decimal(600400)),
    (Decimal(3000000), Decimal(679400)),
    (Decimal(3250000), Decimal(762000)),
    (Decimal(3500000), Decimal(848600)),
    (Decimal(3750000), Decimal(936500)),
    (Decimal(4000000), Decimal(1024300)),
    (Decimal(4250000), Decimal(1112200)),
    (Decimal(4500000), Decimal(1200100)),
    (Decimal(4750000), Decimal(1288000)),
    (Decimal(5000000), Decimal(1375900)),
    (Decimal(5250000), Decimal(1463800)),
    (Decimal(5500000), Decimal(1553800)),
    (Decimal(5750000), Decimal(1651400)),
    (Decimal(6000000), Decimal(1749000)),
    (Decimal(6250000), Decimal(1846600)),
    (Decimal(6500000), Decimal(1944100)),
    (Decimal(6750000), Decimal(2041700)),
    (Decimal(7000000), Decimal(2139300)),
    (Decimal(7250000), Decimal(2236900)),
    (Decimal(7500000), Decimal(2334400)),
    (Decimal(7750000), Decimal(2432000)),
    (Decimal(8000000), Decimal(2529600)),
    (Decimal(8250000), Decimal(2633400)),
    (Decimal(8500000), Decimal(2738400)),
    (Decimal(8750000), Decimal(2843400)),
    (Decimal(9000000), Decimal(2948400))
])
def test_lohnsteuer_steuerklasse_5(re4, expected):
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 5,              # Steuerklasse
        'KRV': 0,               # Gesetzliche RV -> BBG West
        'PKV': 0,               # gesetzlich krankenversicherte Arbeitnehmer
        'KVZ': Decimal(0.90),   # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,               # Zuschlag zur Pflegeversicherung für Kinderlose
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000),  Decimal(56600)),
    (Decimal(750000),  Decimal(84900)),
    (Decimal(1000000), Decimal(113300)),
    (Decimal(1250000), Decimal(141600)),
    (Decimal(1500000), Decimal(211900)),
    (Decimal(1750000), Decimal(305300)),
    (Decimal(2000000), Decimal(402900)),
    (Decimal(2250000), Decimal(488800)),
    (Decimal(2500000), Decimal(562000)),
    (Decimal(2750000), Decimal(639000)),
    (Decimal(3000000), Decimal(719800)),
    (Decimal(3250000), Decimal(804400)),
    (Decimal(3500000), Decimal(892100)),
    (Decimal(3750000), Decimal(980000)),
    (Decimal(4000000), Decimal(1067800)),
    (Decimal(4250000), Decimal(1155700)),
    (Decimal(4500000), Decimal(1243600)),
    (Decimal(4750000), Decimal(1331500)),
    (Decimal(5000000), Decimal(1419400)),
    (Decimal(5250000), Decimal(1507300)),
    (Decimal(5500000), Decimal(1597300)),
    (Decimal(5750000), Decimal(1694900)),
    (Decimal(6000000), Decimal(1792500)),
    (Decimal(6250000), Decimal(1890100)),
    (Decimal(6500000), Decimal(1987600)),
    (Decimal(6750000), Decimal(2085200)),
    (Decimal(7000000), Decimal(2182800)),
    (Decimal(7250000), Decimal(2280400)),
    (Decimal(7500000), Decimal(2377900)),
    (Decimal(7750000), Decimal(2475500)),
    (Decimal(8000000), Decimal(2573100)),
    (Decimal(8250000), Decimal(2676900)),
    (Decimal(8500000), Decimal(2781900)),
    (Decimal(8750000), Decimal(2886900)),
    (Decimal(9000000), Decimal(2991900))
])
def test_lohnsteuer_steuerklasse_6(re4, expected):
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 6,              # Steuerklasse
        'KRV': 0,               # Gesetzliche RV -> BBG West
        'PKV': 0,               # gesetzlich krankenversicherte Arbeitnehmer
        'KVZ': Decimal(0.90),   # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,               # Zuschlag zur Pflegeversicherung für Kinderlose
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected