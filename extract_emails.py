from pathlib import Path
import re


EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def main():
    print("=== Email Address Extractor ===")
    input_text = input("Enter the path to the input .txt file: ").strip().strip('"')
    input_path = Path(input_text).expanduser()

    if not input_path.is_file():
        print("Error: input file does not exist.")
        return
    if input_path.suffix.lower() != ".txt":
        print("Please select a .txt file.")
        return

    output_text = input("Output file name (press Enter for emails.txt): ").strip()
    output_path = Path(output_text or "emails.txt").expanduser()

    try:
        content = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print("Error: the file is not readable as UTF-8 text.")
        return

    emails = sorted(set(EMAIL_PATTERN.findall(content)), key=str.lower)
    output_path.write_text("\n".join(emails) + ("\n" if emails else ""), encoding="utf-8")

    print(f"Found {len(emails)} unique email address(es).")
    print(f"Results saved to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
