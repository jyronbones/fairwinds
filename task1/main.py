from src.fetch_csv import fetch_csv_data, convert_to_dataframe
from src.process_data import get_first_five_rows


def main():
    csv_data = fetch_csv_data()

    df = convert_to_dataframe(csv_data)

    first_five_rows = get_first_five_rows(df)
    print(first_five_rows)


if __name__ == "__main__":
    main()