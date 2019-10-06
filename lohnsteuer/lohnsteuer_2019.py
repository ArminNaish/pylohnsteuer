wage_tax_inputs = {
    # 1, wenn die Anwendung des Faktorverfahrens gewählt wurde 
    # (nur in Steuerklasse IV) 
    'AF': 1,

    # Auf die Vollendung des 64. Lebensjahres folgendes Kalenderjahr 
    # (erforderlich, wenn ALTER1=1)
    'AJAHR': 0, 

    # 1, wenn das 64. Lebensjahr vor Beginn des Kalenderjahres vollendet wurde,
    # in dem der Lohnzahlungszeitraum endet (§ 24a EStG), sonst = 0
    'ALTER1': 0, 

    # In VKAPA und VMT enthaltene Entschädigungen nach § 24 Nummer 1 EStG 
    # in Cent
    'ENTSCH': 0.0, 

    # eingetragener Faktor mit drei Nachkommastellen
    'F': 1.0, 

    # Jahresfreibetrag für die Ermittlung der Lohnsteuer für die sonstigen
    # Bezüge nach Maßgabe der elektronischen Lohnsteuerabzugsmerkmale
    # nach § 39e EStG oder der Eintragung auf der Bescheinigung für den 
    # Lohnsteuerabzug 2019 in Cent(ggf. 0)
    'JFREIB': 0.0,

    # Jahreshinzurechnungsbetrag für die Ermittlung der Lohnsteuer für
    # die sonstigen Bezüge nach Maßgabe der elektronischen
    # Lohnsteuerabzugsmerkmale nach § 39e EStG oder der Eintragung
    # auf der Bescheinigung für den Lohnsteuerabzug 2019 in Cent (ggf. 0)
    'JHINZU': 0.0,

    # Voraussichtlicher Jahresarbeitslohn ohne sonstige Bezüge und ohne
    # Vergütung für mehrjährige Tätigkeit in Cent. Anmerkung: Die
    # Eingabe dieses Feldes (ggf. 0) ist erforderlich bei Eingaben zu
    # sonstigen Bezügen (Felder SONSTB, VMT oder VKAPA).
    # Sind in einem vorangegangenen Abrechnungszeitraum bereits
    # sonstige Bezüge gezahlt worden, so sind sie dem voraussichtlichen
    # Jahresarbeitslohn hinzuzurechnen. Vergütungen für mehrjährige
    # Tätigkeit aus einem vorangegangenen Abrechnungszeitraum wer-
    # den in voller Höhe hinzugerechnet.
    'JRE4': 0.0,

    # In JRE4 enthaltene Entschädigungen nach § 24 Nummer 1 EStG in Cent
    'JRE4ENT': 0.0,

    # In JRE4 enthaltene Versorgungsbezüge in Cent (ggf. 0)
    'JVBEZ': 0.0, 

    # Merker für die Vorsorgepauschale:
    # 0 = der Arbeitnehmer ist in der gesetzlichen Rentenversicherung
    # oder einer berufsständischen Versorgungseinrichtung
    # pflichtversichert oder bei Befreiung von der Versicherungspflicht
    # freiwillig versichert; 
    # es gilt die allgemeine Beitragsbemessungsgrenze (BBG West)
    # 1 = der Arbeitnehmer ist in der gesetzlichen Rentenversicherung
    # oder einer berufsständischen Versorgungseinrichtung
    # pflichtversichert oder bei Befreiung von der Versicherungspflicht
    # freiwillig versichert; 
    # es gilt die Beitragsbemessungsgrenze Ost (BBG Ost)
    # 2 = wenn nicht 0 oder 1
    'KRV': 0,

    # Kassenindividueller Zusatzbeitragssatz bei einem gesetzlich
    # krankenversicherten Arbeitnehmer in Prozent (bspw. 0,90 für
    # 0,90 %) mit 2 Dezimalstellen. Es ist der volle Zusatzbeitragssatz
    # anzugeben. Die Aufteilung in Arbeitnehmer- und Arbeitgeberanteil
    # erfolgt im Programmablauf.
    # Siehe i.Ü. auch Erläuterungen unter Pkt. 2.4.
    'KVZ': 0.0,

    # Lohnzahlungszeitraum:
    # 1 = Jahr
    # 2 = Monat
    # 3 = Woche
    # 4 = Tag
    'LZZ': 0,

    # Der als elektronisches Lohnsteuerabzugsmerkmal für den
    # Arbeitgeber nach § 39e EStG festgestellte oder in der Bescheinigung
    # für den Lohnsteuerabzug 2019 eingetragene Freibetrag für den
    # Lohnzahlungszeitraum in Cent
    'LZZFREIB': 0.0, 

    # Der als elektronisches Lohnsteuerabzugsmerkmal für den
    # Arbeitgeber nach § 39e EStG festgestellte oder in der Bescheinigung
    # für den Lohnsteuerabzug 2019 eingetragene Hinzurechnungsbetrag
    # für den Lohnzahlungszeitraum in Cent
    'LZZHINZU': 0.0, 

    # Dem Arbeitgeber mitgeteilte Beiträge des Arbeitnehmers für eine
    # private Basiskranken- bzw. Pflege-Pflichtversicherung im Sinne des
    # § 10 Absatz 1 Nummer 3 EStG in Cent; der Wert ist unabhängig vom
    # Lohnzahlungszeitraum immer als Monatsbetrag anzugeben
    'PKPV': 0.0,

    # 0 = gesetzlich krankenversicherte Arbeitnehmer
    # 1 = ausschließlich privat krankenversicherte Arbeitnehmer ohne 
    # Arbeitgeberzuschuss
    # 2 = ausschließlich privat krankenversicherte Arbeitnehmer mit 
    # Arbeitgeberzuschuss
    'PKV': 0, 

    # 1, wenn bei der sozialen Pflegeversicherung die Besonderheiten in
    # Sachsen zu berücksichtigen sind bzw. zu berücksichtigen wären
    'PVS': 0,

    # 1, wenn der Arbeitnehmer den Zuschlag zur sozialen
    # Pflegeversicherung zu zahlen hat
    'PVZ': 0,

    # Religionsgemeinschaft des Arbeitnehmers lt. elektronischer
    # Lohnsteuerabzugsmerkmale oder der Bescheinigung für den
    # Lohnsteuerabzug 2019 (bei keiner Religionszugehörigkeit = 0)
    'R': 0, 

    # Steuerpflichtiger Arbeitslohn für den Lohnzahlungszeitraum vor
    # Berücksichtigung des Versorgungsfreibetrags und des Zuschlags
    # zum Versorgungsfreibetrag, des Altersentlastungsbetrags und des
    # als elektronisches Lohnsteuerabzugsmerkmal festgestellten oder in
    # der Bescheinigung für den Lohnsteuerabzug 2019 für den
    # Lohnzahlungszeitraum eingetragenen Freibetrags bzw.
    # Hinzurechnungsbetrags in Cent
    'RE4': 0.0,

    # Sonstige Bezüge (ohne Vergütung aus mehrjähriger Tätigkeit)
    # einschließlich Sterbegeld bei Versorgungsbezügen sowie
    # Kapitalauszahlungen/Abfindungen, soweit es sich nicht um Bezüge
    # für mehrere Jahre handelt, in Cent (ggf. 0)
    'SONSTB': 0.0,

    # In SONSTB enthaltene Entschädigungen nach § 24 Nummer 1 EStG in 
    # Cent
    'SONSTENT': 0.0, 

    # Sterbegeld bei Versorgungsbezügen sowie
    # Kapitalauszahlungen/Abfindungen, soweit es sich nicht um Bezüge
    # für mehrere Jahre handelt (in SONSTB enthalten), in Cent
    'STERBE': 0.0,

    # Steuerklasse:
    # 1 = I
    # 2 = II
    # 3 = III
    # 4 = IV
    # 5 = V
    # 6 = VI
    'STKL': 0,

    # In RE4 enthaltene Versorgungsbezüge in Cent (ggf. 0) ggf. unter
    # Berücksichtigung einer geänderten Bemessungsgrundlage nach
    # § 19 Absatz 2 Satz 10 und 11 EStG
    'VBEZ': 0.0,

    # Versorgungsbezug im Januar 2005 bzw. für den ersten vollen Monat,
    # wenn der Versorgungsbezug erstmalig nach Januar 2005 gewährt
    # wurde, in Cent
    'VBEZM': 0.0,

    # Voraussichtliche Sonderzahlungen von Versorgungsbezügen im
    # Kalenderjahr des Versorgungsbeginns bei Versorgungsempfängern
    # ohne Sterbegeld, Kapitalauszahlungen/Abfindungen in Cent
    'VBEZS': 0.0,

    # In SONSTB enthaltene Versorgungsbezüge einschließlich 
    # Sterbegeld in Cent (ggf. 0)
    'VBS': 0.0,

    # Jahr, in dem der Versorgungsbezug erstmalig gewährt wurde;
    # werden mehrere Versorgungsbezüge gezahlt, wird aus
    # Vereinfachungsgründen für die Berechnung das Jahr des ältesten
    # erstmaligen Bezugs herangezogen; auf die Möglichkeit der
    # getrennten Abrechnung verschiedenartiger Bezüge (§ 39e Absatz 5a
    # EStG) wird im Übrigen verwiesen
    'VJAHR': 0,

    # Entschädigungen/Kapitalauszahlungen/Abfindungen/Nachzahlungen
    # bei Versorgungsbezügen für mehrere Jahre in Cent (ggf. 0)
    'VKAPA': 0.0,

    # Entschädigungen und Vergütung für mehrjährige Tätigkeit ohne
    # Kapitalauszahlungen und ohne Abfindungen bei
    # Versorgungsbezügen in Cent (ggf. 0)
    'VMT': 0.0,

    # Zahl der Freibeträge für Kinder (eine Dezimalstelle, nur bei
    # Steuerklassen I, II, III und IV)
    'ZKF': 0.0,

    # Zahl der Monate, für die im Kalenderjahr Versorgungsbezüge
    # gezahlt werden [nur erforderlich bei Jahresberechnung (LZZ = 1)]
    'ZMVB': 0
}


wage_tax_outputs = {
    # Bemessungsgrundlage für die Kirchenlohnsteuer in Cent
    'BK': 0.0,

    # Bemessungsgrundlage der sonstigen Bezüge (ohne Vergütung für
    # mehrjährige Tätigkeit) für die Kirchenlohnsteuer in Cent
    'BKS': 0.0, 

    # Bemessungsgrundlage der Vergütung für mehrjährige Tätigkeit für
    # die Kirchenlohnsteuer in Cent
    'BKV': 0.0,

    # Für den Lohnzahlungszeitraum einzubehaltende Lohnsteuer in Cent
    'LSTLZZ': 0.0,

    # Für den Lohnzahlungszeitraum einzubehaltender
    # Solidaritätszuschlag in Cent
    'SOLZLZZ': 0.0,

    # Solidaritätszuschlag für sonstige Bezüge (ohne Vergütung für mehr-
    # jährige Tätigkeit) in Cent
    'SOLZS': 0.0,

    # Solidaritätszuschlag für die Vergütung für mehrjährige Tätigkeit in
    # Cent
    'SOLZV': 0.0, 

    # Lohnsteuer für sonstige Bezüge (ohne Vergütung für mehrjährige
    # Tätigkeit) in Cent
    'STS': 0.0,

    # Lohnsteuer für die Vergütung für mehrjährige Tätigkeit in Cent
    'STV': 0.0,

    # Für den Lohnzahlungszeitraum berücksichtigte Beiträge des
    # Arbeitnehmers zur privaten Basis-Krankenversicherung und privaten
    # Pflege-Pflichtversicherung (ggf. auch die Mindestvorsorgepauschale)
    # in Cent beim laufenden Arbeitslohn. Für Zwecke der
    # Lohnsteuerbescheinigung sind die einzelnen Ausgabewerte
    # außerhalb des eigentlichen Lohnsteuerberechnungsprogramms zu
    # addieren; hinzuzurechnen sind auch die Ausgabewerte VKVSONST.
    'VKVLZZ': 0.0,

    # Für den Lohnzahlungszeitraum berücksichtigte Beiträge des
    # Arbeitnehmers zur privaten Basis-Krankenversicherung und privaten
    # Pflege-Pflichtversicherung (ggf. auch die Mindestvorsorgepauschale)
    # in Cent bei sonstigen Bezügen. Der Ausgabewert kann auch negativ
    # sein. Für tarifermäßigt zu besteuernde Vergütungen für mehrjährige
    # Tätigkeiten enthält der PAP keinen entsprechenden Ausgabewert.
    'VKVSONST': 0.0,

    # Verbrauchter Freibetrag bei Berechnung des laufenden Arbeitslohns,
    # in Cent
    'VFRB': 0.0,

    # Verbrauchter Freibetrag bei Berechnung des voraussichtlichen
    # Jahresarbeitslohns, in Cent
    'VFRBS1': 0.0,

    # Verbrauchter Freibetrag bei Berechnung der sonstigen Bezüge, in
    # Cent
    'VFRBS2': 0.0,

    # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach
    # dem DBA Türkei verfügbares ZVE über dem Grundfreibetrag bei der
    # Berechnung des laufenden Arbeitslohns, in Cent
    'WVFRB': 0.0, 

    # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach
    # dem DBA Türkei verfügbares ZVE über dem Grundfreibetrag bei der
    # Berechnung der sonstigen Bezüge, in Cent
    'WVFRBM': 0.0,

    # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach
    # dem DBA Türkei verfügbares ZVE über dem Grundfreibetrag bei
    'WVFRBO': 0.0,
}


wage_tax_internals = {
    # Altersentlastungsbetrag in Euro, Cent (2 Dezimalstellen)
    'ALTE': 0.0,

    # Arbeitnehmer-Pauschbetrag/Werbungskosten-Pauschbetrag in Euro
    'ANP': 0.0,

    # Auf den Lohnzahlungszeitraum entfallender Anteil von Jahreswerten
    # auf ganze Cent abgerundet
    'ANTEIL1': 0.0,

    # Beitragsbemessungsgrenze in der gesetzlichen
    # Krankenversicherung und der sozialen Pflegeversicherung in Euro
    'BBGKVPV': 0.0,

    # Allgemeine Beitragsbemessungsgrenze in der allgemeinen
    # Rentenversicherung in Euro
    'BBGRV': 0.0,

    # Bemessungsgrundlage für Altersentlastungsbetrag in Euro, Cent
    # (2 Dezimalstellen)
    'BMG': 0.0,

    # Differenz zwischen ST1 und ST2 in Euro
    'DIFF': 0.0, 

    # Entlastungsbetrag für Alleinerziehende in Euro
    'EFA': 0.0,

    # Versorgungsfreibetrag in Euro, Cent (2 Dezimalstellen)
    'FVB': 0.0, 

    # Versorgungsfreibetrag in Euro, Cent (2 Dezimalstellen) für die
    # Berechnung der Lohnsteuer für den sonstigen Bezug
    'FVBSO': 0.0,

    # Zuschlag zum Versorgungsfreibetrag in Euro
    'FVBZ': 0.0, 

    # Zuschlag zum Versorgungsfreibetrag in Euro für die Berechnung der
    # Lohnsteuer beim sonstigen Bezug
    'FVBZSO': 0.0,

    # Grundfreibetrag in Euro
    'GFB': 0.0,

    # Maximaler Altersentlastungsbetrag in Euro
    'HBALTE': 0.0, 

    # Maßgeblicher maximaler Versorgungsfreibetrag in Euro
    'HFVB': 0.0,

    # Maßgeblicher maximaler Zuschlag zum Versorgungsfreibetrag in
    # Euro, Cent (2 Dezimalstellen)
    'HFVBZ': 0.0,

    # Maßgeblicher maximaler Zuschlag zum Versorgungsfreibetrag in
    # Euro, Cent (2 Dezimalstellen) für die Berechnung der Lohnsteuer für
    # den sonstigen Bezug
    'HFVBZSO': 0.0,

    # Zwischenfeld zu X für die Berechnung der Steuer nach § 39b
    # Absatz 2 Satz 7 EStG in Euro
    'HOCH': 0.0,

    # Nummer der Tabellenwerte für Versorgungsparameter
    'J': 0, 

    # Jahressteuer nach § 51a EStG, aus der Solidaritätszuschlag und
    # Bemessungsgrundlage für die Kirchenlohnsteuer ermittelt werden, in
    # Euro
    'JBMG': 0.0,

    # Auf einen Jahreslohn hochgerechneter LZZFREIB in Euro, Cent
    # (2 Dezimalstellen)
    'JLFREIB': 0.0,

    # Auf einen Jahreslohn hochgerechneter LZZHINZU in Euro, Cent
    # (2 Dezimalstellen)
    'JLHINZU': 0.0,

    'JW': 0.0,
    # Jahreswert, dessen Anteil für einen Lohnzahlungszeitraum in
    # UPANTEIL errechnet werden soll, in Cent

    # Nummer der Tabellenwerte für Parameter bei
    # Altersentlastungsbetrag
    'K': 0,

    # Merker für Berechnung Lohnsteuer für mehrjährige Tätigkeit
    # 0 = normale Steuerberechnung
    # 1 = Steuerberechnung für mehrjährige Tätigkeit
    # 2 = Ermittlung der Vorsorgepauschale ohne Entschädigungen i.S.d.
    # § 24 Nummer 1 EStG
    'KENNVMT': 0,

    # Summe der Freibeträge für Kinder in Euro
    'KFB': 0.0, 

    # Beitragssatz des Arbeitgebers zur Krankenversicherung unter
    # Berücksichtigung des durchschnittlichen Zusatzbeitragssatzes für die
    # Ermittlung des Arbeitgeberzuschusses (5 Dezimalstellen)
    'KVSATZAG': 0.0,

    # Beitragssatz des Arbeitnehmers zur Krankenversicherung
    # (5 Dezimalstellen)
    'KVSATZAN': 0.0,

    # Kennzahl für die Einkommensteuer-Tarifarten:
    # 1 = Grundtarif
    # 2 = Splittingverfahren
    'KZTAB': 0,

    # Jahreslohnsteuer in Euro
    'LSTJAHR': 0.0, 

    # Zwischenfelder der Jahreslohnsteuer in Cent
    'LST1': 0.0, 
    'LST2': 0.0, 
    'LST3': 0.0, 
    'LSTOSO': 0.0, 
    'LSTSO': 0.0, 

    MIST Mindeststeuer für die Steuerklassen V und VI in Euro
    PVSATZAG Beitragssatz des Arbeitgebers zur Pflegeversicherung
    (5 Dezimalstellen)
    PVSATZAN Beitragssatz des Arbeitnehmers zur Pflegeversicherung
    (5 Dezimalstellen)
    RVSATZAN Beitragssatz des Arbeitnehmers in der allgemeinen gesetzlichen
    Rentenversicherung (4 Dezimalstellen)
    RW Rechenwert in Gleitkommadarstellung
    SAP Sonderausgaben-Pauschbetrag in Euro
    SOLZFREI Freigrenze für den Solidaritätszuschlag in Euro
    SOLZJ Solidaritätszuschlag auf die Jahreslohnsteuer in Euro, Cent
    (2 Dezimalstellen)
    SOLZMIN Zwischenwert für den Solidaritätszuschlag auf die Jahreslohnsteuer
    in Euro, Cent (2 Dezimalstellen)
    ST Tarifliche Einkommensteuer in Euro
    ST1 Tarifliche Einkommensteuer auf das 1,25-fache ZX in Euro
    ST2 Tarifliche Einkommensteuer auf das 0,75-fache ZX in Euro
    STOVMT Zwischenfeld zur Ermittlung der Steuer auf Vergütungen für
    mehrjährige Tätigkeit in Euro
    TAB1 Tabelle für die Prozentsätze des Versorgungsfreibetrags
    TAB2 Tabelle für die Höchstbeträge des Versorgungsfreibetrags
    TAB3 Tabelle für die Zuschläge zum Versorgungsfreibetrag
    TAB4 Tabelle für die Prozentsätze des Altersentlastungsbetrags
    TAB5 Tabelle für die Höchstbeträge des Altersentlastungsbetrags
    TBSVORV Teilbetragssatz der Vorsorgepauschale für die Rentenversicherung
    (2 Dezimalstellen)
    VBEZB Bemessungsgrundlage für den Versorgungsfreibetrag in Cent
    VBEZBSO Bemessungsgrundlage für den Versorgungsfreibetrag in Cent für
    den sonstigen Bezug
    VERGL Zwischenfeld zu X für die Berechnung der Steuer nach § 39b
    Absatz 2 Satz 7 EStG in Euro
    VHB Höchstbetrag der Mindestvorsorgepauschale für die Kranken- und
    Pflegeversicherung in Euro, Cent (2 Dezimalstellen)
    VKV Jahreswert der berücksichtigten Beiträge zur privaten Basis-
    Krankenversicherung und privaten Pflege-Pflichtversicherung (ggf.
    auch die Mindestvorsorgepauschale) in Cent
    VSP Vorsorgepauschale mit Teilbeträgen für die Rentenversicherung
    sowie die gesetzliche Kranken- und soziale Pflegeversicherung nach
    fiktiven Beträgen oder ggf. für die private Basiskrankenversicherung
    und private Pflege-Pflichtversicherung in Euro, Cent
    (2 Dezimalstellen)
    VSPN Vorsorgepauschale mit Teilbeträgen für die Rentenversicherung
    sowie der Mindestvorsorgepauschale für die Kranken- und
    Pflegeversicherung in Euro, Cent (2 Dezimalstellen)
    VSP1 Zwischenwert 1 bei der Berechnung der Vorsorgepauschale in Euro,
    Cent (2 Dezimalstellen)
    VSP2 Zwischenwert 2 bei der Berechnung der Vorsorgepauschale in Euro,
    Cent (2 Dezimalstellen)
    VSP3 Vorsorgepauschale mit Teilbeträgen für die gesetzliche Kranken-
    und soziale Pflegeversicherung nach fiktiven Beträgen oder ggf. für
    die private Basiskrankenversicherung und private Pflege-
    Pflichtversicherung in Euro, Cent (2 Dezimalstellen)
    W1STKL5 Erster Grenzwert in Steuerklasse V/VI in Euro
    W2STKL5 Zweiter Grenzwert in Steuerklasse V/VI in Euro
    W3STKL5 Dritter Grenzwert in Steuerklasse V/VI in Euro
    X Zu versteuerndes Einkommen gem. § 32a Absatz 1 und 5 EStG in
    Euro, Cent (2 Dezimalstellen)
    Y Gem. § 32a Absatz 1 EStG (6 Dezimalstellen)
    ZRE4 Auf einen Jahreslohn hochgerechnetes RE4 in Euro, Cent
    (2 Dezimalstellen) nach Abzug der Freibeträge nach § 39b Absatz 2
    Satz 3 und 4 EStG
    ZRE4J Auf einen Jahreslohn hochgerechnetes RE4 in Euro, Cent
    (2 Dezimalstellen)
    ZRE4VP Auf einen Jahreslohn hochgerechnetes RE4, ggf. nach Abzug der
    Entschädigungen i.S.d. § 24 Nummer 1 EStG in Euro, Cent (2
    Dezimalstellen)
    ZTABFB Feste Tabellenfreibeträge (ohne Vorsorgepauschale) in Euro, Cent
    (2 Dezimalstellen)
    ZVBEZ Auf einen Jahreslohn hochgerechnetes VBEZ abzüglich FVB in
    Euro, Cent (2 Dezimalstellen)
    ZVBEZJ Auf einen Jahreslohn hochgerechnetes VBEZ in Euro, Cent
    (2 Dezimalstellen)
    ZVE Zu versteuerndes Einkommen in Euro, Cent (2 Dezimalstellen)
    ZX Zwischenfeld zu X für die Berechnung der Steuer nach § 39b
    Absatz 2 Satz 7 EStG in Euro
    ZZX Zwischenfeld zu X für die Berech
}


def calculate_wage_tax(inputs):
    ''' Programmablaufplan für die Berechnung der Lohnsteuer 2019'''
    wage_tax_inputs.update(inputs)
    # todo: init internals?

    # MPARA()
    # MRE4JL()
    # VBEZBSO = 0
    # KENNVMT = 0
    # MRE4ABZ()
    # MBERECH()
    # MSONST()
    # MVMT()

    return wage_tax_outputs


def mpara(wage_tax_inputs):
    ''' Zuweisung von Werten für bestimmte Sozialversicherungsparameter '''
    if wage_tax_inputs['KRV'] < 2:
        pass
    pass
    # todo
    