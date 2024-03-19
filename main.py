from pathlib import Path
from app import io

DATA_DIR = Path(__file__).parent / "data"


def main():
    input_dir = DATA_DIR / "in"
    output_dir = DATA_DIR / "out"
    console_input = io.input.input_from_console("Write data to save to file: ")
    io.output.write_to_file(output_dir / "console_output.txt", console_input)
    file_input = io.input.read_from_file(input_dir / "file_input.txt")
    io.output.write_to_file(output_dir / "file_output.txt", file_input)
    csv_input = io.input.read_csv(input_dir / "csv_input.csv")
    io.output.write_csv(output_dir / "csv_output.csv", csv_input, index=False)


if __name__ == "__main__":
    main()
