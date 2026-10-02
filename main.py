from compressor import lz77_compress


if __name__ == "__main__":
    text = "ABAABABAABBBBBBBBBBBBA"
    res = lz77_compress(text, window=10, lookahead=10)
    print("Tokens:", res)