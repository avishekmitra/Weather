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
          1. weather_data.dat (Final output dependent on numer of weather iterations)
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

          Data folder Git location: Weather/src/main/data
          UNLOCODE.txt*
          weather.tif*

          *Note: You can use any .tif file which stores weather data but you have to rename it to weather.tif and place to data folder.
          you might have to change file permission depending on your env setup. use chmod for unix/linux


### Installing

A step by step series of installation to get the dev environment build : 

           Steps:
             1. Install Ubuntu 18.04 on windows 10
             2. Install python 3.7
             3. Install pip
             5. Install pylint
             6. Install Py builder (http://pybuilder.github.io/)
             7. Install external pakages (refer : requirements.txt) 



## Running the tests

Unit test scripts are located at
/Weather/src/unittest/python
2 Sample test scripts are present on above directory

                    Testing requirement

            1. Due to some PATH veriable issue implicitly defined src path in unit test scripts
            -------------------
            import sys
            sys.path.append('/home/amitra/environments/Weather/src/main/python')
            -----------------------
            2. Special care needed when you will build the project in your local environment.
            You have to create a data folder inside ~/environments and place your 'weather.tif' file when running pyb build.


### Coding style tests

pylint has been used to check coding style ->

Below are the scores : 
            Command line : pylint <yourcode.py>
            Location(git) -> Weather/src/main/codestandard
            paylint_score_core_Module (Code standard score for core module)
            paylint_Score_helpers_module (Code standard score for helpers module)
            paylint_Score_loghelpers_module (Code standard score for loghelpers module)
            paylint_Score_subhelpers_module (Code standard score for subhelpers module)

  
## Deployment

Using Py builder -> please Py builder reference
(my_env) <user-domain>:~/environments/Weather$ pip install ~/environments/Weather/target/dist/Weather-1.0/dist/Weather-1.0.tar.gz




## Built With

Build using Py builder(build.py stores the build parameters):
------------------------------------------------------------ 
 
(my_env) <user-domain>:~/environments/Weather$ pyb
PyBuilder version 0.11.17
Build started at 2019-02-17 23:28:04
------------------------------------------------------------
[INFO]  Building Weather version 1.0
[INFO]  Executing build in /home/amitra/environments/Weather
[INFO]  Going to execute task publish
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /home/amitra/environments/Weather/src/unittest/python
[INFO]  Executed 2 unit tests
[INFO]  All unit tests passed.
[INFO]  Building distribution in /home/amitra/environments/Weather/target/dist/Weather-1.0
[INFO]  Copying scripts to /home/amitra/environments/Weather/target/dist/Weather-1.0/scripts
[INFO]  Writing setup.py as /home/amitra/environments/Weather/target/dist/Weather-1.0/setup.py
[INFO]  Collecting coverage information
[WARN]  coverage_branch_threshold_warn is 0 and branch coverage will not be checked
[WARN]  coverage_branch_partial_threshold_warn is 0 and partial branch coverage will not be checked
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /home/amitra/environments/Weather/src/unittest/python
[INFO]  Executed 2 unit tests
[INFO]  All unit tests passed.
[WARN]  Module '__init__' was not imported by the covered tests
[WARN]  Module 'core' was not imported by the covered tests
[WARN]  Test coverage below 70% for core:  0%
[WARN]  Test coverage below 70% for helpers: 41%
[WARN]  Test coverage below 70% for loghelpers:  0%
[WARN]  Overall coverage is below 70%: 30%
[INFO]  Overall coverage branch coverage is 25%
[INFO]  Overall coverage partial branch coverage is 91%
[INFO]  Building binary distribution in /home/amitra/environments/Weather/target/dist/Weather-1.0
------------------------------------------------------------
BUILD SUCCESSFUL
------------------------------------------------------------
Build Summary
             Project: Weather
             Version: 1.0
      Base directory: /home/amitra/environments/Weather
        Environments:
               Tasks: prepare [727 ms] compile_sources [0 ms] run_unit_tests [974 ms] package [144 ms] run_integration_tests [0 ms] verify [2499 ms] publish [2199 ms]
Build finished at 2019-02-17 23:28:11
Build took 6 seconds (6641 ms)

## Versioning

See version comments on Git.

## Authors

* **Avishek Mitra** - *Initial work* - amitraa2012@gmail.com

## License

see the LICENSE.md file for details

## Acknowledgments

* pyhton community
* who have had used their brain to generate weather data
* pyhton community worked on raster filr process
* Reference code from same problem statement



