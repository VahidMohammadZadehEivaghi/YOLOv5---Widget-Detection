This is an initial version of widget detection model trained based on YOLOv5 architecture. 



- The present model is trained, tested, and validated for 15000, 3500, and 3500 screenshots respectively. 
- The mean avargae precision and recall stand for 88% and 72% respectively as well.

- For making this model to inference one need to install all requirements which are listed in requirement.txt and trained weighted located in weight directory. 
- There is an inference function in main.py module which simply take two arguements, one positional and one keyword arguments. Positional arguement is the path to screenshot webpages and keywork arguements specify the type of device on which one is going to use the model, it sets on "0" by default which indicate the model is run on GPU by default. 
- Inference function returns a list of dictioary including widget names and their positions in the given URL. 
 