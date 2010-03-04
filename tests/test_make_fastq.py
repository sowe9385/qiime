#!/usr/bin/env python
#unit tests for make_fastq.py

from cogent.util.unit_test import TestCase, main
from qiime.make_fastq import make_fastq_rec, split_lib_transform, iter_fastq
from qiime.split_libraries import qual_score
__author__ = "Rob Knight"
__copyright__ = "Copyright 2010, The QIIME Project" #consider project name
__credits__ = ["Rob Knight"] #remember to add yourself if you make changes
__license__ = "GPL"
__version__ = "0.92-dev"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Pre-release"

class TopLevelTests(TestCase):
    """Tests of top-level module functions."""
    def test_make_fasta_rec(self):
        """make_fasta_rec should return expected results."""
        header = '>E2_1 FYI2DSB01B17QJ orig_bc=ATCACTAGTCAC new_bc=ATCACTAGTCAC bc_diffs=0'
        seq = 'CTGGTC'
        qual = map(int, '32 32 32 19 19 19'.split())
        self.assertEqual(make_fastq_rec(header, seq, qual),
"""@E2_1 FYI2DSB01B17QJ orig_bc=ATCACTAGTCAC new_bc=ATCACTAGTCAC bc_diffs=0
CTGGTC
+E2_1 FYI2DSB01B17QJ orig_bc=ATCACTAGTCAC new_bc=ATCACTAGTCAC bc_diffs=0
AAA444""")

    def test_split_lib_transform(self):
        """split_lib_transform should return expected results"""
        header = '>E2_1 FYI2DSB01B17QJ orig_bc=ATCACTAGTCAC new_bc=ATCACTAGTCAC bc_diffs=0'
        self.assertEqual(split_lib_transform(header), 
('E2_1 read_id=FYI2DSB01B17QJ barcode=ATCACTAGTCAC', 'FYI2DSB01B17QJ'))

    def test_iter_fastq(self):
        """iter_fastq should iterate over correct # of fasta records"""
        from StringIO import StringIO
        fasta = """>M32Nstr_1 039732_1312_3088 orig_bc=CTCGTGGAGTAG new_bc=CTCGTGGAGTAG bc_diffs=0
CATGCTGCCTCCCGTAGGAGTCTGGGCCGTATCTCAGTCCCAATGTGGCCGGTCACCCTCTCAGGCCGGCTACCCGTCAAAGCCTTGGTAAGCCACTACCCCACCAACAAGCTGATAAGCCGCGAGTCCATCCCCAACCGCCGAAACTTTCCAACCCCCACCCATGCAGCAGGAGCTCCTATCCGGTATTAGCCCCAGTTTCCTGAAGTTATCCCAAAGTCAAGGGCAGGTTACTCACGTGTTACTCACCCGTTCGCCA
>F22Frhd_2 040027_1369_1966 orig_bc=CAAGTGAGAGAG new_bc=CAAGTGAGAGAG bc_diffs=0
CATGCTGCCTCCCGTAGGAGTCTGGGCCGTATCTCAGTCCCAATGTGGCCGGTCACCCTCTCAGGCCGGCTACCCGTCAAAGCCTTGGTAAGCCACTACCCCACCAACAAGCTGATAAGCCGCGAGTCCATCCCCAACCGCCGAAACTTTCCAACCCCCACCCATGCAGCAGGAGCTCCTATCCGGTATTAGCCCCAGTTTCCTGAAGTTATCCCAAAGTCAAGGGCAGGTTACTCACGTGTTACTCACCCGTTCGCCA
>F12Labi_3 040135_0934_1957 orig_bc=AGTTAGTGCGTC new_bc=AGTTAGTGCGTC bc_diffs=0
CATGCTGCCTCCCGTAGGAGTTTGGACCGTGTCTCAGTTCCAATGTGGGGGACCTTCCTCTCAGAACCCCTACTGATCGTTGCCTTGGTGGGCCGTTACCCCGCCAACAAGCTAATCAGACGCATCCCCATCCATAACCGATAAATCTTTATTCGTAATCTCATGAGATCAAACGAATACATAAGGTATTAGTCCAACTTTGCTGGGTTAGTCCCTTACGTTATTGGGCGAGGTTGGATACGCGTTACTCACCCGTGCGCCGGTCGCCG
""".splitlines()
        qual_raw = """>039695_0364_2008 length=49 uaccno=FFLHOYS01A5986
35 35 35 35 35 35 35 35 35 32 30 30 33 33 35 35 35 35 35 34 34 34 36 36 36 36 36 35 35 36 36 36 36 36 40 37 37 37 37 38 39 38 37 38 36 35 35 35 35 
>039732_1312_3088 length=271 uaccno=FFLHOYS01DHI8I
37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 
37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 
37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 38 38 33 33 34 34 36 36 37 37 35 24 19 19 19 38 38 37 37 37 
37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 38 38 38 38 38 37 38 38 38 38 38 38 38 37 37 38 38 38 31 31 33 36 33 33 33 36 36 36 36 24 25 25 28 31 36 36 36 36 36 36 36 38 
38 38 40 40 38 32 31 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 30 30 30 31 32 32 32 
>040027_1369_1966 length=271 uaccno=FFLHOYS01DMIIO
37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 
37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 34 34 34 34 37 37 37 37 37 37 
37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 26 26 24 38 32 22 22 15 15 15 15 15 20 16 16 16 38 38 37 37 37 
37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 37 38 38 34 34 34 37 37 38 28 28 27 36 33 33 33 36 36 36 36 32 32 32 33 36 36 36 38 37 37 36 37 38 
38 38 38 38 38 31 31 32 32 32 32 32 32 32 32 32 32 32 32 31 28 28 28 32 31 31 31 31 32 32 32 
>040135_0934_1957 length=281 uaccno=FFLHOYS01CKBO3
33 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 40 40 40 40 38 38 38 39 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 35 35 35 35 35 35 35 35 35 35 35 35 35 28 28 
28 28 28 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 33 26 26 26 26 33 35 35 35 35 35 
35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 26 26 26 30 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 
35 35 30 30 30 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 35 27 27 25 15 15 15 18 18 25 15 15 15 15 15 15 14 15 15 15 15 15 15 15 14 15 15 15 15 15 15 23 23 28 
28 24 30 31 32 22 22 16 16 16 16 22 22 23 25 21 21 21 21 21 19 21 16 16 16 16 16 22 21 23 25 25 25 21 22 22 22 22 22 22 22 
""".splitlines()
        qual = qual_score(qual_raw)
        result = list(iter_fastq(fasta, qual))
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][1], 'M32Nstr_1')
        self.assertEqual(result[1][1], 'F22Frhd_2')
        self.assertEqual(result[2][1], 'F12Labi_3')

        lines = result[0][0].splitlines()
        self.assertEqual(lines[1][:5], 'CATGC')
        self.assertEqual(lines[3][:5], chr(33+37)*5)
        self.assertEqual(lines[3][-5:], ''.join(map(chr, [33+30,33+31, 33+32, 33+32, 33+32])))
    

#run unit tests if run from command-line
if __name__ == '__main__':
    main()
