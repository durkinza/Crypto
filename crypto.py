
from crypto import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopping...")
        exit(2)
