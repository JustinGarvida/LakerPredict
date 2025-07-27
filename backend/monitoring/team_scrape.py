import argparse



def parse_args():
    parser = argparse.ArgumentParser(description="NBA Player Points Prediction")
    parser.add_argument("--player", type=str, required=True, help="Name or ID of the player to scrape")
    return parser.parse_args()

def main():
    args = parse_args()

    # Access arguments like:
    print(f"Predicting points for {args.player} vs {args.opponent}")

    # You can now call your prediction logic here
    # prediction = predict(args.player, args.opponent)
    # print(f"Predicted points: {prediction}")

if __name__ == "__main__":
    main()
