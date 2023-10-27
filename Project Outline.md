# Project Document Template

## _Authors: Sai Krishna Sashank Madipally, Aakash Bhatnagar and Krishna Adithya Venkatesh,  2023-10-15, v1.0.1-dev_


## Summary/Overview

# Project Summary: Automated Analysis of Body Camera Footage

## Situation and Current Issues
In this project, our client represets victims of police brutality, false arrest, wrongful death, and civil rights violations. A critical aspect of these cases involves analyzing body camera footage, which can vary greatly in length from minutes to hours. The current manual review process is time-consuming and labor-intensive. The aim of this project is to use AI to find moments where:
1. Officers complain about the lack of a plan
2. Officers fail to offer people with directions
3. Officers direct aggressive comments at protestors

## Key Questions
- How can we extract timestamps from all the videos everytime one of the above actions took place?
- How can we make this extraction efficiently and effectively?
- How can AI be leveraged to streamline this analysis without compromising accuracy?

## Hypothesis: Overview of How it Could Be Done
The project aims to develop an automated system for the analysis of body camera footage. This system will utilize advanced Automatic Speech Recognition (ASR) and Natural Language Processing (NLP) techniques to identify and extract specific actions and events from the videos. These ASR and NLP models could be programmed to recognize instances of aggressive comments and lack of a plan. Additionally, the system could generate searchable metadata associated with each video clip.

## Impact
If successfully completed, this project would have significant positive outcomes for all stakeholders involved:

- **Lawyers and Legal Team:**
  - *Desired Outcome:* Increased efficiency in reviewing body camera footage, allowing for more comprehensive analysis in less time.
  - *Impact:* Reduced manual labor, faster identification of critical evidence, and improved preparation for legal proceedings. This could lead to stronger cases and potentially higher success rates in lawsuits.

- **Victims and Plaintiffs:**
  - *Desired Outcome:* Thorough and accurate representation in the court case against the BPD, ensuring justice is served.
  - *Impact:* Improved chances of obtaining fair compensation and accountability. This could lead to a sense of closure and justice.

- **Overall Business Value:**
  - *Desired Outcome:* Enhanced reputation and increased effectiveness in advocating for victims in the court case.
  - *Impact:* AI is here to stay. The use of AI in an ongoing civil rights case could stand as an example for the future use of AI in this space.



### A. Problem Statement:

Our client requires an efficient and accurate method using AI for analyzing body camera footage involving police brutality, aggressive comments, and lack of planning. The current manual review process is time-consuming and labor-intensive, leading to inefficiencies in case preparation.

### B. Checklist for Project Completion:

- Train/Implement ASR model(s) to extract a transcript of the audio in all videos
- Train/Implement NLP model(s) on the extracted text.
- Identify and timestamp specific events (e.g., lack of planning, aggressive comments, and failure to provide directions to protestors) from the videos.

### C. Solution in Terms of Human Actions:

1. Listen to the recordings to identify instances where foul language or bad phrases were used by BPD and note the timestamp.
2. Listen to the recordings to identify instances where BPD criticizes the lack of a plan and fail to offer protestors directions and note the timestamps.
3. Listen to the recordings and verify the performance of the model after it makes predictions for fine-tuning the model(s).
4. Perform EDA on the dataset to find any insights into the videos that might be useful while training.

### D. Solution in Terms of Machine Learning Tasks:

1. Train a Speech Recognition model to transcribe the audio from all the bodycam videos.
2. Preprocess the text retrieved in Step 1.
3. Train an NLP model on this preprocessed data to recognize the three actions.
4. Recognize and timestamp the actions using the NLP model.
5. Extract these moments in the videos using the timestamps from Step 4.

### E. Path to Operationalization:

The automated analysis system produced by this project can be accessed through a user-friendly interface, allowing legal teams to upload body camera footage for analysis. The system can generate detailed reports with identified actions/events, along with timestamps for reference. The technology stack may include Python for backend processing. The end user, in this case, would be legal professionals, who can utilize this tool to enhance their case preparation process.

The code and analysis of the data can be accessed at this [repo](https://github.com/k-sashank/ml-nlgma-body-cam) and the data (bodycam videos) can be accessed [here](https://drive.google.com/drive/u/1/folders/1eMsS2tl9cgiBJ25kAfu4jjsFu1nvtnS0).



## Resources

### Data Sets
* [BPD Body Cam Videos](https://drive.google.com/drive/u/1/folders/1eMsS2tl9cgiBJ25kAfu4jjsFu1nvtnS0)

### References
1. "Robust speech recognition via large-scale weak supervision." Radford, Alec, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever. In International Conference on Machine Learning, pp. 28492-28518. PMLR, 2023.
2. TweetNLP: Cutting-Edge Natural Language Processing for Social Media. Jose Camacho-collados, Kiamehr Rezaee, Talayeh Riahi, Asahi Ushio, Daniel Loureiro, Dimosthenis Antypas, Joanne Boisson, Luis Espinosa Anke, Fangyu Liu, Eugenio Martínez Cámara
3. SS-BERT: Mitigating Identity Terms Bias in Toxic Comment Classification by Utilising the Notion of "Subjectivity" and "Identity Terms" Zhixue Zhao, Ziqi Zhang, Frank Hopfgartner
4. AWS Trascribe: https://aws.amazon.com/pm/transcribe/?trk=8217174a-004c-4464-9374-7f64e3ed195f&sc_channel=ps&ef_id=CjwKCAjw4P6oBhBsEiwAKYVkqwAvaFINIQKcux3_g2kpJJZMjTn43_EyqGGfqNwF0A7g4ufmeQcE3xoCwIUQAvD_BwE:G:s&s_kwcid=AL!4422!3!652240143550!p!!g!!amazon%20transcribe%20service!19878157838!
5. MTEB: Massive Text Embedding Benchmark. Muennighoff, Niklas and Tazi, Nouamane and Magne, Lo{\"\i}c and Reimers, Nils
6. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. Alexey Dosovitskiy, Lucas Beyer, Alexander KolesnikovAlexander_Kolesnikov2, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby, Neil_Houlsby1





## Weekly Meeting Updates

[Click Here](https://docs.google.com/document/d/1yBMbNlGdPpKdbqIZcFRiYo6AghhWJ1reWf3ohdllhak/edit?usp=sharing) for Weekly Meeting Updates Document.
