## Product Review Sarcasm Detection (LSSD problem)
- Sheng Liu shengliu [at] nyu [dot] edu
- New York University, NY, USA
## Table of Contents

### Project Abstract
In this modern age of social media, people find it convenient to voice their opinion through social media messages, blogs or post. Social media data has become an area of study in the fields of cognitive science, psychology, computational linguistics amongst various others. Sarcasm is a way of communication where the user hides the real meaning by using words in contrasting sense. Finding sarcasm in social media text can be challenging because it is natural to relate the sense of the word in its literal sense. Hence sarcasm detection can be viewed as word sense disambiguation task where the sense to be classified are sarcas- tic or literal. This is called as Literal/Sar- castic Sense Disambiguation (LSSD) prob- lem. This paper recreates the experiments performed by Ghosh and his colleagues us- ing the algorithm described by them in the same publication.


### Part 1: Dataset
Available corpus including annotations about whether a text is ironic or not has been published by Filatova (2012). Due to the limitted size of product reviews dataset, we adopted the twitter corpus that Ghosh et. al. used to perform their experiments for the ‘Sarcastic or Not: Word Embeddings to Predict the Literal or Sarcastic Meaning of Words’


2. download data from dropbox, click [here](https://www.dropbox.com/sh/o8q9m69583wbp7v/AADz7qg75WlrhbA-p4h50OpSa?dl=0)
to download.

4. move data folder **DataBase** into our repo 1007_project

5. Make sure that 'chorogrid', 'DataBase', 'h1b_exploring' and main_new.py are in the repo.


### Part 2 : Usage of the Application

1. This data visualization will generate four graphs with two pie plots and two bar plots: gender distribution, user type distribution, daily usage and daily miles.

2. The station frequency visualization part (option 2) will print the name of  top 5 high frequency stations and generate 3 plots automatically (close one to see the next plot).

    * Plot 1: The points of citi bike stations on the map
    * Plot 2: The top 5 high frequency stations on the map
    * Plot 3: The heat map of the station frequency

3. Recommendation and predication
    * Get information of usage of the station on that particular date on historical date and get recommendation on the station.
    * Get two alternative stations nearby which meet with the criterion: I. within 15-minute walk, II. predicted to be recommended.

### Part 3 : Configuration

1. Pandas to access data.
2. Numpy to perform statistical analysis.
3. Matplotlib for graphics including pie plots and bar plots.
4. Basemap for graphics including geometric maps.

### Part 4: How to run the program

In terminal, enter the command to run the program:

``` sh
$ cd 1007_project
$ python main_new.py
```

##### Main Menu:

- Enter a to go to a sub menu of Overview of H1b Data.
- Enter b to go to a sub menu of Location(National Level, State Level, and City Level).
- Enter c to go to a sub menu of Industry Level.
- Enter d to go to a sub menu of Company Level.


###### Option a: Overview
- Input year and month between 2013/7 and 2015/10:
  - Enter a year between 2013, 2014, 2015.
  - Enter an integer from 1 to 12 as month.
- Enter back: go back to main menu.
- Enter quit: exit the program.
- Note: close one plot will show the next plot

###### Option b: Location
- Input year and month between 2013/7 and 2015/10:
  - Enter a year between 2013, 2014, 2015.
  - Enter an integer from 1 to 12 as month.
- Enter back: go back to main menu.
- Enter quit: exit the program.
- Note: close one plot will show the next plot.

###### Option c: Prediction and recommendation

- **Note**: When customers go to a bike station, they can see the station id. So, we just use the station id as our input, which is more convenient for customers.
***You can find the station id information, station_information.pdf [here](https://drive.google.com/drive/u/2/folders/0B1ADHcCkWGbad2prZDFxdnBLN3M)***
- Enter 1 to run the prediction function, enter station ID, day, month and each end with return.
- Enter 2 to run the recommendation function, enter station ID, day, month and each end with return.
- Enter back: go back to main menu.
- Enter quit: exit the program.

###### Option d: Company Level



### Part 5: A commmon walk-through example
1. At the begining of the program, it will take seconds to load data and then you will see the Main Menu and options.
![Main_Menu](readme_materials/1.png ?raw=true =600x)
2. For example, if you would like to see the overview of the h1b data, you should type `a`, then the line chart will pop up:
![Main_Menu](readme_materials/2.png ?raw=true =600x)
3. Close the pop up window, you can type `r` to return to Main Menu. Type `b` then decide which level you are interested in. For instance, if you are interested in national level, you should type `a`, and choose the topic and year you want to see. Then you will find a **.svg** in 1007_project repo, open it with your web browser.
![Main_Menu](readme_materials/3.png ?raw=true =600x)
If you are interested in city level, type `c`, you will get a table
![Main_Menu](readme_materials/4.png ?raw=true =600x)
4. You can also find information about each company. For example, you can get information about the most popular companies. And find more detail in a **.pdf** in our repo, open it you will see
![Main_Menu](readme_materials/5.png ?raw=true =600x)
5. You can find more information about a specific company by choosing Customized Company Inquiry and enter the company name. sometimes you may forget the complete name of the company, just type in part of the name, the system will give you a list of company names that match. For example, type `goog`, you will get
![Main_Menu](readme_materials/6.png ?raw=true =600x)
6. If the company you want to see is in the list, type `yes`, you will see
![Main_Menu](readme_materials/7.png ?raw=true =600x)
7. type `quit` to exit the system.


### Part 5: Q&A
1. Where can I find data?
  - You can find it on google drive or follow the [link](https://drive.google.com/drive/u/2/folders/0B1ADHcCkWGbad2prZDFxdnBLN3M) from Part 1.

2. How to install the basemap?
  - Please follow the instruction [here](basemap_installation_guide.md)

3. What is the result for the program?
  - You can find some sample plots under the [sample_figures](sample_figures/) file.

4. What should we do, if we can not read the markdown file? 
  - We also have pdf version for our user guide and basemap installation guide.

5. How to test the program?
  - You can run the test by enter
```
$ python test.py
```


### Acknowledgement
- Data resource from ````sds````