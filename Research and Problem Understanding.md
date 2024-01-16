# Phase 2: Research and Problem Understanding:

## Papers

### 1. Automated Hate Speech Detection and the Problem of Offensive Language

A key challenge for automatic hate-speech detection on social media is the separation of hate speech from other instances of offensive language. Lexical detection methods tend to have low precision because they classify all messages containing particular terms as hate speech and previous work using supervised learning has failed to distinguish between the two categories. This paper uses a crowd-sourced hate speech lexicon
to collect tweets containing hate speech keywords. Then, it uses crowd-sourcing to label a sample of these tweets into three categories: those containing hate speech, only offensive language, and those with neither. This paper trains a multi-class classifier to distinguish between these different categories. Close analysis of the predictions and the errors shows when hate speech can be reliably seperated from other offensive language
and it can also be determined when this differentiation is more difficult. This paper finds that racist and homophobic tweets are more likely to be classified as hate speech but that sexist tweets are generally classified
as offensive. Tweets without explicit hate keywords are also more difficult to classify

This paper has performed an extensitve study of hate speech detection and the problem of offensive language as two seperate problems. The conclusions and datasets of this paper can be used extensively when we analyze offensive comments hurled towards the protestors by police officers.

### 2. Transfer Learning for Sentiment Analysis Using BERT Based Supervised Fine-Tuning

The growth of the Internet has expanded the amount of data expressed by users across multiple platforms. The availability of these different worldviews and individuals’ emotions empowers sentiment analysis. However, sentiment analysis becomes even more challenging due to a scarcity of standardized labeled data in regional languages. The majority of regional language research has relied on models of deep learning that significantly focus on context-independent word embeddings, such as Word2Vec, GloVe, and fastText, in which each word has a fixed representation irrespective of its context. Meanwhile, Context-Based pre-trained language models such as BERT have recently revolutionized the state of natural language processing. This work utilizes BERT’s transfer learning ability to a deep integrated model CNN-BiLSTM for enhanced performance of decision-making in Sentiment Analysis on regional languages. In addition, this work also introduces the ability of Transfer Learning to classical Machine Learning algorithms for the performance comparison of CNN-BiLSTM. Additionally, it also explore various word embedding techniques, such as Word2Vec, GloVe, and fastText, and compare their performance to the BERT Transfer Learning strategy. As a result, this research shows a state-of-the-art binary classification performance for Sentiment Analysis in Bangla that significantly outperforms all embedding and algorithms.

Though this paper explores fine-tuning of BERT for sentiment analysis in regional languages (specficially Bangla), the paper mentions the lack of labelled data in this domain which hinders the fine-tuning of models like BERT. We can extract a few instances where the police talk about the lack of a plan or fail to offer directions to the protestors and then, we can leverage the methods used in this paper to fine-tune BERT to detect more such incidents in the rest of the text.

### 3. Robust Speech Recognition via Large-Scale Weak Supervision

This paper, written by OpenAI researchers, introduces OpenAI Whisper, an Open-Source Machine Learning model to transcribe text from aidio. This paper trains speech recognition models on 680,000 hours of weakly supervised web data rather than curated datasets. The model is evaluated in a zero-shot transfer setting without any fine-tuning on test sets. The models in this work are traind to multitask, doing speech recognition in 125 languages, speech translation, and voice activity detection jointly. Without fine-tuning, the models match or exceed state-of-the-art results on many test sets, showing much higher generalization. On English tests, the models approach human-level performance and robustness, properly handling accents and noise. The work highlights the importance of scaling up weakly supervised pretraining data instead of just model size for speech  recognition. In summary, the paper shows weakly supervised pretraining at scale leads to highly robust speech recognition models that generalize much better to diverse settings than existing methods. The models approach human accuracy without any fine-tuning.

OpenAI's Whisper can be used for transcribing the audio form all the texts which would be the first step towards achieveing the goal of timestamping the incidents in all the videos.

## Repos

### 1. Whisper Diarization

This repository combines Whisper ASR capabilities with Voice Activity Detection (VAD) and Speaker Embedding to identify the speaker for each sentence in the transcription generated by Whisper. First, the vocals are extracted from the audio to increase the speaker embedding accuracy, then the transcription is generated using Whisper, then the timestamps are corrected and aligned using WhisperX to help minimize diarization error due to time shift. The audio is then passed into MarbleNet for VAD and segmentation to exclude silences, TitaNet is then used to extract speaker embeddings to identify the speaker for each segment, the result is then associated with the timestamps generated by WhisperX to detect the speaker for each word based on timestamps and then realigned using punctuation models to compensate for minor time shifts.

This repository achieves two important goals of this project i.e. audio transcription and speaker detection. It also timestamps each dialogue to indicate when it was spoken in the transcripts. These timestamps would come in handy when we train a Language Model on the text to detect moments such as a lack of plan, failing to offer directions, and aggressive comments.

### 2. Detoxify

Detoxify is a Python library for Toxic Comment Classification developed using PyTorch Lightning and Transformers. It provides pre-trained models and code for predicting toxicity across 3 Kaggle challenges:

- Toxic Comment Classification Challenge (2018) - Classify Toxic Comments into 6 categories (like threats, insults, etc.) using BERT's 'original' model.
- Unintended Bias in Toxicity Classification (2019) - Detect Toxicity while minimizing unintended bias towards identities using RoBERTa's 'unbiased' model.
- Multilingual Toxic Comment Classification (2020) - Classify Toxicity in comments across 7 languages using XLM-Roberta's 'multilingual' model.

The models are designed to be simple and easy to use. The code supports training new models as well as making predictions. A few limitations of this repo include potential biases towards minority groups when classifying based on profanity.

## References

[1] Davidson, Thomas, Dana Warmsley, Michael Macy, and Ingmar Weber. "Automated hate speech detection and the problem of offensive language." In Proceedings of the international AAAI conference on web and social media, vol. 11, no. 1, pp. 512-515. 2017.

[2] Prottasha, Nusrat Jahan, Abdullah As Sami, Md Kowsher, Saydul Akbar Murad, Anupam Kumar Bairagi, Mehedi Masud, and Mohammed Baz. "Transfer learning for sentiment analysis using BERT based supervised fine-tuning." Sensors 22, no. 11 (2022): 4157.

[3] Radford, Alec, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever. "Robust speech recognition via large-scale weak supervision." In International Conference on Machine Learning, pp. 28492-28518. PMLR, 2023.

[4] https://github.com/MahmoudAshraf97/whisper-diarization

[5] https://github.com/unitaryai/detoxify