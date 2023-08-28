INSTRUCTIONS TO LOAD THE SENTIMENT ANALYSIS PROJECT

LIBRARIES #Install and import the following Libraries.
pandas
numpy
matplotlib
seaborn
openai
random
torch
spacy



FOR THE INTRODUCTORY PROJECT
Sign Up for the OpenAI API and Obtain an API Key. Replace the ""YOUR_API_KEY_HERE" with your actual API key
#Create a Sentiment Analysis Prompt :
#Call the ChatGPT API for Sentiment Analysis




FOR THE MAIN PROJECT

About the dataset -> We will utilize the International Movie Database (IMDb) review dataset for sentiment analysis. 
This dataset comprises 50,000 movie reviews from a global spectrum, and it's organized for binary classification,
labeling each review as either positive or negative. 
The dataset is divided into 25,000 samples for training and an equal count of 25,000 samples for testing. 


The IMDb dataset available through the TorchText library's datasets module. The datasets.IMDB.splits(txt, labels) function call is used to load the IMDb dataset.

To ACCESS the dataset, visit http://ai.stanford.edu/~amaas/data/sentiment/

NOTE: the dataset is balanced between positives and negatives then we created another validation dataset

EXECUTION
we have added comments inbetween codes for you to have a better understaning of everything done. 
run the cells one after the other, try not to run the next cell when the one before it has not finished. 
you can adjust your batches if you want it to run faster. 




