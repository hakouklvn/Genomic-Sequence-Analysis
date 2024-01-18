from modules.dna_generator import DNA_GENRATOR
from modules.dna_processor import DNA_Processor
from modules.protein_builder import Protein_Builder

from variables import results


def main():
    print(
        """
 1: Generate a DNA
 2: Validate the DNA
 3: Calculate the necleotides base frequency
 4: Translate DNA to RNA
 5: Translate RNA into a protein
 6: Calculate the inverse complement of a DNA
 7: Calculate the taux of GC in a DNA
 8: Calculate the frequency of a codons in a DNA
 9: Make a random mutations to DNA
10: Find a motif in a DNA
11: Save results in a file
"""
    )

    while True:
        choice = input("> ")

        if choice == "quit()":
            break

        if choice == "1":
            DNA_GENRATOR().generate()

        if not results.get("DNA"):
            print("[ERROR]: Please generate a set of DNA first")
            continue

        if choice == "2":
            DNA().validate()
            print(f"DNA is validated: {results['is_dna_validated']}", "\n")

        if choice == "3":
            DNA().calculate_frequency()

        if choice == "4":
            DNA().translate_to_RNA()
            print(f"The RNA sequence is: {results.get('RNA')}\n")

        if choice == "5":
            PROTEIN().generate_from_rna()
            print(f"Proteins found in this DNA are:")
            [print(f"{protein}") for protein in results.get("proteins", [])]
            print()

        if choice == "6":
            DNA().calculate_inverse()
            print(f"DNA inverse is: {results['DNA_inverse']}")

        if choice == "7":
            DNA().calculate_GC_content()
            print(f"the GC content of the DNA sequence is {results['GC_content']}%")

        if choice == "8":
            PROTEIN().calculate_codons_frequencey()

        if choice == "9":
            DNA().make_mutations()

        if choice == "10":
            DNA().find_motif()

        if choice == "11":
            DNA_GENRATOR().save_to_file()


if __name__ == "__main__":
    main()
