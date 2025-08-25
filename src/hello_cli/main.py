import argparse

def run():
    parser = argparse.ArgumentParser(description="Hello CLI")
    parser.add_argument("--name", default="world", help="Nome da salutare")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    run()
