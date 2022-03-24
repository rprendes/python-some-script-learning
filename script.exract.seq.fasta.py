import sys
from pyfasta import Fasta
#from Bio import SeqIO
#for record in SeqIO.parse("test1.fasta", "fasta"):
#    fa=record
#
#import pandas as pd
#bf=pd.read_table('bedfile')

est_fasta_file = sys.argv[1]

# i'll assume it's tab-delimited...
# and est is the query.
est_mirna_blast = sys.argv[2]

# take 100bp up/down-stream.
xstream = 100

est_fasta = Fasta(est_fasta_file)

for line in open(est_mirna_blast):
    # convert to int and 0-based coords.
    qstart, qstop, sstart, sstop = [int(x) - 1 for x in line.split("\t")[6:10]]
    query, subject = line.split("\t")[:2]
    up = min(0, qstart - xstream)
    down = qstop + xstream + 1

    est_upstream = est_fasta[query][up:qstart]
    est_dowstream = est_fasta[query][qstop:down]

    print ">%s_up" % query
    print est_upstream
    print ">%s_down" % query
    print est_dowstream
