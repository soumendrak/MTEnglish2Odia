[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b3a25275798c4c129dc863b7e619f41c)](https://www.codacy.com/app/soumendrak/MTEnglish2Odia?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=soumendrak/MTEnglish2Odia&amp;utm_campaign=Badge_Grade)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsoumendrak%2FMTEnglish2Odia.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsoumendrak%2FMTEnglish2Odia?ref=badge_shield)

# Project moved
This project has been moved under OdiaNLP GitHub organization. For more details please visit: https://odianlp.github.io/

## MTEnglish2Odia

Approx. Number of En-Or parallel reviewed pairs: **42,000**

## Machine Translation from English to Odia language
This is a healthy start to building Automated machine translation for `English` to `Odia` language.
This has been built mainly to help increase quality odia wikipedia articles by translating for English Wikipedia.
The approach is to start building a parallel corpus between English and Odia language which can later be used in SMT(Statistical Machine Translation) or NMT (Neural Machine Translation) in future by interested people.

**Around 9000 English-Odia un-reviewed raw parallel pairs dump available in [this file](/data/output/piped_pairs_raw_may_2019.csv) as pipe separated phrases or sentences.**

For more details visit the website of this repository : [MTEnglish2Odia](https://soumendrak.github.io/MTEnglish2Odia/)

# How can I contribute to this repository?
- [Click here](https://www.dataschool.io/how-to-contribute-on-github/) to read a general guide on how to contribute to a Github open source project for beginners.
### What can I contribute?
- You can send English-Odia word/phrase/sentence pairs on the below format in a new file, under your name and types of data.
- Please put the file under [Individual_files](https://github.com/soumendrak/MTEnglish2Odia/tree/master/data/input/Individual_files)  
- For e.g. if your name is Satyabrata, you want to upload generic phrases:    


| Key        | Example       |
| ------------- |:-------------|
| Filename      | `satyabrata.txt` |
| File upload path      | `data/Individual_files/satyabrata.txt`      |
| File text format | `Why are you so lazy?||ଆପଣ ଏତେ ଅଳସୁଆ କାହିଁକି `      |

> Please make sure you have correct permissions to upload this data in GPL license.
- Tutorial on how to fork a repository and send a PR can be found in [this video](https://www.youtube.com/watch?v=_NrSWLQsDL4) or [this video](https://www.youtube.com/watch?v=rgbCcBNZcdQ) or this Github doc tutorial for [fork](https://help.github.com/en/articles/fork-a-repo) and this one for [pull request](https://help.github.com/en/articles/creating-a-pull-request)
- Your Pull Request will be reviewed first.
- Please follow up if any comments or modifications are needed on your Pull Request.
- In case of any confusion please contact on proud_odia@outlook.com. You will get a response within a day or two.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=_NrSWLQsDL4
" target="_blank"><img src="http://img.youtube.com/vi/_NrSWLQsDL4/0.jpg" 
alt="Fork and Pull Request-1" width="240" height="180" border="10" /></a>

<a href="http://www.youtube.com/watch?feature=player_embedded&v=rgbCcBNZcdQ
" target="_blank"><img src="http://img.youtube.com/vi/rgbCcBNZcdQ/0.jpg" 
alt="Fork and Pull Request-2" width="240" height="180" border="10" /></a>

## License
GPL v3.0

---
ଇଂରାଜୀରୁ ଓଡ଼ିଆ ଭାଷାକୁ ମେସିନ ଟ୍ରାନ୍ସଲେସନଦ୍ୱାରା ଅନୁବାଦ କରିବାକୁ ଏହି ପ୍ରକଳ୍ପଟି ତିଆରି ହୋଇଛି । ଏହା ମୁଖ୍ୟତଃ ଓଡ଼ିଆ ଉଇକିପିଡ଼ିଆରେ ଗୁଣାତ୍ମକ ପୃଷ୍ଠାଗୁଡ଼ିକର ସଂଖ୍ୟା ବୃଦ୍ଧି କରିବାକୁ ଗଠନ କରାଯାଇଛି । ବର୍ତ୍ତମାନର ଯୋଜନା ହିସାବରେ ପ୍ରଥମେ ଇଂରାଜୀ-ଓଡ଼ିଆ ଅନୁବାଦର ପାରାଲେଲ ତଥ୍ୟ ସଂଗ୍ରହ ହେବ । ଯଥେଷ୍ଟ ପରିମାଣର ତଥ୍ୟ ସଂଗ୍ରହ ପରେ ଏହାକୁ ପ୍ରଥମେ ଷ୍ଟାଟିଷ୍ଟିକାଲ ମେସିନ ଟ୍ରାନ୍ସଲେସନ ଏବଂ ପରେ ନ୍ୟୂରାଲ ମେସିନ ଟ୍ରାନ୍ସଲେସନ ଦ୍ୱାରା ଉପଯୋଗ କରାଯାଇ ଅନୁବାଦର ଶୁଦ୍ଧତ୍ତା ହିସାବ କରାଯିବ । ଚଳନୀୟ ଶୁଦ୍ଧତା ହାସଲ ପରେ ଏହାକୁ ସର୍ବସାଧାରଣଙ୍କ ନିମନ୍ତେ ଉତ୍ସର୍ଗୀକୃତ କରାଯିବ ।

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsoumendrak%2FMTEnglish2Odia.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsoumendrak%2FMTEnglish2Odia?ref=badge_large)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/subhadarship"><img src="https://avatars2.githubusercontent.com/u/35211168?v=4" width="100px;" alt=""/><br /><sub><b>subhadarship</b></sub></a><br /><a href="https://github.com/soumendrak/MTEnglish2Odia/commits?author=subhadarship" title="Code">💻</a> <a href="#design-subhadarship" title="Design">🎨</a> <a href="#ideas-subhadarship" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/kamakshyaP"><img src="https://avatars0.githubusercontent.com/u/21032122?v=4" width="100px;" alt=""/><br /><sub><b>kamakshyaP</b></sub></a><br /><a href="#content-kamakshyaP" title="Content">🖋</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/soumendrakumarsahoo/"><img src="https://avatars3.githubusercontent.com/u/10120538?v=4" width="100px;" alt=""/><br /><sub><b>Soumendra kumar sahoo</b></sub></a><br /><a href="#ideas-soumendrak" title="Ideas, Planning, & Feedback">🤔</a> <a href="#design-soumendrak" title="Design">🎨</a> <a href="https://github.com/soumendrak/MTEnglish2Odia/commits?author=soumendrak" title="Documentation">📖</a> <a href="https://github.com/soumendrak/MTEnglish2Odia/commits?author=soumendrak" title="Code">💻</a> <a href="#content-soumendrak" title="Content">🖋</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!