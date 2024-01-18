import random
from variables import SYMBOLS, results


class DNA_GENRATOR:
    def generate(self):
        print(
            """a: generate a random set
b: choose from a predefined sets
0: go back to main menu
        """
        )

        while True:
            choice = input("(1: generate DNA)>> ")

            try:
                assert choice in ("a", "b", "0")

                if choice == "a":
                    results["DNA"] = self.generate_randomly()
                    print(results["DNA"], "\n")
                    break

                if choice == "b":
                    results["DNA"] = self.choose_from_file()
                    print(results["DNA"], "\n")
                    break

                if choice == "0":
                    break

            except (AssertionError, ValueError):
                print("ERROR: Please enter a valid choice")

    def generate_randomly(self):
        while True:
            print("how many sequence do you want?")
            choice = input("(1: generate DNA)>> ")

            try:
                assert choice.isdecimal

                return "".join([random.choice(SYMBOLS) for _ in range(int(choice))])
            except (AssertionError, ValueError):
                print("ERROR: Please enter a valid number\n")

    def choose_from_file(self):
        print(
            """1: sequence 1 consisting of 1000 bases.
2: sequence 2 consisting of 1000 bases.
3: sequence 3 consisting of 500 bases.
4: sequence 4 consisting of 100 bases.
5: sequence 5 consisting of 700 bases.
        """
        )

        sequences = self.read_fasta()

        while True:
            choice = input("(1: generate DNA)>> ")
            try:
                assert choice.isdecimal

                return sequences[int(choice) - 1]

            except (AssertionError, ValueError):
                print("ERROR: Please enter a valid number\n")

    def read_fasta(self):
        sequences = []

        with open("data/sequences.txt", "r") as f:
            seq = ""

            for line in f.readlines():
                if line.startswith(">"):
                    if seq:
                        sequences.append(seq)
                        seq = ""

                    continue

                seq += line.strip("\n")
            if seq:
                sequences.append(seq)

        return sequences

    def save_to_file(self):
        with open("output/results.txt", "w") as f:
            for key, val in results.items():
                f.write(f"{key}: {val}\n")
