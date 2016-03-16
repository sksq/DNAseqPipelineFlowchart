#!/usr/bin/env python

# Module to generate flowchart
from graphviz import Digraph


if __name__ == '__main__':

	# Color Constants
	COVAL = '#BDC3C7'
	CBOX = '#7D1424'
	CPARALLELOGRAM = '#6F2480'
	CDIAMOND = '#0F6177'

	# Shape Constants
	OVAL = 'oval'
	BOX = 'box'
	DIAMOND = 'diamond'
	PARALLELOGRAM = 'parallelogram'

	
	# Digraph Object
	dot = Digraph()

	# 1- picard_sam_to_fastq
	dot.node('Start', 'Start', shape=OVAL, color=COVAL, style='filled')
	dot.node('1.condition', 'FASTQ in readset?', shape=DIAMOND, color=CDIAMOND)
	dot.node('1.FASTQ', 'FASTQ', shape=BOX, color=CBOX)
	dot.node('1.generate_fastq', 'Generate FASTQ from SAM/BAM files', shape=BOX, color=CBOX)

	dot.edge('Start', '1.condition')
	dot.edge('1.condition', '1.FASTQ', label='Yes')
	dot.edge('1.condition', '1.generate_fastq', label='No')
	dot.edge('1.generate_fastq', '1.FASTQ')

	# 2- trimmomatic
	dot.node('2.condition', 'FASTA file specified in config file?', shape=DIAMOND, color=CDIAMOND)
	dot.node('2.FASTA', 'FASTA', shape=BOX, color=CBOX)
	dot.node('2.A1_A2', 'Adapter1 and Adapter2 from readset file', shape=BOX, color=CBOX)
	dot.node('2.Trimmomatic', 'Trimmomatic', shape=PARALLELOGRAM, color=CPARALLELOGRAM)

	dot.edge('1.FASTQ', '2.Trimmomatic')
	dot.edge('2.condition', '2.FASTA', label='Yes')
	dot.edge('2.condition', '2.A1_A2', label='No')
	dot.edge('2.A1_A2', '2.FASTA', label='Create an adapter')
	dot.edge('2.FASTA', '2.Trimmomatic', label='Trimming')

	dot.node('2.condition_2', 'PAIRED_END or SINGLE_END adapters?', shape=DIAMOND, color=CDIAMOND)
	dot.node('2.AdaptersReversed', 'Adapters reversed-complemented & swapped', shape=BOX, color=CBOX)
	dot.node('2.Adapter1', 'Use Adapter1', shape=BOX, color=CBOX)

	dot.edge('2.condition_2', '2.AdaptersReversed', label='PAIRED_END')
	dot.edge('2.condition_2', '2.Adapter1', label='SINGLE_END')
	dot.edge('2.AdaptersReversed', '2.Trimmomatic')
	dot.edge('2.Adapter1', '2.Trimmomatic')

	# 3- merge_trimmomatic_stats
	dot.node('3.TrimmedFASTQ', 'Trimmed FASTQ', shape=BOX, color=CBOX)
	dot.edge('2.Trimmomatic', '3.TrimmedFASTQ', label='')

	# 4- bwa_mem_picard_sort_sam
	dot.node('4.Genome', 'Aligned to reference genome', shape=PARALLELOGRAM, color=CPARALLELOGRAM)
	dot.node('4.BAM', 'BAM files', shape=BOX, color=CBOX)
	dot.node('4.Sorted', 'Sorted by coordinate', shape=PARALLELOGRAM, color=CPARALLELOGRAM)
	dot.node('4.SortedBAM', 'Aligned and sorted BAM files', shape=BOX, color=CBOX)

	dot.edge('3.TrimmedFASTQ', '4.Genome', label='')
	dot.edge('4.Genome', '4.BAM', label='Software: BWA, Algorithm: bwa mem')
	dot.edge('4.BAM', '4.Sorted', label='')
	dot.edge('4.Sorted', '4.SortedBAM', label='Using Picard')

	# 5- picard_merge_sam_files
	dot.node('5.Merged', 'Merged into one file per sample', shape=PARALLELOGRAM, color=CPARALLELOGRAM)
	dot.node('5.MergedBAM', 'Merged BAM files', shape=BOX, color=CBOX)
	dot.node('End', 'End', shape=OVAL, color=COVAL, style='filled')

	dot.edge('4.SortedBAM', '5.Merged')
	dot.edge('5.Merged', '5.MergedBAM', label='Using Picard')
	dot.edge('5.MergedBAM', 'End')

	# Output file output/DNAseqPipeline.pdf
	dot.render('output/DNAseqPipeline', view=True)

