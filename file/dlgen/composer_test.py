from .composer import Composer


def test_get_composed_chad():
    data_chad = {
        'customerId': 'L084054624',
        'issuerName': 'Oklahoma',
        'issuerIN': '636058',
        'version': '05',
        'jurVersion': '00',
        'numEntries': '02',

        'familyName': 'Galvan',
        'familyNameT': 'N',
        'firstName': 'Chad',
        'firstNameT': 'N',
        'middleName': 'Anthony',
        'middleNameT': 'N',
        'vehicleClass': 'D',
        'jurRestriction': 'None',
        'jurEndorsement': 'NONE',
        'sex': '1',
        'height': '511',
        'eyeColor': 'BRO',
        'street': '1621 Ne 11th St',
        'city': 'Moore',
        'state': 'OK',
        'country': 'USA',
        'postal': '731600000',
        'weight': '200',
        'expirationDate': '11302021',
        'birthDate': '07241983',
        'issueDate': '11022017',

        'optionalA': 'N',
        'optionalB': 'N',
        'optionalC': 'Original',
        'optionalD': '',
        'optionalE': '1431',
        'optionalF': '55',
        'optionalG': '46.50',
        'optionalH': '',
        'optionalI': 'N',
        'optionalJ': 'N',
    }
    result_chad = '\x40\x0a\x1e\x0dANSI 636058050002DL00410207ZO02480065DLDAQL084054624\nDCSGALVAN\nDDEN\nDACCHAD\nDDFN\nDADANTHONY\nDDGN\nDCAD\nDCBNONE\nDCDNONE\nDBC1\nDAU511\nDAYBRO\nDAG1621 NE 11TH ST\nDAIMOORE\nDAJOK\nDAK731600000  \nDCFNONE\nDCGUSA\nDAW200\nDBA11302021\nDBB07241983\nDBD11022017\rZOZOAN\nZOBN\nZOCOriginal\nZOD\nZOE1431\nZOF55\nZOG46.50\nZOH\nZOIN\nZOJN\r'
    c = Composer()
    assert c.compose(data_chad) == result_chad


def test_get_composed_riley():
    data_riley = {
        'customerId': 'Y083147822',
        'issuerName': 'Oklahoma',
        'issuerIN': '636058',
        'version': '05',
        'jurVersion': '00',
        'numEntries': '02',

        'familyName': 'DUCKWORTH',
        'familyNameT': 'N',
        'firstName': 'RILEY',
        'firstNameT': 'N',
        'middleName': 'DUNCAN',
        'middleNameT': 'N',
        'vehicleClass': 'D',
        'jurRestriction': '1',
        'jurEndorsement': 'NONE',
        'sex': '1',
        'height': '605',
        'eyeColor': 'BLU',
        'street': '2745 CAMBRIDGE CT',
        'city': 'OKLAHOMA CITY',
        'state': 'OK',
        'country': 'USA',
        'postal': '731160000',
        'weight': '230',
        'expirationDate': '12312021',
        'birthDate': '12291993',
        'issueDate': '06062020',

        'optionalA': 'N',
        'optionalB': 'N',
        'optionalC': 'Replacement',
        'optionalD': '',
        'optionalE': '8833',
        'optionalF': '55',
        'optionalG': '25.00',
        'optionalH': '',
        'optionalI': 'N',
        'optionalJ': 'N',
    }
    result_riley = '\x40\x0a\x1e\x0dANSI 636058050002DL00410217ZO02580068DLDAQY083147822\nDCSDUCKWORTH\nDDEN\nDACRILEY\nDDFN\nDADDUNCAN\nDDGN\nDCAD\nDCB1\nDCDNONE\nDBC1\nDAU605\nDAYBLU\nDAG2745 CAMBRIDGE CT\nDAIOKLAHOMA CITY\nDAJOK\nDAK731160000  \nDCFNONE\nDCGUSA\nDAW230\nDBA12312021\nDBB12291993\nDBD06062020\rZOZOAN\nZOBN\nZOCReplacement\nZOD\nZOE8833\nZOF55\nZOG25.00\nZOH\nZOIN\nZOJN\r'
    c = Composer()

    assert c.compose(data_riley) == result_riley
