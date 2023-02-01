from pdf417.encoding import (
    DEFAULT_ENCODING,
    compute_error_correction_code_words,
    encode_rows,
    get_padding,
    validate_barcode_size,
)

from pdf417.util import chunks


def encode(data_words, columns=13, security_level=5,
           encoding=DEFAULT_ENCODING, numeric_compaction=True):
    if columns < 1 or columns > 30:
        raise ValueError(
            "'columns' must be between 1 and 30. Given: %r" % columns
        )

    if security_level < 0 or security_level > 8:
        raise ValueError(
            (
                "'security_level' must be "
                "between 1 and 8. Given: %r"
            ) % security_level
        )

    # Convert data to code words and split into rows
    code_words = data_words_to_code_words(data_words, columns, security_level, numeric_compaction=True)

    rows = list(chunks(code_words, columns))

    return list(encode_rows(rows, columns, security_level))


def data_words_to_code_words(data_words, columns, security_level, numeric_compaction=True):
    """Converts the data words to high level code words.

    Including the length indicator and the error correction words, but without
    padding.
    """

    data_count = len(data_words)

    # Get the padding to align data to column count
    ec_count = 2 ** (security_level + 1)
    padding_words = get_padding(data_count, ec_count, columns)
    padding_count = len(padding_words)

    # Check the generated bar code's size is within specification parameters
    validate_barcode_size(data_count, ec_count, padding_count, columns)

    # Length includes the data CWs, padding CWs and the specifier itself
    length = data_count + padding_count + 1

    # Join encoded data with the length specifier and padding
    extendend_words = [length] + data_words + padding_words

    # Calculate error correction words
    ec_words = compute_error_correction_code_words(extendend_words, security_level)

    return extendend_words + ec_words
