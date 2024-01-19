import re
from variables import results, codon_table

from modules.dna_processor import DNA_Processor


class Protein_Builder:
    def generate_from_rna(self):
        if not results.get("RNA"):
            DNA_Processor().translate_to_RNA()

        # Find all seq starting by (AUG) and ending with (UAA, UAG or UGA)
        # seq must be a multiple of 3
        pattern = r"AUG((?:.{3})*?)(UAA|UAG|UGA)"
        matches = re.findall(pattern, results.get("RNA", ""))

        protiens = []
        for seq, _ in matches:
            # split seq by length of three, get data from codon_table
            acide_amino = []
            for i in range(0, len(seq), 3):
                codon = codon_table.get(seq[i : i + 3], "")
                acide_amino.append(codon)

            protiens.append("M" + "".join(acide_amino))

        results["proteins"] = protiens

    def calculate_codons_frequencey(self):
        if results.get("proteins", []) == []:
            self.generate_from_rna()

        codons_frequencey = {}

        for protein in results.get("proteins", []):
            # save number of occurences of each codon in a protein
            for acido_amino in set(protein):
                codons_frequencey[acido_amino] = protein.count(
                    acido_amino
                ) + codons_frequencey.get(acido_amino, 0)

        results["codons_frequency"] = codons_frequencey
