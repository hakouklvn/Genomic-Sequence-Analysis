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
            print("[ERROR]: Please generate a set of DNA_Processor first")
            continue

        if choice == "2":
            DNA_Processor().validate()
            print(f"DNA_Processor is validated: {results['is_dna_validated']}", "\n")

        if choice == "3":
            DNA_Processor().calculate_frequency()

        if choice == "4":
            DNA_Processor().translate_to_RNA()
            print(f"The RNA sequence is: {results.get('RNA')}\n")

        if choice == "5":
            Protein_Builder().generate_from_rna()
            print(f"Proteins found in this DNA_Processor are:")
            [print(f"{protein}") for protein in results.get("proteins", [])]
            print()

        if choice == "6":
            DNA_Processor().calculate_inverse()
            print(f"DNA inverse is: {results['DNA_inverse']}")

        if choice == "7":
            DNA_Processor().calculate_GC_content()
            print(
                f"the GC content of the DNA_Processor sequence is {results['GC_content']}"
            )

        if choice == "8":
            Protein_Builder().calculate_codons_frequencey()
            print(f"codons frequency:", results["codons_frequency"])

        if choice == "9":
            DNA_Processor().make_mutations()
            print("new mutated DNA:", results.get("DNA", ""))

        if choice == "10":
            DNA_Processor().find_motif()

        if choice == "11":
            DNA_GENRATOR().save_to_file()


if __name__ == "__main__":
    main()
