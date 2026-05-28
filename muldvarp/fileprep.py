#!/usr/bin/env python3
import sys
import os


def xor_with_key(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def main():
    if len(sys.argv) != 3:
        print("Usage: python xor_encrypt.py <hex_key> <filename>")
        sys.exit(1)

    hex_key, filename = sys.argv[1], sys.argv[2]
    os.system("sudo chown ubuntu " + filename)

    try:
        key = bytes.fromhex(hex_key)
    except ValueError:
        print(f"Error: '{hex_key}' is not valid hex.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print(f"Error: file '{filename}' not found.")
        sys.exit(1)

    with open(filename, "rb") as f:
        data = f.read()

    encrypted = xor_with_key(data, key)

    os.makedirs("pub", exist_ok=True)
    out_path = os.path.join("pub", os.path.basename(filename))

    with open(out_path, "wb") as f:
        f.write(encrypted)

    print(f"Saved XORed file to: {out_path}")


if __name__ == "__main__":
    main()
