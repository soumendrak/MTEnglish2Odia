[Home page](https://soumendrak.github.io/MTEnglish2Odia/) | [MT_Flow_Pipleine](https://soumendrak.github.io/MTEnglish2Odia/MT_Flow_Pipleine) |
[Wishlist](https://soumendrak.github.io/MTEnglish2Odia/possible_projects)

Machine translation from [English](https://en.wikipedia.org/wiki/English_language) to [Odia](https://en.wikipedia.org/wiki/Odia_language) language

## Analysis so far:
[Machine Translation](https://en.wikipedia.org/wiki/Machine_translation) (MT) has started as early as on 1950s. Based on the progress on this field, the MT can be broadly categorized into following types:
- Rule based MT (RBMT)
- Statistical MT (SMT) and 
- Neural MT (NMT)
- Hybrid MT (HMT)

The NMT is giving best score (BLEU score) followed by SMT and RBMT. As explained in [this paper](https://arxiv.org/ftp/arxiv/papers/1708/1708.04559.pdf) for Indic languages SMT is performing better (at least 10% higher) than RBMT.
Based on the reading and analysis from some existing papers, as the corpus is low, for the time-being we will go ahead with SMT ([Statistical Machine Translation](https://en.wikipedia.org/wiki/Statistical_machine_translation)) first. As the corpus grows, we will start testing our luck in NMT ([Neural Machine Translation](https://en.wikipedia.org/wiki/Neural_machine_translation))


## High level Roadmap

This road map is prepared based on my extra time and availability to work. If I will get more help we can deliver early.

Month | Year | Milestone | Status
:---------|:----------:|:---------|:---------
 [December](#december2018) | 2018 | Analyze and study the existing resources available on Internet | Completed
 [January](#january2019)  | 2019 | Study the reference papers and experts in NMT and analyze their opinions | Completed
 [February](#february2019) | 2019 | Do same as January, concentrate more on the state-of-the-art practices | Completed
 Mar-Dec    | 2019 | Parallel corpora generation | 
 [September](#september2019) | 2019 | Data ingestion pipeline | Initial draft prepared |
 [October](#october2019) | 2019 | Read existing papers on MT and write the summary | Delegated
 [Nov-Dec](#novdec2019) | 2019 | Parallel corpora generation and data cleaning | In-progress


*The parallel corpora generation data has been moved to [Odia Wikimedia](https://github.com/OdiaWikimedia/English-Odia). There will be **no further work** unless we have achieved at least 10k (12k/10k achieved) parallel corpus.*

### <a name="december2018"></a> Detailed works completed in December 2018
- Found corpus worth around [27,000 English-Odia tab separated translation pairs](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2879)
 This needs work on the followings:
  - Some preprocessing need to be done.
  - All translation not so accurate based on few manual review
  - Spelling mistakes are there
- After reading [one article](http://www.scielo.org.mx/scielo.php?pid=S1405-55462017000400725&script=sci_arttext) on preprocessing English-Hindi corpus for SMT, I got insight on the following preprocessing tasks need to be done at first:
  - Punctuation should NOT be removed
  - **English** text should be lower cased as Odia does not have any upper case or lower case
  - Spell normalization (Which is like [Lemmatization](https://en.wikipedia.org/wiki/Lemmatization)) will have a greater impact
  - The impact of mapping numbers with unique class labels is not very effective and can be left out.
  - We need [NER](https://en.wikipedia.org/wiki/Named-entity_recognition) (Named Entity Recognition) words for which [Transliteration](https://en.wikipedia.org/wiki/Transliteration) is enough
  - We need POS tag data to improve the accuracy also.
- [Moses](http://www.statmt.org/moses/?n=Moses.Overview) MT tool is open source and ideal for developing SMT for our purpose. 
  - It needs parallel corpus to train and build the model after that prediction it can do.
  - Data curation as explained on above point will be crucial to train this kind of system.
  - If no better option available, we will mostly go with this approach.
- Other than this I got a good sense to keep an eye on [Hybrid Machine Translation](https://en.wikipedia.org/wiki/Hybrid_machine_translation), which will be mixture of RBMT and SMT.
- There is not enough corpus available to go for NMT/SMT currently. We need to prepare a platform like [Google translate community](https://translate.google.com/community?source=mfooter#en/or) where we can manually create English-Odia phrase or word pairs. For this the following needed:
  - UI hosted somewhere on cloud which can handle at least 100 requests per minute
  - A DB, also hosted in cloud to store the data provided by users
  - Possible suggestions for new users to start translating
  - Review mechanism on the translated terms, even with good intention grammatical or syntactical errors need to be validated
  - This infrastructure need to be hosted somewhere on cloud and it should be absolutely free to use.
- **Unknown words handling** : There will be definitely terms will come for which Odia words will not be present. These are some suggestions to handle unknown words:
  - Transliterate those words to Odia
  - Using some other existing translation system, convert those words to Hindi/Sanskrit then transliterate those words to Odia. Because most of the words in between Hindi/Sanskrit and Odia are same and people can understand.

### <a name="january2019"></a> Detailed works completed in January 2019
- Last year has been pretty exciting to prepare this plan. Hope this year we will be able to deliver something useful for the community.
- Quality of data is highly needed. Therefore started preparing phrase parallel corpus and contributing simultaneously to both Google and Facebook. How ? Google translation community and Facebook Translate are recommending phrases to translate. The same phrases I am keeping a copy to myself.
- Microsoft has given [an exciting resource](https://hub.microsofttranslator.com) to public to train their own Parallel Translation model that is also **FREE**. Details: 
  - It needs more than 10,000 pairs of parallel sentence pairs
  - It seems to be working on SMT
  - Train, Testing, Deployment all pipeline have been there
- First attempt I have tried this tool with GNOME translation pair I got. However, It got failed may be due to only 60 parallel sentences.
- In the meantime there seems to be many work going on with frequent papers in [Unsupervised NMT](http://arxiv.org/abs/1901.04112v1) for low resources languages, there has not been any significant usable work yet. However, I am keeping an eye on that too.
- The Translator Hub has been retired on May 2019. It has been migrated to [Microsoft Custom translator](https://www.microsoft.com/en-us/translator/business/hub/). However, Odia language is unavailable currently. I have requested them to add it.

### <a name="february2019"></a> Detailed works completed/ongoing in February 2019
- Data review and preparation started. 
- Around 550 pairs reviewed till now. We need at least 10,000 pairs by end of this month. Finding ways to automate.

### <a name="september2019"></a> Data Ingestion pipeline
- A [pipeline flow](https://soumendrak.github.io/MTEnglish2Odia/MT_Flow_Pipleine) draft for data ingestion been created.  

### <a name="october2019"></a> Reading papers
#### Six Challenges for Neural Machine Translation
- There are [six challenges in NMT](https://arxiv.org/pdf/1706.03872.pdf)
  1. Domain mismatch
  2. Amount of Training Data
  3. Rare Words
  4. Long sentences
  5. Word Alignment
  6. Beam Search
### <a name="novdec2019"></a> New pairs addition
Bible pairs from OdiEnCorp1.0 has been added to the consolidated corpus.

## Impediments
- [x] Get at least 10,000 parallel open corpus for Odia language to begin with.
- [ ] Verification of the existing corpus badly needed.
- [ ] Moses does not run on Windows. Need an Ubuntu OS to test that.
- [ ] Need a cloud system to host manual translation API server and in future for online translation. Is it Microsoft ?

## Referred articles/websites:
* [Apertium Wiki for Odia language](http://wiki.apertium.org/wiki/Odia)
* [Indic Languages Multilingual Parallel Corpus](http://lotus.kuee.kyoto-u.ac.jp/WAT/indic-multilingual/index.html)
* [The RGNLP Machine Translation Systems for WAT 2018](https://arxiv.org/ftp/arxiv/papers/1812/1812.00798.pdf)
* [Anuvadaksh- An online existing English-Odia translator](https://www.cdac.in/index.aspx?id=mc_mat_anuvadakshInfo)
* [Wordnet for Odia](http://www.cfilt.iitb.ac.in/indowordnet/)
* [RBMT vs SMT](https://arxiv.org/ftp/arxiv/papers/1708/1708.04559.pdf)
* [Detail MT system analysis of Indic languages](http://airccse.org/journal/ijnlc/papers/4215ijnlc05.pdf)
* [English-Punjabi parallel corpus creation](http://ijesm.co.in/uploads/68/4983_pdf.pdf)
* [Creating more corpus by breaking long sentences](https://arxiv.org/pdf/1905.08945v1)

## Useful Open source libraries
* [fast_align](https://github.com/clab/fast_align) : Align the words between two parallel corpus 

## Data collected from:
* [Wikipedia Data dump](https://www.mediawiki.org/wiki/Content_translation/Published_translations)
* [Open Parallel Corpus](http://opus.nlpl.eu)
* [OdiEnCorp 1.0](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2879)
* [TDIL](http://tdil-dc.in/index.php?option=com_download&task=showresourceDetails&toolid=1070&lang=en) - Technical strings 52,000 pairs-Data needs to be cleaned
* [Global Voices](http://casmacat.eu/corpus/global-voices.html) - 328 sentences pairs
* [Mann ki baat](https://www.narendramodi.in/mann-ki-baat) - 1000+ pairs
* [Twitter:DoctorBabu](https://twitter.com/drgynaec) - Around 100 Botanical terms En-Or pairs
* [Rupesh Ranjan Panda](https://github.com/rupeshranjanpanda/odia) - Around 300 generic En-Or pairs


## Prospective data corpus
These are few places where relevant data may be present, however getting the data is not straight forward.
* [EMILLE Project](http://catalog.elra.info/en-us/repository/browse/ELRA-W0037/) :
  The Oriya written corpus consists of data incorporated from the CIIL Corpus, originally gathered by the Institute of Applied Language Sciences, Bhubaneshwar (approximately 2,730,000 words).
* [Gyan Nidhi-TDIL](https://tdil-dc.in/index.php?option=com_download&task=showresourceDetails&toolid=281&lang=en) : Million pages’ multilingual parallel text corpus in English and 11  Indian  languages  (Assamese,  Bengali,  Gujarati,  Hindi, Kannada,   Marathi,   Malayalam,   Oriya,   Punjabi,   Tamil   & Telugu)  based  on  Unicode  encoding.  The  Gyan  Nidhi  corpus contains  the  text  in  the  form  of  books. In  these  books  there were  number of diagrams,  figures,  charts  and  other  special symbols. These are removed from the text by using automated and  manual  tools.  The  text  in  gyan  nidhi  is  in  the  form of paragraphs, that are converted into short sentences.
* [A Gold Standard Odia Raw Text Corpus](https://data.ldcil.org/text/text-raw-corpus/a-gold-standard-odia-raw-text-corpus) : Around 15, 88, 287 words are there in this corpus available to purchase. 

## Key Contributors
- [Anjan Kumar Panda](https://twitter.com/ak_panda)
- [Dr. Arun Malik](https://www.linkedin.com/in/arun-malik-6a80a77/)
- [Soumendra Kumar Sahoo](https://www.linkedin.com/in/soumendrakumarsahoo/) 
- [Subhadarshi Panda](https://github.com/subhadarship)
- [Subhashish Panigrahi](https://twitter.com/subhapa)

*"In my dream of the 21st century for the State, I would have young men and women who put the interest of the State before them. They will have pride in themselves, confidence in themselves. They will not be at anybody’s mercy, except their own selves. By their brains, intelligence and capacity, they will recapture the history of Kalinga." - [Biju Pattnaik](https://en.wikipedia.org/wiki/Biju_Patnaik)*


<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This Website's documentation work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
