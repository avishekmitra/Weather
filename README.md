# Project : Dummy Weather Data for Toy Simulation (using pyhton, pyb)

This project involves plan, scope and supporting documents (as per SDLC) to create a toy simulation of the environment 
(taking into account things like atmosphere, topography, geography, oceanography, or similar) that evolves over time. 
Then take measurements at various locations and times, and have your program emit that data, as in the following:


Location|Position|Local Time|Conditions|Temperature|Pressure|Humidity
						

Output of the data will be in the following format:
------------------------------------------------------------------
Sydney|-33.86,151.21,39|2015-12-23T05:02:12Z|Rain|+12.5|1004.3|97

Melbourne|-37.83,144.98,7|2015-12-24T15:30:55Z|Snow|-5.3|998.4|55

Adelaide|-34.92,138.62,48|2016-01-03T12:35:37Z|Sunny|+39.4|1114.1|12

where

•	Location is an optional label describing one or more positions,

•	Position is a comma-separated triple containing latitude, longitude, and elevation in metres above sea level,

•	Local time is an ISO8601 date time,

•	Conditions is either Snow, Rain, Sunny,

•	Temperature is in °C,

•	Pressure is in hPa, and

•	Relative humidity is a %.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

## 1. Sotuion environment
          OS : Windows 10
          Solution platform : Ubuntu 18.04 on windows 10 (please refer Ubuntu 18.04 on 
                              windows 10 set up document to set up environment)
          Language Used : Python 3.6.7
          Software installation : python, pip, pyb -> Please see respective information from web
          Additional pakages : please see git Weather/requirements.txt

## 2. Directory Tree
          
A sample file system directory structure gives an idea about how the file and folder has been structured within project environment.

          
         ## ---------------------Dir Structure : Weather ----------------
          Weather
            ├ LICENSE
            ├ README.md
            ├ __init__.py
            ├ build.py
            ├ requirements.txt
            ├ setup.py
            ├ src
            │   ├ main
            │   │   ├ data
            │   │   │   ├ UNLOCODE.txt
            │   │   │   └ cea.tif
            │   │   ├ output
            │   │   │       
            │   │   │   ├ weather_data.dat
            │   │   │   └ weather_data.log
            │   │   ├ python
            │   │   │   ├ core.py
            │   │   │   ├ helpers.py
            │   │   │   ├ loghelpers.py
            │   │   │   └ subhelpers.py
            │   │   └ scripts
            │   └ unittest
          

## 3. Code Structure (execution) :
          
          The code structure is simpele and follows below dependencies :
 
          core.py -> helpers.py -> subhelpers.py
                   | 
                   |-> loghelpers.py

          Description : core.py module is the main functio/module which calls helpers.py to prepare the data, and loghelpers.py to create execution log.  
                        Then the helpers.py calls subhelpers.py module which helpes helpers.py to populate weather data.  
## 4. Output:
          Once the project executed the output file will be created on Weather->src->main->output 
          The outout folder (Weather/src/main/output/ consists:
          1. weather_data.dat (Final Output depending iterations)
          2. weather_data.log (Code execution log)

### Prerequisites

This project is capable to process .tif* files to generate random weather data, but for high resolution .tif* file processing it requires more processing power.

          ```
          e.g - > 8GB Ram should process < 1 MB files very quickly.

          ```
          P.S: The weather data cities are currently defaulted to 'US' as country, we can make it dynamic by capturing localisation variable.
    ##   Please find the steps needed to be follow before executing the project :
          1. A static 'weather.tif file to be placed in data folder (for this project). 
          2. A static '2018-12-21 UN/LOCODE by Country version 2018-2' file has been created from exporting ms_access db to .txt file.  

          Source files Git location: Weather/src/main/data
          UNLOCODE.txt*
          weather.tif*

          *Note: We can use any .tif file which stores weather data but you have to rename it to weather.tif and place to data folder.
          you might have to change file permission depending on your env setup. use chmod for unix/linux


### Installing

A step by step series of installation to get the dev environment build : 

           Steps:
             1. Install Ubuntu 18.04 on windows 10 (url: )
             2. Install python 
             3. Install pip
             5. Install pylint
             6. Install Py builder (http://pybuilder.github.io/)
             7. Install external pakages (refer : requirements.txt) 



## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

pylint has been used to check coding style ->

Below are the scores : 
          # Command line : pylint <yourcode.py>
          #Location(git) -> Weather/src/main/codestandard
            paylint_score_core_Module (Code standard score for core module)
            paylint_Score_helpers_module (Code standard score for helpers module)
            paylint_Score_loghelpers_module (Code standard score for loghelpers module)
            paylint_Score_subhelpers_module (Code standard score for subhelpers module)


## Deployment

 

## Built With

*  Py builder

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Avishek Mitra** - *Initial work* - amitraa2012@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* pyhton community
* who have had used their brain to generate weather data
* raster process community



