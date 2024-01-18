from variables import results, SYMBOLS, COMPLEMENT
import random
import re


class DNA_Processor:
    def validate(self):
        is_validated = set(results.get("DNA", "")).issubset(SYMBOLS)

        results["is_dna_validated"] = is_validated

    def calculate_frequency(self):
        print("Enter necleotide to calculate frequency (A,T,C,G)")
        print("Enter 0 to go back to main menu\n")

        while True:
            try:
                base = input("(3: Calculate frequency)>> ")
                if base == "0":
                    print()
                    break

                assert base.upper() in SYMBOLS

                print(f"frequency of {base} is : {results.get('DNA','').count(base)}\n")

            except (AssertionError, ValueError):
                print("[ERROR]: Enter a valid necleotide base\n")

    def translate_to_RNA(self):
        results["RNA"] = results.get("DNA", "").replace("T", "U")

    def calculate_inverse(self):
        inverse = "".join(
            map(lambda base: COMPLEMENT.get(base, ""), results.get("DNA", ""))
        )

        results["DNA_inverse"] = inverse

    def calculate_GC_content(self):
        dna = results.get("DNA", "")

        gc_content = (dna.count("G") + dna.count("C")) / len(dna) * 100
        results["GC_content"] = f"{gc_content}%"

    def make_mutations(self):
        print("Enter the number of mutation you want to make:")

        dna = results.get("DNA", "")

        while True:
            try:
                choice = input("(9: Random mutations)>> ")
                assert choice.isdecimal

                random_indexes = []
                for _ in range(int(choice)):
                    random_necleotide = random.choice(SYMBOLS)
                    random_index = random.randint(0, len(dna) - 1)

                    while random_index in random_indexes:
                        random_index = random.randint(0, len(dna) - 1)
                    random_indexes.append(random_index)

                    while dna[random_index] == random_necleotide:
                        random_necleotide = random.choice(SYMBOLS)

                    dna = list(dna)
                    dna[random_index] = random_necleotide
                    results["DNA"] = "".join(dna)

                print(f"new mutated DNA:\n{results.get('DNA','')}")
                break

            except (AssertionError, ValueError):
                print("[ERROR]: Enter a valid necleotide base\n")

    def find_motif(self):
        print("Enter motif you want to search for")
        print("Enter 0 to go back to main menu\n")

        while True:
            try:
                motif = input("(10: Find motif)>> ")
                if motif == "0":
                    print()
                    break

                for i in list(motif):
                    assert i.upper() in SYMBOLS

                occ = [
                    m.start()
                    for m in re.finditer(f"(?={motif})", results.get("DNA", ""))
                ]
                print(f"This motif has found at these indexes: {occ}\n")

            except (AssertionError, ValueError):
                print("[ERROR]: Enter a valid necleotide base\n")
