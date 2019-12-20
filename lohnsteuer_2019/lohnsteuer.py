import math

from decimal import Decimal, ROUND_UP, ROUND_DOWN


def calculate_wage_tax(wage_tax_inputs, wage_tax_internals, wage_tax_outputs):
    ''' Programmablaufplan für die Berechnung der Lohnsteuer 2019 '''
    # todo: add validation
    # todo: add comments to code to understand it
    mpara(wage_tax_inputs, wage_tax_internals)
    mre4jl(wage_tax_inputs, wage_tax_internals)
    wage_tax_internals['VBEZBSO'] = 0
    wage_tax_internals['KENNVMT'] = 0
    mre4(wage_tax_inputs, wage_tax_internals)
    mre4abz(wage_tax_inputs, wage_tax_internals)
    mberech(wage_tax_inputs, wage_tax_internals, wage_tax_outputs)
    # todo: implement msonst and mvmt features
    # msonst(wage_tax_inputs, wage_tax_internals, wage_tax_outputs)
    # mvmt(wage_tax_inputs, wage_tax_internals, wage_tax_outputs)


def mpara(wage_tax_inputs, wage_tax_internals):
    ''' Zuweisung von Werten für bestimmte Sozialversicherungsparameter '''
    # Parameter Rentenversicherung
    if wage_tax_inputs['KRV'] < 2:
        if wage_tax_inputs['KRV'] == 0:
            wage_tax_internals['BBGRV'] = Decimal(80400)
        else:
            wage_tax_internals['BBGRV'] = Decimal(73800)
        wage_tax_internals['RVSATZAN'] = Decimal(0.093)
        wage_tax_internals['TBSVORV'] = Decimal(0.76)

    # Parameter Krankenversicherung/Pflegeversicherung
    wage_tax_internals['BBGKVPV'] = Decimal(54450)
    wage_tax_internals['KVSATZAN'] = (wage_tax_inputs['KVZ'] / 2 / 100) + Decimal(0.07)
    wage_tax_internals['KVSATZAG'] = Decimal(0.0045) + Decimal(0.07)
    if wage_tax_inputs['PVS'] == 1:
        wage_tax_internals['PVSATZAN'] = Decimal(0.02025)
        wage_tax_internals['PVSATZAG'] = Decimal(0.01025)
    else:
        wage_tax_internals['PVSATZAN'] = Decimal(0.01525)
        wage_tax_internals['PVSATZAG'] = Decimal(0.01525)
    if wage_tax_inputs['PVZ'] == 1:
        wage_tax_internals['PVSATZAN'] = wage_tax_internals['PVSATZAN'] + Decimal(0.0025)

    # Grenzwerte für die Steuerklassen V / VI
    wage_tax_internals['W1STKL5'] = Decimal(10635)
    wage_tax_internals['W2STKL5'] = Decimal(27980)
    wage_tax_internals['W3STKL5'] = Decimal(212261)

    # Grundfreibetrag
    wage_tax_internals['GFB'] = Decimal(9168)

    # Freigrenze SolZ
    wage_tax_internals['SOLZFREI'] = Decimal(972)


def mre4jl(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung des Jahresarbeitslohns und der Freibeträge '''
    if wage_tax_inputs['LZZ'] == 1:
        wage_tax_internals['ZRE4J'] = Decimal(wage_tax_inputs['RE4'] / 100)
        wage_tax_internals['ZVBEZJ'] = Decimal(wage_tax_inputs['VBEZ'] / 100)
        wage_tax_internals['JLFREIB'] = Decimal(wage_tax_inputs['LZZFREIB'] / 100)
        wage_tax_internals['JLHINZU'] = Decimal(wage_tax_inputs['LZZHINZU'] / 100)
    else:
        if wage_tax_inputs['LZZ'] == 2:
            wage_tax_internals['ZRE4J'] = Decimal(wage_tax_inputs['RE4'] * 12 / 100)
            wage_tax_internals['ZVBEZJ'] = Decimal(wage_tax_inputs['VBEZ'] * 12 / 100)
            wage_tax_internals['JLFREIB'] = Decimal(wage_tax_inputs['LZZFREIB'] * 12 / 100)
            wage_tax_internals['JLHINZU'] = Decimal(wage_tax_inputs['LZZHINZU'] * 12 / 100)
        else:
            if wage_tax_inputs['LZZ'] == 3:
                wage_tax_internals['ZRE4J'] = Decimal(wage_tax_inputs['RE4'] * 360 / 7 / 100)
                wage_tax_internals['ZVBEZJ'] = Decimal(wage_tax_inputs['VBEZ'] * 360 / 7 / 100)
                wage_tax_internals['JLFREIB'] = Decimal(wage_tax_inputs['LZZFREIB'] * 360 / 7 / 100)
                wage_tax_internals['JLHINZU'] = Decimal(wage_tax_inputs['LZZHINZU'] * 360 / 7 / 100)
            else:
                wage_tax_internals['ZRE4J'] = Decimal(wage_tax_inputs['RE4'] * 360 / 100)
                wage_tax_internals['ZVBEZJ'] = Decimal(wage_tax_inputs['VBEZ'] * 360 / 100)
                wage_tax_internals['JLFREIB'] = Decimal(wage_tax_inputs['LZZFREIB'] * 360 / 100)
                wage_tax_internals['JLHINZU'] = Decimal(wage_tax_inputs['LZZHINZU'] * 360 / 100)

    if wage_tax_inputs['AF'] == 0:
        wage_tax_inputs['F'] = Decimal(1)


def mre4(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung der Freibeträge für Versorgungsbezüge, Altersentlastungsbetrag '''
    if wage_tax_internals['ZVBEZJ'] == 0:
        wage_tax_internals['FVBZ'] = 0
        wage_tax_internals['FVB'] = 0
        wage_tax_internals['FVBZSO'] = 0
        wage_tax_internals['FVBSO'] = 0
    else:
        if wage_tax_inputs['VJAHR'] < 2006:
            wage_tax_internals['J'] = 1
        else:
            if wage_tax_inputs['VJAHR'] < 2040:
                wage_tax_internals['J'] = wage_tax_inputs['VJAHR'] - 2004
            else:
                wage_tax_internals['J'] = 36

        if wage_tax_inputs['LZZ'] == 1:
            wage_tax_internals['VBEZB'] = wage_tax_inputs['VBEZM'] * wage_tax_inputs['ZMVB'] + wage_tax_inputs['VBEZS']
            wage_tax_internals['HFVB'] = wage_tax_inputs['TAB2'][wage_tax_internals['J']] / 12 * wage_tax_inputs['ZMVB']
            wage_tax_internals['FVBZ'] = Decimal((wage_tax_inputs['TAB3'][wage_tax_internals['J']] / 12 * wage_tax_inputs['ZMVB'])).quantize(Decimal('1.'), rounding=ROUND_UP)
        else:
            wage_tax_internals['VBEZB'] = wage_tax_inputs['VBEZM'] * 12 + wage_tax_inputs['VBEZS']
            wage_tax_internals['HFVB'] = wage_tax_inputs['TAB2'][wage_tax_internals['J']]
            wage_tax_internals['FVBZ'] = wage_tax_inputs['TAB3'][wage_tax_internals['J']]

        wage_tax_internals['FVB'] = Decimal(wage_tax_internals['VBEZB'] * wage_tax_inputs['TAB1'][wage_tax_internals['J']] / 100).quantize(Decimal('1.00'), rounding=ROUND_UP)
        if wage_tax_internals['FVB'] > wage_tax_internals['HFVB']:
            wage_tax_internals['FVB'] = wage_tax_internals['HFVB']
        if wage_tax_internals['FVB'] > wage_tax_internals['ZVBEZJ']:
            wage_tax_internals['FVB'] = wage_tax_internals['ZVBEZJ']

        wage_tax_internals['FVBSO'] = Decimal(wage_tax_internals['FVB'] + wage_tax_internals['VBEZBSO'] * wage_tax_inputs['TAB1'][wage_tax_internals['J']] / 100).quantize(Decimal('1.00'), rounding=ROUND_UP)
        if wage_tax_internals['FVBSO'] > wage_tax_inputs['TAB2'][wage_tax_internals['J']]:
            wage_tax_internals['FVBSO'] = wage_tax_inputs['TAB2'][wage_tax_internals['J']]

        wage_tax_internals['HFVBZSO'] = (wage_tax_internals['VBEZB'] + wage_tax_internals['VBEZBSO']) / 100 - wage_tax_internals['FVBSO']
        wage_tax_internals['FVBZSO'] = Decimal(wage_tax_internals['FVBZ'] + wage_tax_internals['VBEZBSO'] / 100).quantize(Decimal('1.'), rounding=ROUND_UP)
        if wage_tax_internals['FVBZSO'] > wage_tax_internals['HFVBZSO']:
            wage_tax_internals['FVBZSO'] = Decimal(wage_tax_internals['HFVBZSO']).quantize(Decimal('1.'), rounding=ROUND_UP)
        if wage_tax_internals['FVBZSO'] > wage_tax_inputs['TAB3'][wage_tax_internals['J']]:
            wage_tax_internals['FVBZSO'] = wage_tax_inputs['TAB3'][wage_tax_internals['J']]

        wage_tax_internals['HFVBZ'] = wage_tax_internals['VBEZB'] / 100 - wage_tax_internals['FVB']
        if wage_tax_internals['FVBZ'] > wage_tax_internals['HFVBZ']:
            wage_tax_internals['FVBZ'] = Decimal(wage_tax_internals['HFVBZ']).quantize(Decimal('1.'), rounding=ROUND_UP)

    mre4alte(wage_tax_inputs, wage_tax_internals)


def mre4alte(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung des Altersentlastungsbetrags '''
    if wage_tax_inputs['ALTER1'] == 0:
        wage_tax_internals['ALTE'] = 0
    else:
        if wage_tax_inputs['AJAHR'] < 2006:
            wage_tax_internals['K'] = 1
        else:
            if wage_tax_inputs['AJAHR'] < 2040:
                wage_tax_internals['K'] = wage_tax_inputs['AJAHR'] - 2004
            else:
                wage_tax_internals['K'] = 36

        wage_tax_internals['BMG'] = wage_tax_internals['ZRE4J'] - wage_tax_internals['ZVBEZJ']
        wage_tax_internals['ALTE'] = Decimal(wage_tax_internals['BMG'] * wage_tax_inputs['TAB4'][wage_tax_internals['K']]).quantize(Decimal('1.00'), rounding=ROUND_UP)
        wage_tax_internals['HBALTE'] = wage_tax_inputs['TAB5'][wage_tax_internals['K']]
        if wage_tax_internals['ALTE'] > wage_tax_internals['HBALTE']:
            wage_tax_internals['ALTE'] = wage_tax_internals['HBALTE']


def mre4abz(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung des Jahresarbeitslohns nach Abzug der Freibeträge '''
    wage_tax_internals['ZRE4'] = wage_tax_internals['ZRE4J'] - wage_tax_internals['FVB'] - wage_tax_internals['ALTE'] - wage_tax_internals['JLFREIB'] + wage_tax_internals['JLHINZU']
    if wage_tax_internals['ZRE4'] < 0:
        wage_tax_internals['ZRE4'] = 0

    wage_tax_internals['ZRE4VP'] = wage_tax_internals['ZRE4J']
    if wage_tax_internals['KENNVMT'] == 2:
        wage_tax_internals['ZRE4VP'] = wage_tax_internals['ZRE4VP'] - wage_tax_inputs['ENTSCH'] / 100

    wage_tax_internals['ZVBEZ'] = wage_tax_internals['ZVBEZJ'] - wage_tax_internals['FVB']
    if wage_tax_internals['ZVBEZ'] < 0:
        wage_tax_internals['ZVBEZ'] = 0


def mberech(wage_tax_inputs, wage_tax_internals, wage_tax_outputs):
    ''' Berechnung für laufende Lohnzahlungszeiträume '''
    mztabfb(wage_tax_inputs, wage_tax_internals)
    wage_tax_outputs['VFRB'] = (wage_tax_internals['ANP'] + wage_tax_internals['FVB'] + wage_tax_internals['FVBZ']) * 100
    mlstjahr(wage_tax_inputs, wage_tax_internals)
    wage_tax_outputs['WVFRB'] = (wage_tax_internals['ZVE'] - wage_tax_internals['GFB']) * 100
    if wage_tax_outputs['WVFRB'] < 0:
        wage_tax_outputs['WVFRB'] = 0
    wage_tax_internals['LSTJAHR'] = wage_tax_internals['ST'] * wage_tax_inputs['F']
    uplstlzz(wage_tax_inputs, wage_tax_internals, wage_tax_outputs)
    upvkvlzz(wage_tax_inputs, wage_tax_internals, wage_tax_outputs)
    if wage_tax_inputs['ZKF'] > 0:
        wage_tax_internals['ZTABFB'] = wage_tax_internals['ZTABFB'] + wage_tax_internals['KFB']
        mre4abz(wage_tax_inputs, wage_tax_internals)
        mlstjahr(wage_tax_inputs, wage_tax_internals)
        wage_tax_internals['JBMG'] = wage_tax_internals['ST'] * wage_tax_internals['F']
    else:
        wage_tax_internals['JBMG'] = wage_tax_internals['LSTJAHR']
    msolz(wage_tax_inputs, wage_tax_internals, wage_tax_outputs)


def mztabfb(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung der festen Tabellenfreibeträge '''
    wage_tax_internals['ANP'] = 0
    if wage_tax_internals['ZVBEZ'] >= 0:
        if wage_tax_internals['ZVBEZ'] < wage_tax_internals['FVBZ']:
            wage_tax_internals['FVBZ'] = wage_tax_internals['ZVBEZ']

    if wage_tax_inputs['STKL'] < 6:
        if wage_tax_internals['ZVBEZ'] > 0:
            if (wage_tax_internals['ZVBEZ'] - wage_tax_internals['FVBZ']) < 102:
                wage_tax_internals['ANP'] = Decimal(wage_tax_internals['ZVBEZ'] - wage_tax_internals['FVBZ']).quantize(Decimal('1.'), rounding=ROUND_UP)
            else:
                wage_tax_internals['ANP'] = Decimal(102)
    else:
        wage_tax_internals['FVBZ'] = 0
        wage_tax_internals['FVBZSO'] = 0

    if wage_tax_inputs['STKL'] < 6:
        if wage_tax_internals['ZRE4'] > wage_tax_internals['ZVBEZ']:
            if (wage_tax_internals['ZRE4'] - wage_tax_internals['ZVBEZ']) < 1000:
                wage_tax_internals['ANP'] = Decimal(wage_tax_internals['ANP'] + wage_tax_internals['ZRE4'] - wage_tax_internals['ZVBEZ']).quantize(Decimal('1.'), rounding=ROUND_UP)
            else:
                wage_tax_internals['ANP'] = wage_tax_internals['ANP'] + Decimal(1000)

    wage_tax_internals['KZTAB'] = 1

    if wage_tax_inputs['STKL'] == 1:
        wage_tax_internals['SAP'] = 36
        wage_tax_internals['KFB'] = wage_tax_inputs['ZKF'] * 7620
    elif wage_tax_inputs['STKL'] == 2:
        wage_tax_internals['EFA'] = 1908
        wage_tax_internals['SAP'] = 36
        wage_tax_internals['KFB'] = wage_tax_inputs['ZKF'] * 7620
    elif wage_tax_inputs['STKL'] == 3:
        wage_tax_internals['KZTAB'] = 2
        wage_tax_internals['SAP'] = 36
        wage_tax_internals['KFB'] = wage_tax_inputs['ZKF'] * 7620
    elif wage_tax_inputs['STKL'] == 4:
        wage_tax_internals['SAP'] = 36
        wage_tax_internals['KFB'] = wage_tax_inputs['ZKF'] * 3810
    elif wage_tax_inputs['STKL'] == 5:
        wage_tax_internals['SAP'] = 36
        wage_tax_internals['KFB'] = 0
    else:
        wage_tax_internals['KFB'] = 0

    wage_tax_internals['ZTABFB'] = wage_tax_internals['EFA'] + wage_tax_internals['ANP'] + wage_tax_internals['SAP'] + wage_tax_internals['FVBZ']


def mlstjahr(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung der Jahreslohnsteuer '''
    upevp(wage_tax_inputs, wage_tax_internals)
    if wage_tax_internals['KENNVMT'] != 1:
        wage_tax_internals['ZVE'] = wage_tax_internals['ZRE4'] - wage_tax_internals['ZTABFB'] - wage_tax_internals['VSP']
        upmlst(wage_tax_inputs, wage_tax_internals)
    else:
        wage_tax_internals['ZVE'] = wage_tax_internals['ZRE4'] - wage_tax_internals['ZTABFB'] - wage_tax_internals['VSP'] - wage_tax_internals['VMT'] / 100 - wage_tax_internals['VKAPA'] / 100

        if wage_tax_internals['ZVE'] < 0:
            wage_tax_internals['ZVE'] = (wage_tax_internals['ZVE'] + wage_tax_internals['VMT'] / 100 - wage_tax_internals['VKAPA'] / 100) / 5
            upmlst(wage_tax_inputs, wage_tax_internals)
            wage_tax_internals['ST'] = wage_tax_internals['ST'] * 5
        else:
            upmlst(wage_tax_inputs, wage_tax_internals)
            wage_tax_internals['STOVMT'] = wage_tax_internals['ST']
            wage_tax_internals['ZVE'] = wage_tax_internals['ZVE'] + Decimal(wage_tax_inputs['VMT'] + wage_tax_inputs['VKAPA']) / 500
            upmlst(wage_tax_inputs, wage_tax_internals)
            wage_tax_internals['ST'] = (wage_tax_internals['ST'] - wage_tax_internals['STOVMT']) * 5 + wage_tax_internals['STOVMT']


def upvkvlzz(wage_tax_inputs, wage_tax_internals, wage_tax_outputs):
    ''' Ermittlung des Anteils der berücksichtigten Vorsorgeaufwendungen für den Lohnzahlungszeitraum '''
    upvkv(wage_tax_inputs, wage_tax_internals)
    wage_tax_internals['JW'] = wage_tax_internals['VKV']
    upanteil(wage_tax_inputs, wage_tax_internals)
    wage_tax_outputs['VKVLZZ'] = wage_tax_internals['ANTEIL1']


def upvkv(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung der Jahreswertes der berücksichtigten privaten Kranken- und Pflegeversicherungsbeiträge '''
    if wage_tax_inputs['PKV'] > 0:
        if wage_tax_internals['VSP2'] > wage_tax_internals['VSP3']:
            wage_tax_internals['VKV'] = wage_tax_internals['VSP2'] * 100
        else:
            wage_tax_internals['VKV'] = wage_tax_internals['VSP3'] * 100
    else:
        wage_tax_internals['VKV'] = 0


def uplstlzz(wage_tax_inputs, wage_tax_internals, wage_tax_outputs):
    ''' Ermittlung des Anteils der Jahreslohnsteuer für den Lohnzahlungszeitraum '''
    wage_tax_internals['JW'] = wage_tax_internals['LSTJAHR'] * 100
    upanteil(wage_tax_inputs, wage_tax_internals)
    wage_tax_outputs['LSTLZZ'] = wage_tax_internals['ANTEIL1']


def upevp(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung der Vorsorgepauschale '''
    # Teilbetrag für die Rentenversicherung
    if wage_tax_inputs['KRV'] > 1:
        wage_tax_internals['VSP1'] = 0
    else:
        if wage_tax_internals['ZRE4VP'] > wage_tax_internals['BBGRV']:
            wage_tax_internals['ZRE4VP'] = wage_tax_internals['BBGRV']
        wage_tax_internals['VSP1'] = wage_tax_internals['TBSVORV'] * wage_tax_internals['ZRE4VP']
        wage_tax_internals['VSP1'] = wage_tax_internals['VSP1'] * wage_tax_internals['RVSATZAN']

    # Teilbetrag für die gesetzliche Krankenversicherung und Pflegeversicherung
    wage_tax_internals['VSP2'] = Decimal(0.12) * wage_tax_internals['ZRE4VP']
    if wage_tax_inputs['STKL'] == 3:
        wage_tax_internals['VHB'] = Decimal(3000)
    else:
        wage_tax_internals['VHB'] = Decimal(1900)

    if wage_tax_internals['VSP2'] > wage_tax_internals['VHB']:
        wage_tax_internals['VSP2'] = wage_tax_internals['VHB']

    wage_tax_internals['VSPN'] = Decimal(wage_tax_internals['VSP1'] + wage_tax_internals['VSP2']).quantize(Decimal('1.'), rounding=ROUND_UP)
    mvsp(wage_tax_inputs, wage_tax_internals)
    if wage_tax_internals['VSPN'] > wage_tax_internals['VSP']:
        wage_tax_internals['VSP'] = wage_tax_internals['VSPN']


def mvsp(wage_tax_inputs, wage_tax_internals):
    ''' Vorsorgepauschale - Vergleichsberechung zur Mindestvorsorgepauschale '''
    if wage_tax_internals['ZRE4VP'] > wage_tax_internals['BBGKVPV']:
        wage_tax_internals['ZRE4VP'] = wage_tax_internals['BBGKVPV']

    if wage_tax_inputs['PKV'] > 0:
        # Teilbetrag für die private Basiskranken- und Pflege-Pflichtversicherung
        if wage_tax_inputs['STKL'] == 6:
            wage_tax_internals['VSP3'] = 0
        else:
            wage_tax_internals['VSP3'] = wage_tax_inputs['PKPV'] * 12 / 100
            if wage_tax_internals['PKV'] == 2:
                wage_tax_internals['VSP3'] = wage_tax_internals['VSP3'] - wage_tax_internals['ZRE4VP'] * (wage_tax_internals['KVSATZAG'] + wage_tax_internals['PVSATZAG'])
    else:
        # Teilbetrag für die gesetzliche Krankenversicherung und Pflegeversicherung
        wage_tax_internals['VSP3'] = wage_tax_internals['ZRE4VP'] * (wage_tax_internals['KVSATZAN'] + wage_tax_internals['PVSATZAN'])

    wage_tax_internals['VSP'] = Decimal(wage_tax_internals['VSP3'] + wage_tax_internals['VSP1']).quantize(Decimal('1.'), rounding=ROUND_UP)


def msolz(wage_tax_inputs, wage_tax_internals, wage_tax_outputs):
    ''' Ermittlung des Solidaritätszuschlags '''
    wage_tax_internals['SOLZFREI'] = wage_tax_internals['SOLZFREI'] * wage_tax_internals['KZTAB']
    if wage_tax_internals['JBMG'] > wage_tax_internals['SOLZFREI']:
        wage_tax_internals['SOLZJ'] = Decimal(wage_tax_internals['JBMG'] * Decimal(5.5) / 100).quantize(Decimal('1.00'), rounding=ROUND_DOWN)
        wage_tax_internals['SOLZMIN'] = (wage_tax_internals['JBMG'] - wage_tax_internals['SOLZFREI']) * 20 / 100
        if wage_tax_internals['SOLZMIN'] < wage_tax_internals['SOLZJ']:
            wage_tax_internals['SOLZJ'] = wage_tax_internals['SOLZMIN']
        wage_tax_internals['JW'] = wage_tax_internals['SOLZJ'] * 100
        upanteil(wage_tax_inputs, wage_tax_internals)
        wage_tax_outputs['SOLZLZZ'] = wage_tax_internals['ANTEIL1']
    else:
        wage_tax_outputs['SOLZLZZ'] = 0

    if wage_tax_inputs['R'] > 0:
        wage_tax_internals['JW'] = wage_tax_internals['JBMG'] * 100
        upanteil(wage_tax_inputs, wage_tax_internals)
        wage_tax_outputs['BK'] = wage_tax_internals['ANTEIL1']
    else:
        wage_tax_outputs['BK'] = 0


def upanteil(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung des Anteils der Jahreslohnsteuer für den Lohnzahlungszeitraum '''
    if wage_tax_inputs['LZZ'] == 1:
        wage_tax_internals['ANTEIL1'] = wage_tax_internals['JW']
    elif wage_tax_inputs['LZZ'] == 2:
        wage_tax_internals['ANTEIL1'] = Decimal(wage_tax_internals['JW'] / 12).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    elif wage_tax_inputs['LZZ'] == 3:
        wage_tax_internals['ANTEIL1'] = Decimal(wage_tax_internals['JW'] * 7 / 360).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    else:
        wage_tax_internals['ANTEIL1'] = Decimal(wage_tax_internals['JW'] / 360).quantize(Decimal('1.'), rounding=ROUND_DOWN)


def uptab19(wage_tax_inputs, wage_tax_internals):
    ''' Ermittlung der tariflichen Einkommensteuer '''
    if wage_tax_internals['X'] < wage_tax_internals['GFB'] + 1:
        wage_tax_internals['ST'] = 0
    elif wage_tax_internals['X'] < 14255:
        wage_tax_internals['Y'] = (wage_tax_internals['X'] - wage_tax_internals['GFB']) / 10000
        wage_tax_internals['RW'] = wage_tax_internals['Y'] * Decimal(980.14)
        wage_tax_internals['RW'] = wage_tax_internals['RW'] + 1400
        wage_tax_internals['ST'] = Decimal(wage_tax_internals['RW'] * wage_tax_internals['Y']).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    elif wage_tax_internals['X'] < 55961:
        wage_tax_internals['Y'] = (wage_tax_internals['X'] - 14254) / 10000
        wage_tax_internals['RW'] = wage_tax_internals['Y'] * Decimal(216.16)
        wage_tax_internals['RW'] = wage_tax_internals['RW'] + 2397
        wage_tax_internals['RW'] = wage_tax_internals['RW'] * wage_tax_internals['Y']
        wage_tax_internals['ST'] = Decimal(wage_tax_internals['RW'] + Decimal(965.58)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    elif wage_tax_internals['X'] < 265327:
        wage_tax_internals['ST'] = Decimal(wage_tax_internals['X'] * Decimal(0.42) - Decimal(8780.90)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    else:
        wage_tax_internals['ST'] = Decimal(wage_tax_internals['X'] * Decimal(0.45) - Decimal(16740.68)).quantize(Decimal('1.'), rounding=ROUND_DOWN)

    wage_tax_internals['ST'] = wage_tax_internals['ST'] * wage_tax_internals['KZTAB']


def upmlst(wage_tax_inputs, wage_tax_internals):
    ''' Berechnung der Lohnsteuer '''
    if wage_tax_internals['ZVE'] < 1:
        wage_tax_internals['ZVE'] = 0
        wage_tax_internals['X'] = 0
    else:
        wage_tax_internals['X'] = Decimal(wage_tax_internals['ZVE'] / wage_tax_internals['KZTAB']).quantize(Decimal('1.'), rounding=ROUND_DOWN)

    if wage_tax_inputs['STKL'] < 5:
        uptab19(wage_tax_inputs, wage_tax_internals)
    else:
        mst5_6(wage_tax_inputs, wage_tax_internals)


def mst5_6(wage_tax_inputs, wage_tax_internals):
    ''' Berechnung der Lohnsteuer für die Steuerklassen V und VI '''
    # todo: implement feature
    raise NotImplementedError('Feature is not yet implemented')


def mosonst(wage_tax_inputs, wage_tax_internals, wage_tax_outputs):
    ''' Berechnung sonstiger Bezüge ohne Vergütung für mehrjährige Tätigkeit '''
    # todo: implement feature
    raise NotImplementedError('Feature is not yet implemented')


def mvmt(wage_tax_inputs, wage_tax_internals, wage_tax_outputs):
    ''' Berechnung der Vergütung für mehrjährige Tätigkeit '''
    # todo: implement feature
    raise NotImplementedError('Feature is not yet implemented')