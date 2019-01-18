OdiEnCorp 1.0 Release Description
---------------------------------
http://hdl.handle.net/11234/1-2879
Shantipriya Parida, Ondrej Bojar
Charles University, Faculty of Mathematics and Physics,
Institute of Formal and Applied Linguistics (UFAL)
2018

Data
----
We have collected English-Odia parallel and monolingual data from the
available public websites for NLP research in Odia.

The parallel corpus consists of English-Odia parallel Bible, Odia
digital library, and Odisha Goverment websites. It covers bible,
literature, goverment of Odisha and its policies. We have processed the
raw data collected from the websites, performed alignments (a mix of
manual and automatic alignments) and release the corpus in a form ready
for various NLP tasks.

The Odia monolingual data consists of Odia-Wikipedia and Odia e-magazine
websites. Because the major portion of data is extracted from
Odia-Wikipedia, it covers all kinds of domains. The e-magazines data
mostly cover the literature domain. We have preprocessed the monolingual
data including de-duplication, text normalization, and sentence
segmentation to make it ready for various NLP tasks.

Corpus Formats
--------------
Both corpora are in simple tab-delimited plain text files.

The parallel corpus files have three columns:
- the original book/source of the sentence pair
- the English sentence
- the corresponding Odia sentence

The monolingual corpus has a varying number of columns:
- each line corresponds to one *paragraph* (or related unit) of the
  original source
- each tab-delimited unit corresponds to one *sentence* in the paragraph


Data Statistics
----------------
The statistics of the current release is given below.

Parallel Corpus Statistics
---------------------------

Dataset	Sentences	#English tokens 	#Odia tokens
-------	---------	----------------	-------------
Train  	    27136	          706567	       604147
Dev    	      948	           21912	        19513
Test   	     1262	           28488	        24365
-------	---------	----------------	-------------
Total  	    29346	          756967	       648025

Domain Level Statistics
------------------------

Domain            	Sentences	#English tokens 	#Odia tokens
------------------	---------	----------------	-------------
Bible             	    29069	          756861	       640157
Literature        	      424	            7977	         6611
Goverment policies	      204	            1411	         1257
------------------	---------	----------------	-------------
Total             	    29697	          766249	       648025

Monolingual Corpus Statistics
-----------------------------

Paragraphs	Sentences	#Odia tokens
----------	---------	------------
     71698	   221546	     2641308

Domain Level Statistics
-----------------------

Domain        	Paragraphs    	Sentences	#Odia tokens
--------------	--------------	---------	-------------
General (wiki)	30468 (42.49%)	   102085	      1320367
Literature    	41230 (57.50%)	   119461	      1320941
--------------	--------------	---------	-------------
Total         	         71698	   221546	      2641308


Citation
--------

If you use this corpus, please cite the following paper:

Title: OdiEnCorp: Odia-English and Odia-Only Corpus for Machine Translation
Author: Shantipriya Parida, Ondrej Bojar, and Satya Ranjan Dash
Proceedings of the Third International Conference on Smart Computing & Informatics (SCI) 2018
Series: Smart Innovation, Systems and Technologies (SIST)
Publisher: Springer Singapore

