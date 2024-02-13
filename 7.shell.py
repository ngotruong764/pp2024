import subprocess


def main():
    while True:
        command = str(input("Enter your command( 0:Exit): "))

        # Exit program
        if command == "0":
            print("Exit program!")
            break

        # Execute command
        out = subprocess.run(command, shell=True, text=True, capture_output=True)
        if out.returncode == 0:  # returncode == 0: success
            print(out.stdout)
        else:
            print(out.stderr)


if __name__ == "__main__":
    main()
