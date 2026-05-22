from fly_in.map_parser import MapParser, MapParsingError
from fly_in.visualizer import Visualizer


def main() -> None:
    with MapParser("maps/challenger/01_the_impossible_dream.txt") as map:
        visualizer = Visualizer(map.hubs, map.connections)
        visualizer.run()


if __name__ == "__main__":
    try:
        main()
    except MapParsingError as e:
        print(f"line {e.line}: {e.error}")
