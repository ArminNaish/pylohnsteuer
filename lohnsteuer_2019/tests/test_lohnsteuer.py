import sys
import pytest

from decimal import Decimal
from ..lohnsteuer import calculate_wage_tax


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
    '''
    Allgemeine maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Allgemeine Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    allen Sozialversicherungszweigen versichert ist.

    Berechnet für die Beitragsbemessungsgrenzen West
    Berechnet mit den Merkern KRV und PKV = 0 sowie KVZ = 0,90
    In der Steuerklasse II gilt PVZ = 0, in den anderen Steuerklassen gilt PVZ = 1

    Steuerklasse I
    '''
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
    '''
    Allgemeine maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Allgemeine Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    allen Sozialversicherungszweigen versichert ist.

    Berechnet für die Beitragsbemessungsgrenzen West
    Berechnet mit den Merkern KRV und PKV = 0 sowie KVZ = 0,90
    In der Steuerklasse II gilt PVZ = 0, in den anderen Steuerklassen gilt PVZ = 1

    Steuerklasse II
    '''
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
    '''
    Allgemeine maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Allgemeine Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    allen Sozialversicherungszweigen versichert ist.

    Berechnet für die Beitragsbemessungsgrenzen West
    Berechnet mit den Merkern KRV und PKV = 0 sowie KVZ = 0,90
    In der Steuerklasse II gilt PVZ = 0, in den anderen Steuerklassen gilt PVZ = 1

    Steuerklasse III
    '''
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
    '''
    Allgemeine maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Allgemeine Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    allen Sozialversicherungszweigen versichert ist.

    Berechnet für die Beitragsbemessungsgrenzen West
    Berechnet mit den Merkern KRV und PKV = 0 sowie KVZ = 0,90
    In der Steuerklasse II gilt PVZ = 0, in den anderen Steuerklassen gilt PVZ = 1

    Steuerklasse IV
    '''
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
    '''
    Allgemeine maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Allgemeine Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    allen Sozialversicherungszweigen versichert ist.

    Berechnet für die Beitragsbemessungsgrenzen West
    Berechnet mit den Merkern KRV und PKV = 0 sowie KVZ = 0,90
    In der Steuerklasse II gilt PVZ = 0, in den anderen Steuerklassen gilt PVZ = 1

    Steuerklasse V
    '''
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
    '''
    Allgemeine maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Allgemeine Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    allen Sozialversicherungszweigen versichert ist.

    Berechnet für die Beitragsbemessungsgrenzen West
    Berechnet mit den Merkern KRV und PKV = 0 sowie KVZ = 0,90
    In der Steuerklasse II gilt PVZ = 0, in den anderen Steuerklassen gilt PVZ = 1

    Steuerklasse VI
    '''
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
    

@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000),  Decimal(0)),
    (Decimal(750000),  Decimal(0)),
    (Decimal(1000000), Decimal(0)),
    (Decimal(1250000), Decimal(11700)),
    (Decimal(1500000), Decimal(50700)),
    (Decimal(1750000), Decimal(104000)),
    (Decimal(2000000), Decimal(165600)),
    (Decimal(2250000), Decimal(229900)),
    (Decimal(2500000), Decimal(296900)),
    (Decimal(2750000), Decimal(366600)),
    (Decimal(3000000), Decimal(439000)),
    (Decimal(3250000), Decimal(514200)),
    (Decimal(3500000), Decimal(592000)),
    (Decimal(3750000), Decimal(672500)),
    (Decimal(4000000), Decimal(755700)),
    (Decimal(4250000), Decimal(841700)),
    (Decimal(4500000), Decimal(930300)),
    (Decimal(4750000), Decimal(1021600)),
    (Decimal(5000000), Decimal(1115700)),
    (Decimal(5250000), Decimal(1212400)),
    (Decimal(5500000), Decimal(1311800)),
    (Decimal(5750000), Decimal(1414000)),
    (Decimal(6000000), Decimal(1518500)),
    (Decimal(6250000), Decimal(1623500)),
    (Decimal(6500000), Decimal(1728500)),
    (Decimal(6750000), Decimal(1833500)),
    (Decimal(7000000), Decimal(1938500)),
    (Decimal(7250000), Decimal(2043500)),
    (Decimal(7500000), Decimal(2148500)),
    (Decimal(7750000), Decimal(2253500)),
    (Decimal(8000000), Decimal(2358500)),
    (Decimal(8250000), Decimal(2463500)),
    (Decimal(8500000), Decimal(2568500)),
    (Decimal(8750000), Decimal(2673500)),
    (Decimal(9000000), Decimal(2778500))
])
def test_special_lohnsteuer_steuerklasse_1(re4, expected):
    '''
    Besondere maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Besondere Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    keinem Sozialversicherungszweig versichert und privat kranken- und pflegeversichert ist
    sowie dem Arbeitgeber keine Basiskranken- und Pflege-Pflichtversicherungsbeiträge
    mitgeteilt hat.

    Berechnet mit den Merkern KRV = 2 und PKV = 1; PKPV = 0

    Steuerklasse I
    '''
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 1,              # Steuerklasse
        'KRV': 2,               # in keinem Sozialversicherungszweig versichert
        'PKV': 1,               # privat krankenversicherte Arbeitnehmer
        'PKPV': 0,              # private Basiskranken- bzw. Pflege-Pflichtversicherung 
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000),  Decimal(0)),
    (Decimal(750000),  Decimal(0)),
    (Decimal(1000000), Decimal(0)),
    (Decimal(1250000), Decimal(0)),
    (Decimal(1500000), Decimal(16300)),
    (Decimal(1750000), Decimal(60700)),
    (Decimal(2000000), Decimal(118300)),
    (Decimal(2250000), Decimal(180600)),
    (Decimal(2500000), Decimal(245500)),
    (Decimal(2750000), Decimal(313200)),
    (Decimal(3000000), Decimal(383500)),
    (Decimal(3250000), Decimal(456600)),
    (Decimal(3500000), Decimal(532300)),
    (Decimal(3750000), Decimal(610800)),
    (Decimal(4000000), Decimal(692000)),
    (Decimal(4250000), Decimal(775800)),
    (Decimal(4500000), Decimal(862400)),
    (Decimal(4750000), Decimal(951700)),
    (Decimal(5000000), Decimal(1043600)),
    (Decimal(5250000), Decimal(1138300)),
    (Decimal(5500000), Decimal(1235700)),
    (Decimal(5750000), Decimal(1335800)),
    (Decimal(6000000), Decimal(1438600)),
    (Decimal(6250000), Decimal(1543400)),
    (Decimal(6500000), Decimal(1648400)),
    (Decimal(6750000), Decimal(1753400)),
    (Decimal(7000000), Decimal(1858400)),
    (Decimal(7250000), Decimal(1963400)),
    (Decimal(7500000), Decimal(2068400)),
    (Decimal(7750000), Decimal(2173400)),
    (Decimal(8000000), Decimal(2278400)),
    (Decimal(8250000), Decimal(2383400)),
    (Decimal(8500000), Decimal(2488400)),
    (Decimal(8750000), Decimal(2593400)),
    (Decimal(9000000), Decimal(2698400))
])
def test_special_lohnsteuer_steuerklasse_2(re4, expected):
    '''
    Besondere maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Besondere Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    keinem Sozialversicherungszweig versichert und privat kranken- und pflegeversichert ist
    sowie dem Arbeitgeber keine Basiskranken- und Pflege-Pflichtversicherungsbeiträge
    mitgeteilt hat.

    Berechnet mit den Merkern KRV = 2 und PKV = 1; PKPV = 0

    Steuerklasse II
    '''
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 2,              # Steuerklasse
        'KRV': 2,               # in keinem Sozialversicherungszweig versichert
        'PKV': 1,               # privat krankenversicherte Arbeitnehmer
        'PKPV': 0,              # private Basiskranken- bzw. Pflege-Pflichtversicherung 
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000),  Decimal(0)),
    (Decimal(750000),  Decimal(0)),
    (Decimal(1000000), Decimal(0)),
    (Decimal(1250000), Decimal(0)),
    (Decimal(1500000), Decimal(0)),
    (Decimal(1750000), Decimal(0)),
    (Decimal(2000000), Decimal(0)),
    (Decimal(2250000), Decimal(6000)),
    (Decimal(2500000), Decimal(40000)),
    (Decimal(2750000), Decimal(84600)),
    (Decimal(3000000), Decimal(135200)),
    (Decimal(3250000), Decimal(192000)),
    (Decimal(3500000), Decimal(252600)),
    (Decimal(3750000), Decimal(314400)),
    (Decimal(4000000), Decimal(377800)),
    (Decimal(4250000), Decimal(442400)),
    (Decimal(4500000), Decimal(508400)),
    (Decimal(4750000), Decimal(575600)),
    (Decimal(5000000), Decimal(644400)),
    (Decimal(5250000), Decimal(714400)),
    (Decimal(5500000), Decimal(785800)),
    (Decimal(5750000), Decimal(858600)),
    (Decimal(6000000), Decimal(932600)),
    (Decimal(6250000), Decimal(1008000)),
    (Decimal(6500000), Decimal(1084800)),
    (Decimal(6750000), Decimal(1163000)),
    (Decimal(7000000), Decimal(1242400)),
    (Decimal(7250000), Decimal(1323400)),
    (Decimal(7500000), Decimal(1405600)),
    (Decimal(7750000), Decimal(1489000)),
    (Decimal(8000000), Decimal(1574000)),
    (Decimal(8250000), Decimal(1660200)),
    (Decimal(8500000), Decimal(1747800)),
    (Decimal(8750000), Decimal(1836800)),
    (Decimal(9000000), Decimal(1927000))
])
def test_special_lohnsteuer_steuerklasse_3(re4, expected):
    '''
    Besondere maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Besondere Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    keinem Sozialversicherungszweig versichert und privat kranken- und pflegeversichert ist
    sowie dem Arbeitgeber keine Basiskranken- und Pflege-Pflichtversicherungsbeiträge
    mitgeteilt hat.

    Berechnet mit den Merkern KRV = 2 und PKV = 1; PKPV = 0

    Steuerklasse III
    '''
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 3,              # Steuerklasse
        'KRV': 2,               # in keinem Sozialversicherungszweig versichert
        'PKV': 1,               # privat krankenversicherte Arbeitnehmer
        'PKPV': 0,              # private Basiskranken- bzw. Pflege-Pflichtversicherung 
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000),  Decimal(0)),
    (Decimal(750000),  Decimal(0)),
    (Decimal(1000000), Decimal(0)),
    (Decimal(1250000), Decimal(11700)),
    (Decimal(1500000), Decimal(50700)),
    (Decimal(1750000), Decimal(104000)),
    (Decimal(2000000), Decimal(165600)),
    (Decimal(2250000), Decimal(229900)),
    (Decimal(2500000), Decimal(296900)),
    (Decimal(2750000), Decimal(366600)),
    (Decimal(3000000), Decimal(439000)),
    (Decimal(3250000), Decimal(514200)),
    (Decimal(3500000), Decimal(592000)),
    (Decimal(3750000), Decimal(672500)),
    (Decimal(4000000), Decimal(755700)),
    (Decimal(4250000), Decimal(841700)),
    (Decimal(4500000), Decimal(930300)),
    (Decimal(4750000), Decimal(1021600)),
    (Decimal(5000000), Decimal(1115700)),
    (Decimal(5250000), Decimal(1212400)),
    (Decimal(5500000), Decimal(1311800)),
    (Decimal(5750000), Decimal(1414000)),
    (Decimal(6000000), Decimal(1518500)),
    (Decimal(6250000), Decimal(1623500)),
    (Decimal(6500000), Decimal(1728500)),
    (Decimal(6750000), Decimal(1833500)),
    (Decimal(7000000), Decimal(1938500)),
    (Decimal(7250000), Decimal(2043500)),
    (Decimal(7500000), Decimal(2148500)),
    (Decimal(7750000), Decimal(2253500)),
    (Decimal(8000000), Decimal(2358500)),
    (Decimal(8250000), Decimal(2463500)),
    (Decimal(8500000), Decimal(2568500)),
    (Decimal(8750000), Decimal(2673500)),
    (Decimal(9000000), Decimal(2778500))
])
def test_special_lohnsteuer_steuerklasse_4(re4, expected):
    '''
    Besondere maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Besondere Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    keinem Sozialversicherungszweig versichert und privat kranken- und pflegeversichert ist
    sowie dem Arbeitgeber keine Basiskranken- und Pflege-Pflichtversicherungsbeiträge
    mitgeteilt hat.

    Berechnet mit den Merkern KRV = 2 und PKV = 1; PKPV = 0

    Steuerklasse IV
    '''
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 4,              # Steuerklasse
        'KRV': 2,               # in keinem Sozialversicherungszweig versichert
        'PKV': 1,               # privat krankenversicherte Arbeitnehmer
        'PKPV': 0,              # private Basiskranken- bzw. Pflege-Pflichtversicherung 
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000),  Decimal(47000)),
    (Decimal(750000),  Decimal(77800)),
    (Decimal(1000000), Decimal(108600)),
    (Decimal(1250000), Decimal(139400)),
    (Decimal(1500000), Decimal(213000)),
    (Decimal(1750000), Decimal(313800)),
    (Decimal(2000000), Decimal(418800)),
    (Decimal(2250000), Decimal(513800)),
    (Decimal(2500000), Decimal(603400)),
    (Decimal(2750000), Decimal(698200)),
    (Decimal(3000000), Decimal(798600)),
    (Decimal(3250000), Decimal(903300)),
    (Decimal(3500000), Decimal(1008300)),
    (Decimal(3750000), Decimal(1113300)),
    (Decimal(4000000), Decimal(1218300)),
    (Decimal(4250000), Decimal(1323300)),
    (Decimal(4500000), Decimal(1428300)),
    (Decimal(4750000), Decimal(1533300)),
    (Decimal(5000000), Decimal(1638300)),
    (Decimal(5250000), Decimal(1743300)),
    (Decimal(5500000), Decimal(1848300)),
    (Decimal(5750000), Decimal(1953300)),
    (Decimal(6000000), Decimal(2058300)),
    (Decimal(6250000), Decimal(2163300)),
    (Decimal(6500000), Decimal(2268300)),
    (Decimal(6750000), Decimal(2373300)),
    (Decimal(7000000), Decimal(2478300)),
    (Decimal(7250000), Decimal(2583300)),
    (Decimal(7500000), Decimal(2688300)),
    (Decimal(7750000), Decimal(2793300)),
    (Decimal(8000000), Decimal(2898300)),
    (Decimal(8250000), Decimal(3003300)),
    (Decimal(8500000), Decimal(3108300)),
    (Decimal(8750000), Decimal(3213300)),
    (Decimal(9000000), Decimal(3318300))
])
def test_special_lohnsteuer_steuerklasse_5(re4, expected):
    '''
    Besondere maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Besondere Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    keinem Sozialversicherungszweig versichert und privat kranken- und pflegeversichert ist
    sowie dem Arbeitgeber keine Basiskranken- und Pflege-Pflichtversicherungsbeiträge
    mitgeteilt hat.

    Berechnet mit den Merkern KRV = 2 und PKV = 1; PKPV = 0

    Steuerklasse V
    '''
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 5,              # Steuerklasse
        'KRV': 2,               # in keinem Sozialversicherungszweig versichert
        'PKV': 1,               # privat krankenversicherte Arbeitnehmer
        'PKPV': 0,              # private Basiskranken- bzw. Pflege-Pflichtversicherung 
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


@pytest.mark.parametrize('re4, expected', [
    (Decimal(500000),  Decimal(61600)),
    (Decimal(750000),  Decimal(92400)),
    (Decimal(1000000), Decimal(123200)),
    (Decimal(1250000), Decimal(164100)),
    (Decimal(1500000), Decimal(256500)),
    (Decimal(1750000), Decimal(357300)),
    (Decimal(2000000), Decimal(462300)),
    (Decimal(2250000), Decimal(550200)),
    (Decimal(2500000), Decimal(642000)),
    (Decimal(2750000), Decimal(739200)),
    (Decimal(3000000), Decimal(841800)),
    (Decimal(3250000), Decimal(946800)),
    (Decimal(3500000), Decimal(1051800)),
    (Decimal(3750000), Decimal(1156800)),
    (Decimal(4000000), Decimal(1261800)),
    (Decimal(4250000), Decimal(1366800)),
    (Decimal(4500000), Decimal(1471800)),
    (Decimal(4750000), Decimal(1576800)),
    (Decimal(5000000), Decimal(1681800)),
    (Decimal(5250000), Decimal(1786800)),
    (Decimal(5500000), Decimal(1891800)),
    (Decimal(5750000), Decimal(1996800)),
    (Decimal(6000000), Decimal(2101800)),
    (Decimal(6250000), Decimal(2206800)),
    (Decimal(6500000), Decimal(2311800)),
    (Decimal(6750000), Decimal(2416800)),
    (Decimal(7000000), Decimal(2521800)),
    (Decimal(7250000), Decimal(2626800)),
    (Decimal(7500000), Decimal(2731800)),
    (Decimal(7750000), Decimal(2836800)),
    (Decimal(8000000), Decimal(2941800)),
    (Decimal(8250000), Decimal(3046800)),
    (Decimal(8500000), Decimal(3151800)),
    (Decimal(8750000), Decimal(3256800)),
    (Decimal(9000000), Decimal(3361800))
])
def test_special_lohnsteuer_steuerklasse_6(re4, expected):
    '''
    Besondere maschinelle Jahreslohnsteuer 2019 (Prüftabelle)

    Besondere Lohnsteuer ist die Lohnsteuer, die für einen Arbeitnehmer zu erheben ist, der in
    keinem Sozialversicherungszweig versichert und privat kranken- und pflegeversichert ist
    sowie dem Arbeitgeber keine Basiskranken- und Pflege-Pflichtversicherungsbeiträge
    mitgeteilt hat.

    Berechnet mit den Merkern KRV = 2 und PKV = 1; PKPV = 0

    Steuerklasse VI
    '''
    # arrange
    params = {
        'RE4': re4,             # Bruttolohn in Cent
        'STKL': 6,              # Steuerklasse
        'KRV': 2,               # in keinem Sozialversicherungszweig versichert
        'PKV': 1,               # privat krankenversicherte Arbeitnehmer
        'PKPV': 0,              # private Basiskranken- bzw. Pflege-Pflichtversicherung 
        'LZZ': 1,               # Lohnzahlungszeitraum: Jahr
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == expected


def test_sonstige_bezuegen_1():
    '''
    Beispiel 1 mit Urlaubsgeld (Abrechnungsjahr 2019):

    Ein Arbeitnehmer hat ein Gehalt von 3.000,00 €.
    Er hat dieses Gehalt seit Anfang des Jahres 2019 bezogen.
    Abrechnungsmonat ist der Monat Mai 2019 mit zusätzlichem Urlaubsgeld von 1.000,00 €.
    Die elektronischen Lohnsteuerabzugsmerkmale des Arbeitnehmers beinhalten die Steuerklasse IV, keine Kinderfreibeträge und das Kirchensteuermerkmal ev.
    Die Betriebsstätte befindet sich in Hessen. Der Kirchensteuersatz beträgt 9%. Wegen der verbesserten steuerlichen Berücksichtigung von Vorsorgeaufwendungen müssen beim Steuerabzug Angaben zu Vorsorgeaufwendungen gemacht werden. Für unser Beispiel sind das:
        Rechtskreis West (wegen unterschiedlicher Beitragsbemessungsgrenzen; spielt bei diesem Monatseinkommen aber keine Rolle)
        Der Arbeitnehmer ist pflichtversichert in der gesetzlichen Krankenversicherung. Der krankenkassenindividuelle Zusatzbeitragssatz beträgt 1,1%.
        Beitragszuschlag für Kinderlose von 0,25%

    Vom aktuellen Arbeitgeber bereits gezahlter laufender Arbeitslohn:
    5 * 3.000,00 € = 15.000,00 €

    Umrechnung des bereits gezahlten laufenden Arbeitslohns auf 12 Monate:
    15.000,00 € / 5 * 12 = 36.000,00 €

    Es gibt keine bereits gezahlten steuerpflichtigen sonstigen Bezüge.

    Ein Hinzurechnungsbetrag bzw. Jahresfreibetrag ist nicht zu berücksichtigen.
    Altersentlastungsbetrag (Arbeitnehmer ist noch nicht 64) und Versorgungsfreibetrag (Arbeitnehmer erhält keinen Versorgungsbezug) kommen nicht in Betracht.
    '''
    # arrange
    params = {
        'JRE4': Decimal(3600000),   # Maßgebenden Jahresarbeitslohn (voraussichtliches Gehalt auf 12 Monate)
        'RE4': Decimal(300000),     # Brutto Monatsgehalt
        'SONSTB': Decimal(100000),  # Sonstige Bezüge
        'VBS': 0,                   # darin enthaltene Versorgungsbezüge
        'STKL': 1,                  # Steuerklasse
        'KRV': 0,                   # Gesetzliche RV -> BBG West
        'PKV': 0,                   # gesetzlich krankenversicherte Arbeitnehmer        
        'LZZ': 2,                   # Lohnzahlungszeitraum: Monat
        'R': 1,                     # Religionsgemeinschaft
        'KVZ': Decimal(1.1) ,       # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,                   # Zuschlag zur Pflegeversicherung für Kinderlose
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == 41575
    assert actual['SOLZLZZ'] == 2286
    assert actual['STS'] == 25500   # Lohnsteuer für sonstige Bezüge 
    assert actual['SOLZS'] == 1402
    

def test_sonstige_bezuegen_2():
    '''
    Beispiel 2 mit Weihnachtsgeld (Abrechnungsjahr 2019):
    
    Fortsetzung des obigen Beispiels
    Der Arbeitnehmer hat ein Gehalt von 3.000,00 €.
    Er hat dieses Gehalt seit Anfang des Jahres 2019 bezogen.
    Im Monat Mai wurde ein zusätzliches Urlaubsgeld von 1.000,00 € gezahlt.
    Abrechnungsmonat ist der Monat November 2019 mit zusätzlichem Weihnachtsgeld von 1.000,00 €.
    Die elektronischen Lohnsteuerabzugsmerkmale des Arbeitnehmers beinhalten die Steuerklasse IV, keine Kinderfreibeträge und das Kirchensteuermerkmal ev.
    Die Betriebsstätte befindet sich in Hessen. Der Kirchensteuersatz beträgt 9%. Wegen der verbesserten steuerlichen Berücksichtigung von Vorsorgeaufwendungen müssen beim Steuerabzug Angaben zu Vorsorgeaufwendungen gemacht werden. Für unser Beispiel sind das:
        Rechtskreis West (wegen unterschiedlicher Beitragsbemessungsgrenzen; spielt bei diesem Monatseinkommen aber keine Rolle)
        Der Arbeitnehmer ist pflichtversichert in der gesetzlichen Krankenversicherung. Der krankenkassenindividuelle Zusatzbeitragssatz beträgt 1,1%.
        Beitragszuschlag für Kinderlose von 0,25%

    Vom aktuellen Arbeitgeber bereits gezahlter laufender Arbeitslohn:
    11 * 3.000,00 € = 33.000,00 €

    Umrechnung des bereits gezahlten laufenden Arbeitslohns auf 12 Monate:
    33.000,00 € / 11 * 12 = 36.000,00 €

    Zu den 36.000,00 € muss der steuerpflichtige sonstige Bezug des Monat Mai von 1.000,00 € addiert werden.

    Ein Hinzurechnungsbetrag bzw. Jahresfreibetrag ist nicht zu berücksichtigen.
    Altersentlastungsbetrag (Arbeitnehmer ist noch nicht 64) und Versorgungsfreibetrag (Arbeitnehmer erhält keinen Versorgungsbezug) kommen nicht in Betracht.
    '''
    # arrange
    params = {
        'JRE4': Decimal(3700000),   # Maßgebender Jahresarbeitslohn ((voraussichtliches Gehalt auf 12 Monate + Urlaubsgeld Mai)
        'RE4': Decimal(300000),     # bereits erhaltenes Gehalt für 11 Monate
        'SONSTB': Decimal(100000),  # Sonstige Bezüge
        'VBS': 0,                   # darin enthaltene Versorgungsbezüge
        'STKL': 4,                  # Steuerklasse
        'KRV': 0,                   # Gesetzliche RV -> BBG West
        'PKV': 0,                   # gesetzlich krankenversicherte Arbeitnehmer        
        'LZZ': 2,                   # Lohnzahlungszeitraum: Monatlich
        'R': 1,                     # Religionsgemeinschaft
        'KVZ': Decimal(1.1) ,       # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,                   # Zuschlag zur Pflegeversicherung für Kinderlose
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['LSTLZZ'] == 41575
    assert actual['SOLZLZZ'] == 2286
    assert actual['STS'] == 25800   # Lohnsteuer für sonstige Bezüge 
    assert actual['SOLZS'] == 1419
    

def test_versorgungsbezuege():
    # arrange
    params = {
        'SONSTB': Decimal(2000000),  # Sonstige Bezüge
        'VBS': Decimal(100000),     # darin enthaltene Versorgungsbezüge
        'STKL': 1,                  # Steuerklasse
        'KRV': 0,                   # Gesetzliche RV -> BBG West
        'PKV': 0,                   # gesetzlich krankenversicherte Arbeitnehmer        
        'LZZ': 2,                   # Lohnzahlungszeitraum: Monat
        'R': 1,                     # Religionsgemeinschaft
        'KVZ': Decimal(1.1) ,       # Zusatzbeitragssatz Krankenkasse
        'PVZ': 1,                   # Zuschlag zur Pflegeversicherung für Kinderlose
    }
    # act
    actual = calculate_wage_tax(params)
    # assert
    assert actual['STS'] == 127900   
    assert actual['SOLZS'] == 7034



# todo: test alter > 65
# todo: test mehrjährige Tätigkeit
# todo: test Kinderfreibetrag


# Versorgungsbezüge
# Versorgungsbezüge sind nach der Definition in § 229 SGB V der Rente vergleichbare Einnahmen (Versorgungsbezüge), soweit sie wegen einer Einschränkung der Erwerbsfähigkeit oder zur Alters- oder Hinterbliebenenversorgung erzielt werden.
# Zu den Versorgungsbezügen gehören:
# Renten der Versicherungs- und Versorgungseinrichtungen, die für Angehörige bestimmter Berufe errichtet sind (z.B. der Ärzte, Architekten, Rechtsanwälte),
# Renten der betrieblichen Altersversorgung einschließlich der Zusatzversorgung im öffentlichen Dienst und der hüttenknappschaftlichen Zusatzversorgung,
# Bezüge aus der Versorgung der Abgeordneten, Parlamentarischen Staatssekretäre und Minister,
# Versorgungsbezüge aus einem öffentlich-rechtlichen Dienstverhältnis oder aus einem Arbeitsverhältnis mit Anspruch auf Versorgung nach beamtenrechtlichen Vorschriften oder Grundsätzen.

# Sonstige Bezüge:
# Sonstige Bezüge sind Vergütungen, die ihrem Wesen nach nicht zum laufenden Arbeitslohn gehöre
# Sie werden als einmalige Zahlung aus besonderem Anlass oder zu einem bestimmten Zweck gewährt.
# Beispiele: Weihnachtsgeld / Urlaubsgeld
# https://www.lohn-info.de/lohnsteuerabzug3.html
