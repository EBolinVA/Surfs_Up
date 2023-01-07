# Surfs_Up
  
## Overview of the analysis: 

I love surfing and milkshakes! This is a Business Plan Analysis for a surf &amp; shake shack to be built in Hawaii, analyzing weather using SQLite, SQLAlchemy, and Flask database structures and querying methods. Python code is written and executed in a Jupyter notebook. I'll provide visualization by plotting the results of the precipitation analysis using Matplotlib.

In order to secure funding, I'll provide the investor with insight into the weather patterns of a specific location on Oahu where I want to build my shop.

## Results: 

### Query the SQLite database
-  Pull all daily temps in each of the months June and December. 
Below is the code for obtaining June temperatures from the sqlite database:

    ```
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(extract('month', Measurement.date) == 6).all()
    ```
### Provide summary statistics of daily temperatures
-  Determine summary statistics using pandas DataFrame of the extracted lists: 

    ```
    June_df.describe()
    ```
![image of June summary statistics](https://github.com/EBolinVA/Surfs_Up/blob/main/Resources/image%20files/June_temps.png)

* 1700 daily temperatures were analyzed for the month of June. The minimum temp is 64, the maximum temp is 85 and the average is a balmy 75.

    ```
    Dec_df.describe()
    ```
![image of December summary statistics](https://github.com/EBolinVA/Surfs_Up/blob/main/Resources/image%20files/December_temps.png)

* 1517 daily temperatures were analyzed for the month of December. The minimum temp is 56, the maximum temp is 83 and the average is a balmy 71.

### Visualize the daily temperatures using Matplotlib
-  Plot temperatures and print results in a histogram for each month:

    ```
    %matplotlib inline
    from matplotlib import style
    style.use('fivethirtyeight')
    import matplotlib.pyplot as plt

    June_df.plot.hist(bins=12, title="June temperatures", xlabel="temperature")
    plt.tight_layout()
    ```
![image of June temperatures histogram](https://github.com/EBolinVA/Surfs_Up/blob/main/Resources/image%20files/June_temps_histogram.png)

    ```
    Dec_df.plot.hist(bins=12, title="December temperatures", xlabel="temperature")
    plt.tight_layout()
    ```
![image of December temperatures histogram](https://github.com/EBolinVA/Surfs_Up/blob/main/Resources/image%20files/December_temps_histogram.png)

## Summary: 

The low temperatures for our location are 56-64 degrees. The high temperatures are 83 and 85 degrees. These temperatures can be considered temperate and desirable for most vacationers. 

It appears from both the summary statistics and the visual depiction in the histogram that temperatures are not vastly different when comparing June and December in our Hawaii location. Therefore, the weather remains consistent when considering both June and December temperatures. 

### Additional queries that would provide more weather data for June and December are following: 

- inches of rainfall per June, and per December

In order to get summary statistics of rainfall for June, I refactored the code for June temperatures as such:
 ```
 Prcp_results = []
 Prcp_results = session.query(Measurement.date, Measurement.prcp).\
        filter(extract('month', Measurement.date) == 6).all()

 print(Prcp_results)
 ```
The resulting statistics show little to no rainfall most days for June.
![image of summary statistics for June precipitation](https://github.com/EBolinVA/Surfs_Up/blob/main/Resources/image%20files/June_prcp_stats.png)

Similarly, there is little rainfall in December, although it appears to be a little rainier than June.
![image of summary statistics for December precipitation](https://github.com/EBolinVA/Surfs_Up/blob/main/Resources/image%20files/December_prcp_stats.png)

