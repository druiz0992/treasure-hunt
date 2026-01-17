import sys
import hashlib

HASHES = {
    "1": "19d327a733b9ad4091c8ba9e8ada4034",
    "2": "26e69d6b066b0df14399a73869e33805",
    "3": "e438f71039a21a37203ffca666690d72",
    "4": "f74d39fa044aa309eaea14b9f57fe79c",
    "5": "cf47bfada44d83471864a45004948681",
    "6": "b72da152a36eb9f68082c8f20988a36d",
    "7": "73aa20c5960d3dcd44dbfbcbbe9d40d4",
    "8": "19061a3a59c328a0672c5f3a8d8337b1",
}


def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()


def main():
    if len(sys.argv) != 3:
        print("Usage: python check.py <day> <answer>")
        sys.exit(1)

    day, answer = sys.argv[1], sys.argv[2]

    if day not in HASHES:
        print(f"Puzzle {day} desconocido")
        sys.exit(1)

    if md5(answer) == HASHES[day]:
        print(f"🎶 Puzzle {day}: correcto!")
    else:
        print(f"❌ Puzzle {day}: incorrecto.")


if __name__ == "__main__":
    main()
