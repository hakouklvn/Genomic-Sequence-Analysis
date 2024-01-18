import re
from variables import results, codon_table

from modules.dna_processor import DNA_Processor


class Protein_Builder:
    def generate_from_rna(self):
        if not results.get("RNA"):
            DNA().translate_to_RNA()

        pattern = r"AUG((?:.{3})*?)(UAA|UAG|UGA)"
        matches = re.findall(pattern, results.get("RNA", ""))

        protiens = []
        for seq, _ in matches:
            sequences = [seq[i : i + 3] for i in range(0, len(seq), 3)]
            acide_amino = map(lambda seq: codon_table.get(seq, ""), sequences)

            protiens.append("M" + "".join(acide_amino))

        results["proteins"] = protiens

    def calculate_codons_frequencey(self):
        if not results.get("proteins"):
            self.generate_from_rna()

        codons_frequencey = {}

        for protein in results.get("proteins", []):
            for acido_amino in set(protein):
                if codons_frequencey.get(acido_amino) is None:
                    codons_frequencey.setdefault(
                        acido_amino, protein.count(acido_amino)
                    )
                else:
                    codons_frequencey[acido_amino] = protein.count(
                        acido_amino
                    ) + codons_frequencey.get(acido_amino, 0)

        results["codons_frequency"] = codons_frequencey
        print(codons_frequencey)
