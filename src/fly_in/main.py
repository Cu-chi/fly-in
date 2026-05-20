from fly_in.map_parser import MapParser, MapParsingError


def main() -> None:
    with MapParser("maps/test.txt") as _:
        pass


if __name__ == "__main__":
    try:
        main()
    except MapParsingError as e:
        print(f"line {e.line}: {e.error}")
