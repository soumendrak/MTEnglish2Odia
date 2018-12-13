Machine translation from [English](https://en.wikipedia.org/wiki/English_language) to [Odia](https://en.wikipedia.org/wiki/Odia_language) language

## Analysis so far:
[Machine Translation](https://en.wikipedia.org/wiki/Machine_translation) (MT) has started as early as on 1950s. Based on the progress on this field, the MT can be broadly categorized into following types:
- Rule based MT (RBMT)
- Statistical MT (SMT) and 
- Neural MT (NMT)

The NMT is giving best score (BLEU score) followed by SMT and RBMT. As explained in [this paper](https://arxiv.org/ftp/arxiv/papers/1708/1708.04559.pdf) for Indic languages SMT is performing better (at least 10% higher) than RBMT.
Based on the reading and analysis from some existing papers, as the corpus is low, for the time-being we will go ahead with SMT ([Statistical Machine Translation](https://en.wikipedia.org/wiki/Statistical_machine_translation)) first. As the corpus grows, we will start testing our luck in NMT ([Neural Machine Translation](https://en.wikipedia.org/wiki/Neural_machine_translation))


## High level Roadmap

This roadmap is prepared based on my extra time and availability to work. If I will get more help we can deliver early.

Month | Year | Milestone | Status
:---------|:----------:|:---------|:---------
 [December](#december2018) | 2018 | Analyze and study the existing resources available on Internet | In-progress
 January  | 2019 | Study the reference papers and experts in NMT and analyze their opinions
 February | 2019 | Do same as January, concentrate more on the state-of-the-art practices
 March    | 2019 | Plan the code structure, prepare CI/CD and Unit test cases and start coding
 April    | 2019 | First Alpha version should be released on first week of April ([Utkala Divasa](https://en.wikipedia.org/wiki/Odisha_Day))
 May      | 2019 | Analyze the codebase and do refactoring
 June     | 2019 | Second Alpha version release. Use best practices and concentrate on scalability
 July     | 2019 | First Beta version release
 August   | 2019 | Break
 September| 2019 | Break
 October  | 2019 | Analyze over internet again and do necessary changes
 November | 2019 | Second Beta release. Bug fixes and improvements on Alpha/Beta release feedback
 December | 2019 | Testing and Testing
 January  | 2020 | Production release


### Detailed works completed/ongoing in December 2018 <a name="december2018"></a>
- Found corpuses worth around [27,000 English-Odia tab separated translation pairs](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2879)
 This needs work on the followings:
  - Some preprocessing need to be done.
  - All translation not so accurate based on few manual review
  - Spelling mistakes are there


## Referred articles/websites:
* [Apertium Wiki for Odia language](http://wiki.apertium.org/wiki/Odia)
* [Indic Languages Multilingual Parallel Corpus](http://lotus.kuee.kyoto-u.ac.jp/WAT/indic-multilingual/index.html)
* [The RGNLP Machine Translation Systems for WAT 2018](https://arxiv.org/ftp/arxiv/papers/1812/1812.00798.pdf)
* [Anuvadaksh- An online existing English-Odia translator](https://www.cdac.in/index.aspx?id=mc_mat_anuvadakshInfo)
* [Wordnet for Odia](http://www.cfilt.iitb.ac.in/indowordnet/)
* [RBMT vs SMT](https://arxiv.org/ftp/arxiv/papers/1708/1708.04559.pdf)

## Data collected from:
* [Wikipedia Data dump](https://www.mediawiki.org/wiki/Content_translation/Published_translations)
* [Open Parallel Corpus](http://opus.nlpl.eu)
* [OdiEnCorp 1.0](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2879)

## Contributors
- Soumendra Kumar Sahoo