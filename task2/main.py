from src.fetch_api_data import fetch_api_data
from src.process_data import convert_to_dataframe, get_first_five_rows


def main():
    api_data = fetch_api_data()

    df = convert_to_dataframe(api_data)

    print(get_first_five_rows(df))


if __name__ == "__main__":
    main()