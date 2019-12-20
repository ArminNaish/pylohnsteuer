from decimal import Decimal

tab1 = {
     1: Decimal('0.400'),
     2: Decimal('0.384'),
     3: Decimal('0.368'),
     4: Decimal('0.352'),
     5: Decimal('0.336'),
     6: Decimal('0.320'),
     7: Decimal('0.304'),
     8: Decimal('0.288'),
     9: Decimal('0.272'),
    10: Decimal('0.256'),
    11: Decimal('0.240'),
    12: Decimal('0.224'),
    13: Decimal('0.208'),
    14: Decimal('0.192'),
    15: Decimal('0.176'),
    16: Decimal('0.160'),
    17: Decimal('0.152'),
    18: Decimal('0.144'),
    19: Decimal('0.136'),
    20: Decimal('0.128'),
    21: Decimal('0.120'),
    22: Decimal('0.112'),
    23: Decimal('0.104'),
    24: Decimal('0.096'),
    25: Decimal('0.088'),
    26: Decimal('0.080'),
    27: Decimal('0.072'),
    28: Decimal('0.064'),
    29: Decimal('0.056'),
    30: Decimal('0.048'),
    31: Decimal('0.040'),
    32: Decimal('0.032'),
    33: Decimal('0.024'),
    34: Decimal('0.016'),
    35: Decimal('0.008'),
    36: Decimal('0.000'),
}

tab2 = {
     1: Decimal('3000'),
     2: Decimal('2880'),
     3: Decimal('2760'),
     4: Decimal('2640'),
     5: Decimal('2520'),
     6: Decimal('2400'),
     7: Decimal('2280'),
     8: Decimal('2160'),
     9: Decimal('2040'),
    10: Decimal('1920'),
    11: Decimal('1800'),
    12: Decimal('1680'),
    13: Decimal('1560'),
    14: Decimal('1440'),
    15: Decimal('1320'),
    16: Decimal('1200'),
    17: Decimal('1140'),
    18: Decimal('1080'),
    19: Decimal('1020'),
    20: Decimal('960'),
    21: Decimal('900'),
    22: Decimal('840'),
    23: Decimal('780'),
    24: Decimal('720'),
    25: Decimal('660'),
    26: Decimal('600'),
    27: Decimal('540'),
    28: Decimal('480'),
    29: Decimal('420'),
    30: Decimal('360'),
    31: Decimal('300'),
    32: Decimal('240'),
    33: Decimal('180'),
    34: Decimal('120'),
    35: Decimal('60'),
    36: Decimal(0),
}

tab3 = {
     1: Decimal('900'),
     2: Decimal('864'),
     3: Decimal('828'),
     4: Decimal('792'),
     5: Decimal('756'),
     6: Decimal('720'),
     7: Decimal('684'),
     8: Decimal('648'),
     9: Decimal('612'),
    10: Decimal('576'),
    11: Decimal('540'),
    12: Decimal('504'),
    13: Decimal('468'),
    14: Decimal('432'),
    15: Decimal('396'),
    16: Decimal('360'),
    17: Decimal('342'),
    18: Decimal('324'),
    19: Decimal('306'),
    20: Decimal('288'),
    21: Decimal('270'),
    22: Decimal('252'),
    23: Decimal('234'),
    24: Decimal('216'),
    25: Decimal('198'),
    26: Decimal('180'),
    27: Decimal('162'),
    28: Decimal('144'),
    29: Decimal('126'),
    30: Decimal('108'),
    31: Decimal('90'),
    32: Decimal('72'),
    33: Decimal('54'),
    34: Decimal('36'),
    35: Decimal('18'),
    36: Decimal(0),
}

tab4 = {
     1: Decimal('0.400'),
     2: Decimal('0.384'),
     3: Decimal('0.368'),
     4: Decimal('0.352'),
     5: Decimal('0.336'),
     6: Decimal('0.320'),
     7: Decimal('0.304'),
     8: Decimal('0.288'),
     9: Decimal('0.272'),
    10: Decimal('0.256'),
    11: Decimal('0.240'),
    12: Decimal('0.224'),
    13: Decimal('0.208'),
    14: Decimal('0.000'),
    15: Decimal('0.192'),
    16: Decimal('0.176'),
    17: Decimal('0.160'),
    18: Decimal('0.152'),
    19: Decimal('0.144'),
    20: Decimal('0.128'),
    21: Decimal('0.120'),
    22: Decimal('0.112'),
    23: Decimal('0.104'),
    24: Decimal('0.096'),
    25: Decimal('0.088'),
    26: Decimal('0.080'),
    27: Decimal('0.072'),
    28: Decimal('0.064'),
    29: Decimal('0.056'),
    30: Decimal('0.048'),
    31: Decimal('0.040'),
    32: Decimal('0.032'),
    33: Decimal('0.024'),
    34: Decimal('0.016'),
    35: Decimal('0.008'),
    36: Decimal('0.000'),
}

tab5 = {
     1: Decimal('1900'),
     2: Decimal('1824'),
     3: Decimal('1748'),
     4: Decimal('1672'),
     5: Decimal('1596'),
     6: Decimal('1520'),
     7: Decimal('1444'),
     8: Decimal('1368'),
     9: Decimal('1292'),
    10: Decimal('1216'),
    11: Decimal('1140'),
    12: Decimal('1064'),
    13: Decimal('988'),
    14: Decimal('912'),
    15: Decimal('836'),
    16: Decimal('760'),
    17: Decimal('722'),
    18: Decimal('684'),
    19: Decimal('646'),
    20: Decimal('608'),
    21: Decimal('570'),
    22: Decimal('532'),
    23: Decimal('494'),
    24: Decimal('456'),
    25: Decimal('418'),
    26: Decimal('380'),
    27: Decimal('342'),
    28: Decimal('304'),
    29: Decimal('266'),
    30: Decimal('228'),
    31: Decimal('190'),
    32: Decimal('152'),
    33: Decimal('114'),
    34: Decimal('76'),
    35: Decimal('38'),
    36: Decimal(0),
}

wage_tax_inputs = {
    # 1, wenn die Anwendung des Faktorverfahrens gewählt wurde
    # (nur in Steuerklasse IV)
    'AF': 0,

    # Auf die Vollendung des 64. Lebensjahres folgendes Kalenderjahr
    # (erforderlich, wenn ALTER1=1)
    'AJAHR': 0,

    # 1, wenn das 64. Lebensjahr vor Beginn des Kalenderjahres vollendet wurde,
    # in dem der Lohnzahlungszeitraum endet (§ 24a EStG), sonst = 0
    'ALTER1': 0,

    # In VKAPA und VMT enthaltene Entschädigungen nach § 24 Nummer 1 EStG
    # in Cent
    'ENTSCH': Decimal(0),

    # eingetragener Faktor mit drei Nachkommastellen
    'F': Decimal(0),

    # Jahresfreibetrag für die Ermittlung der Lohnsteuer für die sonstigen
    # Bezüge nach Maßgabe der elektronischen Lohnsteuerabzugsmerkmale
    # nach § 39e EStG oder der Eintragung auf der Bescheinigung für den
    # Lohnsteuerabzug 2019 in Cent (ggf. 0)
    'JFREIB': Decimal(0),

    # Jahreshinzurechnungsbetrag für die Ermittlung der Lohnsteuer für
    # die sonstigen Bezüge nach Maßgabe der elektronischen
    # Lohnsteuerabzugsmerkmale nach § 39e EStG oder der Eintragung
    # auf der Bescheinigung für den Lohnsteuerabzug 2019 in Cent (ggf. 0)
    'JHINZU': Decimal(0),

    # Voraussichtlicher Jahresarbeitslohn ohne sonstige Bezüge und ohne
    # Vergütung für mehrjährige Tätigkeit in Cent. Anmerkung: Die
    # Eingabe dieses Feldes (ggf. 0) ist erforderlich bei Eingaben zu
    # sonstigen Bezügen (Felder SONSTB, VMT oder VKAPA).
    # Sind in einem vorangegangenen Abrechnungszeitraum bereits
    # sonstige Bezüge gezahlt worden, so sind sie dem voraussichtlichen
    # Jahresarbeitslohn hinzuzurechnen. Vergütungen für mehrjährige
    # Tätigkeit aus einem vorangegangenen Abrechnungszeitraum wer-
    # den in voller Höhe hinzugerechnet.
    'JRE4': Decimal(0),

    # In JRE4 enthaltene Entschädigungen nach § 24 Nummer 1 EStG in Cent
    'JRE4ENT': Decimal(0),

    # In JRE4 enthaltene Versorgungsbezüge in Cent (ggf. 0)
    'JVBEZ': Decimal(0),

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
    'KVZ': Decimal(0),

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
    'LZZFREIB': Decimal(0),

    # Der als elektronisches Lohnsteuerabzugsmerkmal für den
    # Arbeitgeber nach § 39e EStG festgestellte oder in der Bescheinigung
    # für den Lohnsteuerabzug 2019 eingetragene Hinzurechnungsbetrag
    # für den Lohnzahlungszeitraum in Cent
    'LZZHINZU': Decimal(0),

    # Dem Arbeitgeber mitgeteilte Beiträge des Arbeitnehmers für eine
    # private Basiskranken- bzw. Pflege-Pflichtversicherung im Sinne des
    # § 10 Absatz 1 Nummer 3 EStG in Cent; der Wert ist unabhängig vom
    # Lohnzahlungszeitraum immer als Monatsbetrag anzugeben
    'PKPV': Decimal(0),

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
    'RE4': Decimal(0),

    # Sonstige Bezüge (ohne Vergütung aus mehrjähriger Tätigkeit)
    # einschließlich Sterbegeld bei Versorgungsbezügen sowie
    # Kapitalauszahlungen/Abfindungen, soweit es sich nicht um Bezüge
    # für mehrere Jahre handelt, in Cent (ggf. 0)
    'SONSTB': Decimal(0),

    # In SONSTB enthaltene Entschädigungen nach § 24 Nummer 1 EStG in
    # Cent
    'SONSTENT': 0,

    # Sterbegeld bei Versorgungsbezügen sowie
    # Kapitalauszahlungen/Abfindungen, soweit es sich nicht um Bezüge
    # für mehrere Jahre handelt (in SONSTB enthalten), in Cent
    'STERBE': Decimal(0),

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
    'VBEZ': Decimal(0),

    # Versorgungsbezug im Januar 2005 bzw. für den ersten vollen Monat,
    # wenn der Versorgungsbezug erstmalig nach Januar 2005 gewährt
    # wurde, in Cent
    'VBEZM': Decimal(0),

    # Voraussichtliche Sonderzahlungen von Versorgungsbezügen im
    # Kalenderjahr des Versorgungsbeginns bei Versorgungsempfängern
    # ohne Sterbegeld, Kapitalauszahlungen/Abfindungen in Cent
    'VBEZS': Decimal(0),

    # In SONSTB enthaltene Versorgungsbezüge einschließlich
    # Sterbegeld in Cent (ggf. 0)
    'VBS': Decimal(0),

    # Jahr, in dem der Versorgungsbezug erstmalig gewährt wurde;
    # werden mehrere Versorgungsbezüge gezahlt, wird aus
    # Vereinfachungsgründen für die Berechnung das Jahr des ältesten
    # erstmaligen Bezugs herangezogen; auf die Möglichkeit der
    # getrennten Abrechnung verschiedenartiger Bezüge (§ 39e Absatz 5a
    # EStG) wird im Übrigen verwiesen
    'VJAHR': 0,

    # Entschädigungen/Kapitalauszahlungen/Abfindungen/Nachzahlungen
    # bei Versorgungsbezügen für mehrere Jahre in Cent (ggf. 0)
    'VKAPA': Decimal(0),

    # Entschädigungen und Vergütung für mehrjährige Tätigkeit ohne
    # Kapitalauszahlungen und ohne Abfindungen bei
    # Versorgungsbezügen in Cent (ggf. 0)
    'VMT': Decimal(0),

    # Zahl der Freibeträge für Kinder (eine Dezimalstelle, nur bei
    # Steuerklassen I, II, III und IV)
    'ZKF': Decimal(0),

    # Zahl der Monate, für die im Kalenderjahr Versorgungsbezüge
    # gezahlt werden [nur erforderlich bei Jahresberechnung (LZZ = 1)]
    'ZMVB': 0
}


wage_tax_outputs = {
    # Bemessungsgrundlage für die Kirchenlohnsteuer in Cent
    'BK': Decimal(0),

    # Bemessungsgrundlage der sonstigen Bezüge (ohne Vergütung für
    # mehrjährige Tätigkeit) für die Kirchenlohnsteuer in Cent
    'BKS': Decimal(0),

    # Bemessungsgrundlage der Vergütung für mehrjährige Tätigkeit für
    # die Kirchenlohnsteuer in Cent
    'BKV': Decimal(0),

    # Für den Lohnzahlungszeitraum einzubehaltende Lohnsteuer in Cent
    'LSTLZZ': Decimal(0),

    # Für den Lohnzahlungszeitraum einzubehaltender
    # Solidaritätszuschlag in Cent
    'SOLZLZZ': Decimal(0),

    # Solidaritätszuschlag für sonstige Bezüge (ohne Vergütung für mehr-
    # jährige Tätigkeit) in Cent
    'SOLZS': Decimal(0),

    # Solidaritätszuschlag für die Vergütung für mehrjährige Tätigkeit in
    # Cent
    'SOLZV': 0,

    # Lohnsteuer für sonstige Bezüge (ohne Vergütung für mehrjährige
    # Tätigkeit) in Cent
    'STS': Decimal(0),

    # Lohnsteuer für die Vergütung für mehrjährige Tätigkeit in Cent
    'STV': Decimal(0),

    # Für den Lohnzahlungszeitraum berücksichtigte Beiträge des
    # Arbeitnehmers zur privaten Basis-Krankenversicherung und privaten
    # Pflege-Pflichtversicherung (ggf. auch die Mindestvorsorgepauschale)
    # in Cent beim laufenden Arbeitslohn. Für Zwecke der
    # Lohnsteuerbescheinigung sind die einzelnen Ausgabewerte
    # außerhalb des eigentlichen Lohnsteuerberechnungsprogramms zu
    # addieren; hinzuzurechnen sind auch die Ausgabewerte VKVSONST.
    'VKVLZZ': Decimal(0),

    # Für den Lohnzahlungszeitraum berücksichtigte Beiträge des
    # Arbeitnehmers zur privaten Basis-Krankenversicherung und privaten
    # Pflege-Pflichtversicherung (ggf. auch die Mindestvorsorgepauschale)
    # in Cent bei sonstigen Bezügen. Der Ausgabewert kann auch negativ
    # sein. Für tarifermäßigt zu besteuernde Vergütungen für mehrjährige
    # Tätigkeiten enthält der PAP keinen entsprechenden Ausgabewert.
    'VKVSONST': Decimal(0),

    # Verbrauchter Freibetrag bei Berechnung des laufenden Arbeitslohns,
    # in Cent
    'VFRB': Decimal(0),

    # Verbrauchter Freibetrag bei Berechnung des voraussichtlichen
    # Jahresarbeitslohns, in Cent
    'VFRBS1': Decimal(0),

    # Verbrauchter Freibetrag bei Berechnung der sonstigen Bezüge, in
    # Cent
    'VFRBS2': 0,

    # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach
    # dem DBA Türkei verfügbares ZVE über dem Grundfreibetrag bei der
    # Berechnung des laufenden Arbeitslohns, in Cent
    'WVFRB': Decimal(0),

    # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach
    # dem DBA Türkei verfügbares ZVE über dem Grundfreibetrag bei der
    # Berechnung der sonstigen Bezüge, in Cent
    'WVFRBM': Decimal(0),

    # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach
    # dem DBA Türkei verfügbares ZVE über dem Grundfreibetrag bei der
    # Berechnung des voraussichtlichen Jahresarbeitslohns, in Cent
    'WVFRBO': Decimal(0)
}


wage_tax_internals = {
    # Altersentlastungsbetrag in Euro, Cent (2 Dezimalstellen)
    'ALTE': Decimal(0),

    # Arbeitnehmer-Pauschbetrag/Werbungskosten-Pauschbetrag in Euro
    'ANP': Decimal(0),

    # Auf den Lohnzahlungszeitraum entfallender Anteil von Jahreswerten
    # auf ganze Cent abgerundet
    'ANTEIL1': 0,

    # Beitragsbemessungsgrenze in der gesetzlichen
    # Krankenversicherung und der sozialen Pflegeversicherung in Euro
    'BBGKVPV': Decimal(0),

    # Allgemeine Beitragsbemessungsgrenze in der allgemeinen
    # Rentenversicherung in Euro
    'BBGRV': Decimal(0),

    # Bemessungsgrundlage für Altersentlastungsbetrag in Euro, Cent
    # (2 Dezimalstellen)
    'BMG': Decimal(0),

    # Differenz zwischen ST1 und ST2 in Euro
    'DIFF': Decimal(0),

    # Entlastungsbetrag für Alleinerziehende in Euro
    'EFA': Decimal(0),

    # Versorgungsfreibetrag in Euro, Cent (2 Dezimalstellen)
    'FVB': Decimal(0),

    # Versorgungsfreibetrag in Euro, Cent (2 Dezimalstellen) für die
    # Berechnung der Lohnsteuer für den sonstigen Bezug
    'FVBSO': Decimal(0),

    # Zuschlag zum Versorgungsfreibetrag in Euro
    'FVBZ': Decimal(0),

    # Zuschlag zum Versorgungsfreibetrag in Euro für die Berechnung der
    # Lohnsteuer beim sonstigen Bezug
    'FVBZSO': Decimal(0),

    # Grundfreibetrag in Euro
    'GFB': Decimal(0),

    # Maximaler Altersentlastungsbetrag in Euro
    'HBALTE': Decimal(0),

    # Maßgeblicher maximaler Versorgungsfreibetrag in Euro
    'HFVB': Decimal(0),

    # Maßgeblicher maximaler Zuschlag zum Versorgungsfreibetrag in
    # Euro, Cent (2 Dezimalstellen)
    'HFVBZ': Decimal(0),

    # Maßgeblicher maximaler Zuschlag zum Versorgungsfreibetrag in
    # Euro, Cent (2 Dezimalstellen) für die Berechnung der Lohnsteuer für
    # den sonstigen Bezug
    'HFVBZSO': Decimal(0),

    # Zwischenfeld zu X für die Berechnung der Steuer nach § 39b
    # Absatz 2 Satz 7 EStG in Euro
    'HOCH': Decimal(0),

    # Nummer der Tabellenwerte für Versorgungsparameter
    'J': 0,

    # Jahressteuer nach § 51a EStG, aus der Solidaritätszuschlag und
    # Bemessungsgrundlage für die Kirchenlohnsteuer ermittelt werden, in
    # Euro
    'JBMG': Decimal(0),

    # Auf einen Jahreslohn hochgerechneter LZZFREIB in Euro, Cent
    # (2 Dezimalstellen)
    'JLFREIB': Decimal(0),

    # Auf einen Jahreslohn hochgerechneter LZZHINZU in Euro, Cent
    # (2 Dezimalstellen)
    'JLHINZU': Decimal(0),

    # Jahreswert, dessen Anteil für einen Lohnzahlungszeitraum in
    # UPANTEIL errechnet werden soll, in Cent
    'JW': 0,

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
    'KFB': Decimal(0),

    # Beitragssatz des Arbeitgebers zur Krankenversicherung unter
    # Berücksichtigung des durchschnittlichen Zusatzbeitragssatzes für die
    # Ermittlung des Arbeitgeberzuschusses (5 Dezimalstellen)
    'KVSATZAG': Decimal(0),

    # Beitragssatz des Arbeitnehmers zur Krankenversicherung
    # (5 Dezimalstellen)
    'KVSATZAN': Decimal(0),

    # Kennzahl für die Einkommensteuer-Tarifarten:
    # 1 = Grundtarif
    # 2 = Splittingverfahren
    'KZTAB': 0,

    # Jahreslohnsteuer in Euro
    'LSTJAHR': Decimal(0),

    # Zwischenfelder der Jahreslohnsteuer in Cent
    'LST1': 0,
    'LST2': 0,
    'LST3': 0,
    'LSTOSO': 0,
    'LSTSO': 0,

    # Mindeststeuer für die Steuerklassen V und VI in Euro
    'MIST': Decimal(0),

    # Beitragssatz des Arbeitgebers zur Pflegeversicherung
    # (5 Dezimalstellen)
    'PVSATZAG': Decimal(0),

    # Beitragssatz des Arbeitnehmers zur Pflegeversicherung
    # (5 Dezimalstellen)
    'PVSATZAN': Decimal(0),

    # Beitragssatz des Arbeitnehmers in der allgemeinen gesetzlichen
    # Rentenversicherung (4 Dezimalstellen)
    'RVSATZAN': Decimal(0),

    # Rechenwert in Gleitkommadarstellung
    'RW': Decimal(0),

    # Sonderausgaben-Pauschbetrag in Euro
    'SAP': Decimal(0),

    # Freigrenze für den Solidaritätszuschlag in Euro
    'SOLZFREI': Decimal(0),

    # Solidaritätszuschlag auf die Jahreslohnsteuer in Euro, Cent
    # (2 Dezimalstellen)
    'SOLZJ': Decimal(0),

    # Zwischenwert für den Solidaritätszuschlag auf die Jahreslohnsteuer
    # in Euro, Cent (2 Dezimalstellen)
    'SOLZMIN': Decimal(0),

    # Tarifliche Einkommensteuer in Euro
    'ST': Decimal(0),

    # Tarifliche Einkommensteuer auf das 1,25-fache ZX in Euro
    'ST1': Decimal(0),

    # Tarifliche Einkommensteuer auf das 0,75-fache ZX in Euro
    'ST2': Decimal(0),

    # Zwischenfeld zur Ermittlung der Steuer auf Vergütungen für
    # mehrjährige Tätigkeit in Euro
    'STOVMT': Decimal(0),

    # Tabelle für die Prozentsätze des Versorgungsfreibetrags
    'TAB1': tab1,

    # Tabelle für die Höchstbeträge des Versorgungsfreibetrags
    'TAB2': tab2,

    # Tabelle für die Zuschläge zum Versorgungsfreibetrag
    'TAB3': tab3,

    # Tabelle für die Prozentsätze des Altersentlastungsbetrags
    'TAB4': tab4,

    #  Tabelle für die Höchstbeträge des Altersentlastungsbetrags
    'TAB5': tab5,

    # Teilbetragssatz der Vorsorgepauschale für die Rentenversicherung
    # (2 Dezimalstellen)
    'TBSVORV': Decimal(0),

    # Bemessungsgrundlage für den Versorgungsfreibetrag in Cent
    'VBEZB': 0,

    # Bemessungsgrundlage für den Versorgungsfreibetrag in Cent für
    # den sonstigen Bezug
    'VBEZBSO': 0,

    # Zwischenfeld zu X für die Berechnung der Steuer nach § 39b
    # Absatz 2 Satz 7 EStG in Euro
    'VERGL': Decimal(0),

    # Höchstbetrag der Mindestvorsorgepauschale für die Kranken- und
    # Pflegeversicherung in Euro, Cent (2 Dezimalstellen)
    'VHB': Decimal(0),

    # Jahreswert der berücksichtigten Beiträge zur privaten Basis-
    # Krankenversicherung und privaten Pflege-Pflichtversicherung (ggf.
    # auch die Mindestvorsorgepauschale) in Cent
    'VKV': 0,

    # Vorsorgepauschale mit Teilbeträgen für die Rentenversicherung
    # sowie die gesetzliche Kranken- und soziale Pflegeversicherung nach
    # fiktiven Beträgen oder ggf. für die private Basiskrankenversicherung
    # und private Pflege-Pflichtversicherung in Euro, Cent
    # (2 Dezimalstellen)
    'VSP': Decimal(0),

    # Vorsorgepauschale mit Teilbeträgen für die Rentenversicherung
    # sowie der Mindestvorsorgepauschale für die Kranken- und
    # Pflegeversicherung in Euro, Cent (2 Dezimalstellen)
    'VSPN': Decimal(0),

    # Zwischenwert 1 bei der Berechnung der Vorsorgepauschale in Euro,
    # Cent (2 Dezimalstellen)
    'VSP1': Decimal(0),

    # Zwischenwert 2 bei der Berechnung der Vorsorgepauschale in Euro,
    # Cent (2 Dezimalstellen)
    'VSP2': Decimal(0),

    # Vorsorgepauschale mit Teilbeträgen für die gesetzliche Kranken-
    # und soziale Pflegeversicherung nach fiktiven Beträgen oder ggf. für
    # die private Basiskrankenversicherung und private Pflege-
    # Pflichtversicherung in Euro, Cent (2 Dezimalstellen)
    'VSP3': Decimal(0),

    # Erster Grenzwert in Steuerklasse V/VI in Euro
    'W1STKL5': 0,

    # Zweiter Grenzwert in Steuerklasse V/VI in Euro
    'W2STKL5': 0,

    # Dritter Grenzwert in Steuerklasse V/VI in Euro
    'W3STKL5': 0,

    # Zu versteuerndes Einkommen gem. § 32a Absatz 1 und 5 EStG in
    # Euro, Cent (2 Dezimalstellen)
    'X': Decimal(0),

    # Gem. § 32a Absatz 1 EStG (6 Dezimalstellen)
    'Y': Decimal(0),

    # Auf einen Jahreslohn hochgerechnetes RE4 in Euro, Cent
    # (2 Dezimalstellen) nach Abzug der Freibeträge nach § 39b Absatz 2
    # Satz 3 und 4 EStG
    'ZRE4': Decimal(0),

    # Auf einen Jahreslohn hochgerechnetes RE4 in Euro, Cent
    # (2 Dezimalstellen)
    'ZRE4J': Decimal(0),

    # Auf einen Jahreslohn hochgerechnetes RE4, ggf. nach Abzug der
    # Entschädigungen i.S.d. § 24 Nummer 1 EStG in Euro, Cent (2
    # Dezimalstellen)
    'ZRE4VP': Decimal(0),

    # Feste Tabellenfreibeträge (ohne Vorsorgepauschale) in Euro, Cent
    # (2 Dezimalstellen)
    'ZTABFB': Decimal(0),

    # Auf einen Jahreslohn hochgerechnetes VBEZ abzüglich FVB in
    # Euro, Cent (2 Dezimalstellen)
    'ZVBEZ': Decimal(0),

    # Auf einen Jahreslohn hochgerechnetes VBEZ in Euro, Cent
    # (2 Dezimalstellen)
    'ZVBEZJ': Decimal(0),

    # Zu versteuerndes Einkommen in Euro, Cent (2 Dezimalstellen)
    'ZVE': Decimal(0),

    # Zwischenfeld zu X für die Berechnung der Steuer nach § 39b
    # Absatz 2 Satz 7 EStG in Euro
    'ZX': Decimal(0),

    # Zwischenfeld zu X für die Berechnung der Steuer nach § 39b
    # Absatz 2 Satz 7 EStG in Euro
    'ZZX': Decimal(0)
}

