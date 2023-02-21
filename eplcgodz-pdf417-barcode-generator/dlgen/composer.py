from collections import namedtuple


class Composer:

    def init(self):
        pass

    def compose(self, data: dict) -> str:
        Data = namedtuple('Data', data)
        d = Data(**data)

        offset = 'pppp'
        length = 'qqqq'
        optionalOffset = 'rrrrr'
        optionalLength = 'ssss'

        prefix = '\x40\x0a\x1e\x0d'
        if d.subfileType == 'DL':
            header = 'ANSI ' + d.issuerIN + d.version + d.jurVersion + d.numEntries + d.subfileType + offset + length + 'ZO' + optionalOffset + optionalLength
            body = (
                d.subfileType + 'DAQ' + d.customerId +
                '\nDCS' + d.familyName +
                '\nDDE' + d.familyNameT +
                '\nDAC' + d.firstName +
                '\nDDF' + d.firstNameT +
                '\nDAD' + d.middleName +
                '\nDDG' + d.middleNameT +
                '\nDCA' + d.vehicleClass +
                '\nDCB' + d.jurRestriction +
                '\nDCD' + d.jurEndorsement +
                '\nDBC' + d.sex +
                '\nDAU' + d.height +
                '\nDAY' + d.eyeColor +
                '\nDAG' + d.street +
                '\nDAI' + d.city +
                '\nDAJ' + d.state +
                '\nDAK' + d.postal + '  '  +
                '\nDCF' + 'NONE' +
                '\nDCG' + d.country +
                '\nDAW' + d.weight +
                '\nDBA' + d.expirationDate +
                '\nDBB' + d.birthDate +
                '\nDBD' + d.issueDate +
                '\x0d'
            ).upper()
        elif d.subfileType == 'ID':
            header = 'ANSI ' + d.issuerIN + d.version + d.jurVersion + d.numEntries + d.subfileType + offset + length + 'ZO' + optionalOffset + optionalLength
            body = (
                d.subfileType + 'DAQ' + d.customerId +
                '\nDCS' + d.familyName +
                '\nDDE' + d.familyNameT +
                '\nDAC' + d.firstName +
                '\nDDF' + d.firstNameT +
                '\nDAD' + d.middleName +
                '\nDDG' + d.middleNameT +
                '\nDBC' + d.sex +
                '\nDAU' + d.height +
                '\nDAY' + d.eyeColor +
                '\nDAG' + d.street +
                '\nDAI' + d.city +
                '\nDAJ' + d.state +
                '\nDAK' + d.postal + '  '  +
                '\nDCF' + 'NONE' +
                '\nDCG' + d.country +
                '\nDAW' + d.weight +
                '\nDBA' + d.expirationDate +
                '\nDBB' + d.birthDate +
                '\nDBD' + d.issueDate +
                '\x0d'
            ).upper()
        else:
            raise Exception()
        optional = (
            'ZOZOA' + d.optionalA +
            '\nZOB' + d.optionalB +
            '\nZOC' + d.optionalC +
            '\nZOD' + d.optionalD +
            '\nZOE' + d.optionalE +
            '\nZOF' + d.optionalF +
            '\nZOG' + d.optionalG +
            '\nZOH' + d.optionalH +
            '\nZOI' + d.optionalI +
            '\nZOJ' + d.optionalJ +
            '\x0d'
        )

        header = header.replace('pppp', '00' + str(len(prefix + header) - 1))
        header = header.replace('qqqq', '0' + str(len(body)))
        header = header.replace('rrrrr', '0' + str(len(prefix + header + body) - 1))
        header = header.replace('ssss', '00' + str(len(optional)))

        return prefix + header + body + optional
