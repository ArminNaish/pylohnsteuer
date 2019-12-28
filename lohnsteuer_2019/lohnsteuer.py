from decimal import Decimal, ROUND_UP, ROUND_DOWN
from . import parameters

def calculate_wage_tax(params):
    ''' Programmablaufplan für die Berechnung der Lohnsteuer 2019 '''
    inputs = {**parameters.wage_tax_inputs, **params}
    internals = parameters.wage_tax_internals.copy()
    outputs = parameters.wage_tax_outputs.copy()
    validate(inputs)
    mpara(inputs, internals)
    mre4jl(inputs, internals)
    internals['VBEZBSO'] = 0
    internals['KENNVMT'] = 0
    mre4(inputs, internals)
    mre4abz(inputs, internals)
    mberech(inputs, internals, outputs)
    msonst(inputs, internals, outputs)
    mvmt(inputs, internals, outputs)
    return outputs


def validate(inputs):
    ''' Validate input parameters '''
    if inputs['AF'] not in (0,1): 
        raise ValueError('AF must have a value of 0 or 1')
    if inputs['AJAHR'] < 0: 
        raise ValueError('AJAHR must not be negative')
    if inputs['ALTER1'] not in (0,1):
        raise ValueError('ALTER1 must have a value of 0 or 1')
    if inputs['ENTSCH'] < 0:
        raise ValueError('ENTSCH must not be negative')
    if inputs['F'] < 0:
        raise ValueError('F must not be negative')
    if inputs['JFREIB'] < 0:
        raise ValueError('F must not be negative')
    if inputs['JHINZU'] < 0:
        raise ValueError('JHINZU must not be negative')
    if inputs['JRE4'] < 0:
        raise ValueError('JRE4 must not be negative')
    if inputs['JRE4ENT'] < 0:
        raise ValueError('JRE4ENT must not be negative')
    if inputs['JVBEZ'] < 0:
        raise ValueError('JVBEZ must not be negative')
    if inputs['KRV'] not in (0,1,2):
        raise ValueError('KRV must have a value of 0, 1 or 2')
    if inputs['KVZ'] < 0:
        raise ValueError('KVZ must not be negative')
    if inputs['LZZ'] not in (1,2,3,4):
        raise ValueError('LZZ must have a value between 1 and 4')
    if inputs['LZZFREIB'] < 0:
        raise ValueError('LZZFREIB must not be negative')
    if inputs['LZZHINZU'] < 0:
        raise ValueError('LZZHINZU must not be negative')
    if inputs['PKPV'] < 0:
        raise ValueError('PKPV must not be negative')
    if inputs['PKV'] not in (0,1,2):
        raise ValueError('PKV must have a value of 0, 1 or 2')
    if inputs['PVS'] not in (0,1):
        raise ValueError('PVS must have a value of 0 or 1')
    if inputs['PVZ'] not in (0,1):
        raise ValueError('PVZ must have a value of 0 or 1')
    if inputs['R'] < 0:
        raise ValueError('R must not be negative')
    if inputs['RE4'] < 0:
        raise ValueError('RE4 must not be negative')
    if inputs['SONSTB'] < 0:
        raise ValueError('SONSTB must not be negative')
    if inputs['SONSTENT'] < 0:
        raise ValueError('SONSTENT must not be negative')
    if inputs['STERBE'] < 0:
        raise ValueError('STERBE must not be negative')
    if inputs['STKL'] not in (1,2,3,4,5,6):
        raise ValueError('STKL must have a value between 1 and 6')
    if inputs['VBEZ'] < 0:
        raise ValueError('VBEZ must not be negative')
    if inputs['VBEZM'] < 0:
        raise ValueError('VBEZM must not be negative')
    if inputs['VBEZS'] < 0:
        raise ValueError('VBEZS must not be negative')
    if inputs['VBS'] < 0:
        raise ValueError('VBS must not be negative')
    if inputs['VJAHR'] < 0:
        raise ValueError('VJAHR must not be negative')
    if inputs['VKAPA'] < 0:
        raise ValueError('VKAPA must not be negative')
    if inputs['VMT'] < 0:
        raise ValueError('VMT must not be negative')
    if inputs['ZKF'] < 0:
        raise ValueError('ZKF must not be negative')
    if inputs['ZMVB'] < 0:
        raise ValueError('ZMVB must not be negative')
    if inputs['AJAHR'] == 0 and inputs['ALTER1'] == 1:
        raise ValueError('AJAHR must be set when ALTER1 is 1')

    if inputs['VBEZ'] > 0 and inputs['LZZ'] == 1:
        if inputs['ZMVB'] == 0:
            raise ValueError('ZMVB must be set when LZZ is 1')
    if inputs['VBEZ'] > inputs['RE4']:
        raise ValueError('VBEZ must not be greater than RE4')
    if inputs['STKL'] == 6:
        if inputs['JHINZU'] > 0:
            raise ValueError('JHINZU must not be set when STKL is 6')
        if inputs['LZZHINZU'] > 0:
            raise ValueError('LZZHINZU must not be set when STKL is 6')
    if inputs['STKL'] != 4:
        if inputs['AF'] != 0:
            raise ValueError('AF must not be set when STKL is not 4')
    if inputs['STKL'] > 4:
        if inputs['ZKF'] > 0:
            raise ValueError('ZKF > 0 is only allowed in STKL 5 or 6')


def mpara(inputs, internals):
    ''' Zuweisung von Werten für bestimmte Sozialversicherungsparameter '''
    # Parameter Rentenversicherung
    if inputs['KRV'] < 2:
        if inputs['KRV'] == 0:
            internals['BBGRV'] = Decimal(80400)
        else:
            internals['BBGRV'] = Decimal(73800)
        internals['RVSATZAN'] = Decimal(0.093)
        internals['TBSVORV'] = Decimal(0.76)
    # Parameter Krankenversicherung/Pflegeversicherung
    internals['BBGKVPV'] = Decimal(54450)
    internals['KVSATZAN'] = (inputs['KVZ'] / 2 / 100) + Decimal(0.07)
    internals['KVSATZAG'] = Decimal(0.0045) + Decimal(0.07)
    if inputs['PVS'] == 1:
        internals['PVSATZAN'] = Decimal(0.02025)
        internals['PVSATZAG'] = Decimal(0.01025)
    else:
        internals['PVSATZAN'] = Decimal(0.01525)
        internals['PVSATZAG'] = Decimal(0.01525)
    if inputs['PVZ'] == 1:
        internals['PVSATZAN'] = internals['PVSATZAN'] + Decimal(0.0025)
    # Grenzwerte für die Steuerklassen V / VI
    internals['W1STKL5'] = Decimal(10635)
    internals['W2STKL5'] = Decimal(27980)
    internals['W3STKL5'] = Decimal(212261)
    # Grundfreibetrag
    internals['GFB'] = Decimal(9168)
    # Freigrenze SolZ
    internals['SOLZFREI'] = Decimal(972)


def mre4jl(inputs, internals):
    ''' Ermittlung des Jahresarbeitslohns und der Freibeträge '''
    if inputs['LZZ'] == 1:
        internals['ZRE4J'] = Decimal(inputs['RE4'] / 100)
        internals['ZVBEZJ'] = Decimal(inputs['VBEZ'] / 100)
        internals['JLFREIB'] = Decimal(inputs['LZZFREIB'] / 100)
        internals['JLHINZU'] = Decimal(inputs['LZZHINZU'] / 100)
    elif inputs['LZZ'] == 2:
        internals['ZRE4J'] = Decimal(inputs['RE4'] * 12 / 100)
        internals['ZVBEZJ'] = Decimal(inputs['VBEZ'] * 12 / 100)
        internals['JLFREIB'] = Decimal(inputs['LZZFREIB'] * 12 / 100)
        internals['JLHINZU'] = Decimal(inputs['LZZHINZU'] * 12 / 100)
    elif inputs['LZZ'] == 3:
        internals['ZRE4J'] = Decimal(inputs['RE4'] * 360 / 7 / 100)
        internals['ZVBEZJ'] = Decimal(inputs['VBEZ'] * 360 / 7 / 100)
        internals['JLFREIB'] = Decimal(inputs['LZZFREIB'] * 360 / 7 / 100)
        internals['JLHINZU'] = Decimal(inputs['LZZHINZU'] * 360 / 7 / 100)
    else:
        internals['ZRE4J'] = Decimal(inputs['RE4'] * 360 / 100)
        internals['ZVBEZJ'] = Decimal(inputs['VBEZ'] * 360 / 100)
        internals['JLFREIB'] = Decimal(inputs['LZZFREIB'] * 360 / 100)
        internals['JLHINZU'] = Decimal(inputs['LZZHINZU'] * 360 / 100)

    if inputs['AF'] == 0:
        inputs['F'] = Decimal(1)


def mre4(inputs, internals):
    ''' Ermittlung der Freibeträge für Versorgungsbezüge, Altersentlastungsbetrag '''
    if internals['ZVBEZJ'] == 0:
        internals['FVBZ'] = 0
        internals['FVB'] = 0
        internals['FVBZSO'] = 0
        internals['FVBSO'] = 0
    else:
        if inputs['VJAHR'] < 2006:
            internals['J'] = 1
        else:
            if inputs['VJAHR'] < 2040:
                internals['J'] = inputs['VJAHR'] - 2004
            else:
                internals['J'] = 36
        if inputs['LZZ'] == 1:
            internals['VBEZB'] = inputs['VBEZM'] * inputs['ZMVB'] + inputs['VBEZS']
            internals['HFVB'] = inputs['TAB2'][internals['J']] / 12 * inputs['ZMVB']
            internals['FVBZ'] = Decimal((inputs['TAB3'][internals['J']] / 12 * inputs['ZMVB'])).quantize(Decimal('1.'), rounding=ROUND_UP)
        else:
            internals['VBEZB'] = inputs['VBEZM'] * 12 + inputs['VBEZS']
            internals['HFVB'] = inputs['TAB2'][internals['J']]
            internals['FVBZ'] = inputs['TAB3'][internals['J']]
        internals['FVB'] = Decimal(internals['VBEZB'] * inputs['TAB1'][internals['J']] / 100).quantize(Decimal('1.00'), rounding=ROUND_UP)
        if internals['FVB'] > internals['HFVB']:
            internals['FVB'] = internals['HFVB']
        if internals['FVB'] > internals['ZVBEZJ']:
            internals['FVB'] = internals['ZVBEZJ']
        internals['FVBSO'] = Decimal(internals['FVB'] + internals['VBEZBSO'] * inputs['TAB1'][internals['J']] / 100).quantize(Decimal('1.00'), rounding=ROUND_UP)
        if internals['FVBSO'] > inputs['TAB2'][internals['J']]:
            internals['FVBSO'] = inputs['TAB2'][internals['J']]
        internals['HFVBZSO'] = (internals['VBEZB'] + internals['VBEZBSO']) / 100 - internals['FVBSO']
        internals['FVBZSO'] = Decimal(internals['FVBZ'] + internals['VBEZBSO'] / 100).quantize(Decimal('1.'), rounding=ROUND_UP)
        if internals['FVBZSO'] > internals['HFVBZSO']:
            internals['FVBZSO'] = Decimal(internals['HFVBZSO']).quantize(Decimal('1.'), rounding=ROUND_UP)
        if internals['FVBZSO'] > inputs['TAB3'][internals['J']]:
            internals['FVBZSO'] = inputs['TAB3'][internals['J']]
        internals['HFVBZ'] = internals['VBEZB'] / 100 - internals['FVB']
        if internals['FVBZ'] > internals['HFVBZ']:
            internals['FVBZ'] = Decimal(internals['HFVBZ']).quantize(Decimal('1.'), rounding=ROUND_UP)
    mre4alte(inputs, internals)


def mre4alte(inputs, internals):
    ''' Ermittlung des Altersentlastungsbetrags '''
    if inputs['ALTER1'] == 0:
        internals['ALTE'] = 0
    else:
        if inputs['AJAHR'] < 2006:
            internals['K'] = 1
        else:
            if inputs['AJAHR'] < 2040:
                internals['K'] = inputs['AJAHR'] - 2004
            else:
                internals['K'] = 36
        internals['BMG'] = internals['ZRE4J'] - internals['ZVBEZJ']
        internals['ALTE'] = Decimal(internals['BMG'] * inputs['TAB4'][internals['K']]).quantize(Decimal('1.00'), rounding=ROUND_UP)
        internals['HBALTE'] = inputs['TAB5'][internals['K']]
        if internals['ALTE'] > internals['HBALTE']:
            internals['ALTE'] = internals['HBALTE']


def mre4abz(inputs, internals):
    ''' Ermittlung des Jahresarbeitslohns nach Abzug der Freibeträge '''
    internals['ZRE4'] = internals['ZRE4J'] - internals['FVB'] - internals['ALTE'] - internals['JLFREIB'] + internals['JLHINZU']
    if internals['ZRE4'] < 0:
        internals['ZRE4'] = 0
    internals['ZRE4VP'] = internals['ZRE4J']
    if internals['KENNVMT'] == 2:
        internals['ZRE4VP'] = internals['ZRE4VP'] - inputs['ENTSCH'] / 100
    internals['ZVBEZ'] = internals['ZVBEZJ'] - internals['FVB']
    if internals['ZVBEZ'] < 0:
        internals['ZVBEZ'] = 0


def mberech(inputs, internals, outputs):
    ''' Berechnung für laufende Lohnzahlungszeiträume '''
    mztabfb(inputs, internals)
    outputs['VFRB'] = (internals['ANP'] + internals['FVB'] + internals['FVBZ']) * 100
    mlstjahr(inputs, internals)
    outputs['WVFRB'] = (internals['ZVE'] - internals['GFB']) * 100
    if outputs['WVFRB'] < 0:
        outputs['WVFRB'] = 0
    internals['LSTJAHR'] = internals['ST'] * inputs['F']
    uplstlzz(inputs, internals, outputs)
    upvkvlzz(inputs, internals, outputs)
    if inputs['ZKF'] > 0:
        internals['ZTABFB'] = internals['ZTABFB'] + internals['KFB']
        mre4abz(inputs, internals)
        mlstjahr(inputs, internals)
        internals['JBMG'] = internals['ST'] * internals['F']
    else:
        internals['JBMG'] = internals['LSTJAHR']
    msolz(inputs, internals, outputs)


def mztabfb(inputs, internals):
    ''' Ermittlung der festen Tabellenfreibeträge '''
    internals['ANP'] = 0
    if internals['ZVBEZ'] >= 0:
        if internals['ZVBEZ'] < internals['FVBZ']:
            internals['FVBZ'] = internals['ZVBEZ']
    if inputs['STKL'] < 6:
        if internals['ZVBEZ'] > 0:
            if (internals['ZVBEZ'] - internals['FVBZ']) < 102:
                internals['ANP'] = Decimal(internals['ZVBEZ'] - internals['FVBZ']).quantize(Decimal('1.'), rounding=ROUND_UP)
            else:
                internals['ANP'] = Decimal(102)
    else:
        internals['FVBZ'] = 0
        internals['FVBZSO'] = 0
    if inputs['STKL'] < 6:
        if internals['ZRE4'] > internals['ZVBEZ']:
            if (internals['ZRE4'] - internals['ZVBEZ']) < 1000:
                internals['ANP'] = Decimal(internals['ANP'] + internals['ZRE4'] - internals['ZVBEZ']).quantize(Decimal('1.'), rounding=ROUND_UP)
            else:
                internals['ANP'] = internals['ANP'] + Decimal(1000)
    internals['KZTAB'] = 1
    if inputs['STKL'] == 1:
        internals['SAP'] = 36
        internals['KFB'] = inputs['ZKF'] * 7620
    elif inputs['STKL'] == 2:
        internals['EFA'] = 1908
        internals['SAP'] = 36
        internals['KFB'] = inputs['ZKF'] * 7620
    elif inputs['STKL'] == 3:
        internals['KZTAB'] = 2
        internals['SAP'] = 36
        internals['KFB'] = inputs['ZKF'] * 7620
    elif inputs['STKL'] == 4:
        internals['SAP'] = 36
        internals['KFB'] = inputs['ZKF'] * 3810
    elif inputs['STKL'] == 5:
        internals['SAP'] = 36
        internals['KFB'] = 0
    else:
        internals['KFB'] = 0
    internals['ZTABFB'] = internals['EFA'] + internals['ANP'] + internals['SAP'] + internals['FVBZ']


def mlstjahr(inputs, internals):
    ''' Ermittlung der Jahreslohnsteuer '''
    upevp(inputs, internals)
    if internals['KENNVMT'] != 1:
        internals['ZVE'] = internals['ZRE4'] - internals['ZTABFB'] - internals['VSP']
        upmlst(inputs, internals)
    else:
        internals['ZVE'] = internals['ZRE4'] - internals['ZTABFB'] - internals['VSP'] - internals['VMT'] / 100 - internals['VKAPA'] / 100
        if internals['ZVE'] < 0:
            internals['ZVE'] = (internals['ZVE'] + internals['VMT'] / 100 - internals['VKAPA'] / 100) / 5
            upmlst(inputs, internals)
            internals['ST'] = internals['ST'] * 5
        else:
            upmlst(inputs, internals)
            internals['STOVMT'] = internals['ST']
            internals['ZVE'] = internals['ZVE'] + Decimal(inputs['VMT'] + inputs['VKAPA']) / 500
            upmlst(inputs, internals)
            internals['ST'] = (internals['ST'] - internals['STOVMT']) * 5 + internals['STOVMT']


def upvkvlzz(inputs, internals, outputs):
    ''' Ermittlung des Anteils der berücksichtigten Vorsorgeaufwendungen für den Lohnzahlungszeitraum '''
    upvkv(inputs, internals)
    internals['JW'] = internals['VKV']
    upanteil(inputs, internals)
    outputs['VKVLZZ'] = internals['ANTEIL1']


def upvkv(inputs, internals):
    ''' Ermittlung der Jahreswertes der berücksichtigten privaten Kranken- und Pflegeversicherungsbeiträge '''
    if inputs['PKV'] > 0:
        if internals['VSP2'] > internals['VSP3']:
            internals['VKV'] = internals['VSP2'] * 100
        else:
            internals['VKV'] = internals['VSP3'] * 100
    else:
        internals['VKV'] = 0


def uplstlzz(inputs, internals, outputs):
    ''' Ermittlung des Anteils der Jahreslohnsteuer für den Lohnzahlungszeitraum '''
    internals['JW'] = internals['LSTJAHR'] * 100
    upanteil(inputs, internals)
    outputs['LSTLZZ'] = internals['ANTEIL1']


def upmlst(inputs, internals):
    ''' Berechnung der Lohnsteuer '''
    if internals['ZVE'] < 1:
        internals['ZVE'] = 0
        internals['X'] = 0
    else:
        internals['X'] = Decimal(internals['ZVE'] / internals['KZTAB']).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    if inputs['STKL'] < 5:
        uptab19(inputs, internals)
    else:
        mst5_6(inputs, internals)


def upevp(inputs, internals):
    ''' Ermittlung der Vorsorgepauschale '''
    # Teilbetrag für die Rentenversicherung
    if inputs['KRV'] > 1:
        internals['VSP1'] = 0
    else:
        if internals['ZRE4VP'] > internals['BBGRV']:
            internals['ZRE4VP'] = internals['BBGRV']
        internals['VSP1'] = internals['TBSVORV'] * internals['ZRE4VP']
        internals['VSP1'] = internals['VSP1'] * internals['RVSATZAN']
    # Teilbetrag für die gesetzliche Krankenversicherung und Pflegeversicherung
    internals['VSP2'] = Decimal(0.12) * internals['ZRE4VP']
    if inputs['STKL'] == 3:
        internals['VHB'] = Decimal(3000)
    else:
        internals['VHB'] = Decimal(1900)

    if internals['VSP2'] > internals['VHB']:
        internals['VSP2'] = internals['VHB']
    internals['VSPN'] = Decimal(internals['VSP1'] + internals['VSP2']).quantize(Decimal('1.'), rounding=ROUND_UP)
    mvsp(inputs, internals)
    if internals['VSPN'] > internals['VSP']:
        internals['VSP'] = internals['VSPN']


def mvsp(inputs, internals):
    ''' Vorsorgepauschale - Vergleichsberechung zur Mindestvorsorgepauschale '''
    if internals['ZRE4VP'] > internals['BBGKVPV']:
        internals['ZRE4VP'] = internals['BBGKVPV']
    if inputs['PKV'] > 0:
        # Teilbetrag für die private Basiskranken- und Pflege-Pflichtversicherung
        if inputs['STKL'] == 6:
            internals['VSP3'] = 0
        else:
            internals['VSP3'] = inputs['PKPV'] * 12 / 100
            if inputs['PKV'] == 2:
                internals['VSP3'] = internals['VSP3'] - internals['ZRE4VP'] * (internals['KVSATZAG'] + internals['PVSATZAG'])
    else:
        # Teilbetrag für die gesetzliche Krankenversicherung und Pflegeversicherung
        internals['VSP3'] = internals['ZRE4VP'] * (internals['KVSATZAN'] + internals['PVSATZAN'])
    internals['VSP'] = Decimal(internals['VSP3'] + internals['VSP1']).quantize(Decimal('1.'), rounding=ROUND_UP)


def mst5_6(inputs, internals):
    ''' Berechnung der Lohnsteuer für die Steuerklassen V und VI '''
    internals['ZZX'] = internals['X']
    if internals['ZZX'] > internals['W2STKL5']:
        internals['ZX'] = internals['W2STKL5']
        up5_6(inputs, internals)
        if internals['ZZX'] > internals['W3STKL5']:
            internals['ST'] = Decimal(internals['ST'] + (internals['W3STKL5'] - internals['W2STKL5']) * Decimal(0.42)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
            internals['ST'] = Decimal(internals['ST'] + (internals['ZZX'] - internals['W3STKL5']) * Decimal(0.45)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
        else:
            internals['ST'] = Decimal(internals['ST'] + (internals['ZZX'] - internals['W2STKL5']) * Decimal(0.42)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    else:
        internals['ZX'] = internals['ZZX']
        up5_6(inputs, internals)
        if internals['ZZX'] > internals['W1STKL5']:
            internals['VERGL'] = internals['ST']
            internals['ZX'] = internals['W1STKL5']
            up5_6(inputs, internals)
            internals['HOCH'] = Decimal(internals['ST'] + (internals['ZZX'] - internals['W1STKL5']) * Decimal(0.42)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
            if internals['HOCH'] < internals['VERGL']:
                internals['ST'] = internals['HOCH']
            else:
                internals['ST'] = internals['VERGL']


def up5_6(inputs, internals):
    internals['X'] = internals['ZX'] * Decimal(1.25)
    uptab19(inputs, internals)
    internals['ST1'] = internals['ST']
    internals['X'] = internals['ZX'] * Decimal(0.75)
    uptab19(inputs, internals)
    internals['ST2'] = internals['ST']
    internals['DIFF'] = (internals['ST1'] - internals['ST2']) * Decimal(2)
    internals['MIST'] = Decimal(internals['ZX'] * Decimal(0.14)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    if internals['MIST'] > internals['DIFF']:
        internals['ST'] = internals['MIST']
    else:
        internals['ST'] = internals['DIFF']


def msolz(inputs, internals, outputs):
    ''' Ermittlung des Solidaritätszuschlags '''
    internals['SOLZFREI'] = internals['SOLZFREI'] * internals['KZTAB']
    if internals['JBMG'] > internals['SOLZFREI']:
        internals['SOLZJ'] = Decimal(internals['JBMG'] * Decimal(5.5) / 100).quantize(Decimal('1.00'), rounding=ROUND_DOWN)
        internals['SOLZMIN'] = (internals['JBMG'] - internals['SOLZFREI']) * 20 / 100
        if internals['SOLZMIN'] < internals['SOLZJ']:
            internals['SOLZJ'] = internals['SOLZMIN']
        internals['JW'] = internals['SOLZJ'] * 100
        upanteil(inputs, internals)
        outputs['SOLZLZZ'] = internals['ANTEIL1']
    else:
        outputs['SOLZLZZ'] = 0
    if inputs['R'] > 0:
        internals['JW'] = internals['JBMG'] * 100
        upanteil(inputs, internals)
        outputs['BK'] = internals['ANTEIL1']
    else:
        outputs['BK'] = 0


def upanteil(inputs, internals):
    ''' Ermittlung des Anteils der Jahreslohnsteuer für den Lohnzahlungszeitraum '''
    if inputs['LZZ'] == 1:
        internals['ANTEIL1'] = internals['JW']
    elif inputs['LZZ'] == 2:
        internals['ANTEIL1'] = Decimal(internals['JW'] / 12).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    elif inputs['LZZ'] == 3:
        internals['ANTEIL1'] = Decimal(internals['JW'] * 7 / 360).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    else:
        internals['ANTEIL1'] = Decimal(internals['JW'] / 360).quantize(Decimal('1.'), rounding=ROUND_DOWN)


def msonst(inputs, internals, outputs):
    ''' Berechnung sonstiger Bezüge '''
    inputs['LZZ'] = 1
    if inputs['ZMVB'] == 0:
        inputs['ZMVB'] = 12
    if inputs['SONSTB'] == 0:
        outputs['VKVSONST'] = 0
        internals['LSTSO'] = 0
        outputs['STS'] = 0
        outputs['SOLZS'] = 0
        outputs['BKS'] = 0
    else:
        mosonst(inputs, internals)
        upvkv(inputs, internals)
        outputs['VKVSONST'] = internals['VKV']
        internals['ZRE4J'] = (inputs['JRE4'] + inputs['SONSTB']) / 100
        internals['ZVBEZJ'] = (inputs['JVBEZ'] + inputs['VBS']) / 100
        internals['VBEZBSO'] = inputs['STERBE']
        mre4sonst(inputs, internals)
        mlstjahr(inputs, internals)
        outputs['WVFRBM'] = (internals['ZVE'] - internals['GFB']) * Decimal(100)
        if outputs['WVFRBM'] < 0:
            outputs['WVFRBM'] = 0
        upvkv(inputs, internals)
        outputs['VKVSONST'] = internals['VKV']  - outputs['VKVSONST']
        internals['LSTSO'] = internals['ST'] * Decimal(100)
        outputs['STS'] = Decimal((internals['LSTSO'] - internals['LSTOSO']) * inputs['F']).quantize(Decimal('1.'), rounding=ROUND_DOWN)
        if outputs['STS'] < 0:
            outputs['STS'] = 0
        outputs['SOLZS'] = Decimal(outputs['STS'] * Decimal(5.5) / Decimal(100)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
        if inputs['R'] > 0:
            outputs['BKS'] = outputs['STS']
        else:
            outputs['BKS'] = 0


def mvmt(inputs, internals, outputs):
    ''' 
    Berechnung der Entschädigung und Vergütung für mehrjährige
    Tätigkeit nach § 39b Absatz 3 Satz 9 und 10 EStG 
    '''
    if inputs['VKAPA'] < 0:
        inputs['VKAPA'] = 0
    if inputs['VMT'] + inputs['VKAPA'] > 0:
        if internals['LSTSO'] == 0:
            mosonst(inputs, internals)
            internals['LST1'] = internals['LSTOSO']
        else:
            internals['LST1'] = internals['LSTSO']
        internals['VBEZBSO'] = inputs['STERBE'] + inputs['VKAPA']
        internals['ZRE4J'] = (inputs['JRE4'] + internals['SONSTB'] + internals['VMT'] + inputs['VKAPA']) / Decimal(100)
        internals['KENNVMT'] = 2
        mre4sonst(inputs, internals)
        mlstjahr(inputs,internals)
        internals['LST3'] = internals['ST'] * Decimal(100)
        mre4abz(inputs, internals)
        internals['ZRE4VP'] = internals['ZRE4VP'] - internals['JRE4ENT'] / Decimal(100) - internals['SONSTENT'] / Decimal(100)
        internals['KENNVMT'] = 1
        mlstjahr()
        internals['LST2'] = internals['ST'] * Decimal(100)
        outputs['STV'] = internals['LST2'] - internals['LST1']
        internals['LST3'] = internals['LST3'] - internals['LST1']
        if internals['LST3'] < outputs['STV']:
            outputs['STV'] = internals['LST3']
        if outputs['STV'] < 0:
            outputs['STV'] = 0
        else:
            outputs['STV'] = Decimal(outputs['STV'] * inputs['F']).quantize(Decimal('1.'), rounding=ROUND_DOWN)
        outputs['SOLZV'] = outputs['STV'] * Decimal(5.5) / Decimal(100)
        if internals['R'] > 0:
            outputs['BKV'] = outputs['STV']
        else:
            outputs['BKV'] = 0
    else:
        outputs['STV'] = 0
        outputs['SOLZV'] = 0
        outputs['BKV'] = 0


def mosonst(inputs, internals):
    ''' 
    Sonderberechnung ohne sonstige Bezüge für Berechnung bei 
    sonstigen Bezügen oder Vergütung für mehrjährige Tätigkeit 
    '''
    internals['ZRE4J'] = inputs['JRE4'] / Decimal(100)
    internals['ZVBEZJ'] = inputs['JVBEZ'] / Decimal(100)
    internals['JLFREIB'] = inputs['JFREIB'] / Decimal(100)
    internals['JLHINZU'] = inputs['JHINZU'] / Decimal(100)
    mre4(inputs, internals)
    mre4abz(inputs, internals)
    internals['ZRE4VP'] = internals['ZRE4VP'] - inputs['JRE4ENT'] / Decimal(100)
    mztabfb(inputs, internals)
    internals['VFRBS1'] = (internals['ANP'] + internals['FVB'] + internals['FVBZ']) * Decimal(100)
    mlstjahr(inputs, internals)
    internals['WVFRBO'] = (internals['ZVE'] - internals['GFB']) * Decimal(100)
    if internals['WVFRBO'] < 0:
        internals['WVFRBO'] = 0
    internals['LSTOSO'] = internals['ST']  * Decimal(100)


def mre4sonst(inputs, internals):
    '''
    Sonderberechnung mit sonstigen Bezügen für Berechnung bei 
    sonstigen Bezügen oder Vergütung für mehrjährige Tätigkeit
    '''
    mre4(inputs, internals)
    internals['FVB'] = internals['FVBSO']
    mre4abz(inputs, internals)
    internals['ZRE4VP'] = internals['ZRE4VP'] - inputs['JRE4ENT'] / Decimal(100) - inputs['SONSTENT'] / Decimal(100)
    internals['FVBZ'] = internals['FVBZSO']
    mztabfb(inputs, internals)
    internals['VFRBS2'] = (internals['ANP'] + internals['FVB'] + internals['FVBZ']) * Decimal(100) - internals['VFRBS1']


def uptab19(inputs, internals):
    ''' Ermittlung der tariflichen Einkommensteuer '''
    if internals['X'] < internals['GFB'] + 1:
        internals['ST'] = 0
    elif internals['X'] < 14255:
        internals['Y'] = (internals['X'] - internals['GFB']) / 10000
        internals['RW'] = internals['Y'] * Decimal(980.14)
        internals['RW'] = internals['RW'] + 1400
        internals['ST'] = Decimal(internals['RW'] * internals['Y']).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    elif internals['X'] < 55961:
        internals['Y'] = (internals['X'] - 14254) / 10000
        internals['RW'] = internals['Y'] * Decimal(216.16)
        internals['RW'] = internals['RW'] + 2397
        internals['RW'] = internals['RW'] * internals['Y']
        internals['ST'] = Decimal(internals['RW'] + Decimal(965.58)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    elif internals['X'] < 265327:
        internals['ST'] = Decimal(internals['X'] * Decimal(0.42) - Decimal(8780.90)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    else:
        internals['ST'] = Decimal(internals['X'] * Decimal(0.45) - Decimal(16740.68)).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    internals['ST'] = internals['ST'] * internals['KZTAB']















