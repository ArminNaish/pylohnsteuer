from decimal import Decimal, ROUND_UP, ROUND_DOWN
from . import parameters

# todo: compare files -> extract differences -> merge similarities
# todo: extract constants
# todo: group things that change together
# todo: refactor to mixin base class?
# todo: add further test, (sonstige Bezüge)

def calculate_wage_tax(params):
    ''' Programmablaufplan für die Berechnung der Lohnsteuer 2020 '''
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
    msonst(inputs, internals)
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
    if not (0 <= inputs['KVZ'] <= 1):
        raise ValueError('KVZ must have a value between 0 and 1')
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
            internals['BBGRV'] = Decimal(82800)
        else:
            internals['BBGRV'] = Decimal(77400)
        internals['RVSATZAN'] = Decimal(0.093)
        internals['TBSVORV'] = Decimal(0.8)
    # Parameter Krankenversicherung/Pflegeversicherung
    internals['BBGKVPV'] = Decimal(56250)
    internals['KVSATZAN'] = (inputs['KVZ'] / 2 / 100) + Decimal(0.07)
    internals['KVSATZAG'] = Decimal(0.0055) + Decimal(0.07)
    if inputs['PVS'] == 1:
        internals['PVSATZAN'] = Decimal(0.02025)
        internals['PVSATZAG'] = Decimal(0.01025)
    else:
        internals['PVSATZAN'] = Decimal(0.01525)
        internals['PVSATZAG'] = Decimal(0.01525)
    if inputs['PVZ'] == 1:
        internals['PVSATZAN'] = internals['PVSATZAN'] + Decimal(0.0025)
    # Grenzwerte für die Steuerklassen V / VI
    internals['W1STKL5'] = Decimal(10898)
    internals['W2STKL5'] = Decimal(28526)
    internals['W3STKL5'] = Decimal(216400)
    # Grundfreibetrag
    internals['GFB'] = Decimal(9408)
    # Freigrenze SolZ
    internals['SOLZFREI'] = Decimal(972)

