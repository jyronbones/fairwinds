from src.fetch_api_data import fetch_api_data
from src.process_data import convert_to_dataframe


def main():
    api_data = fetch_api_data()

    df = convert_to_dataframe(api_data)

    print(df.head())


if __name__ == "__main__":
    main()