# Project : Dummy Weather Data for Toy Simulation (using pyhton, pyb)

This project involves plan, scope and supporting documents (as per SDLC) to create a toy simulation of the environment 
(taking into account things like atmosphere, topography, geography, oceanography, or similar) that evolves over time. 
Then take measurements at various locations and times, and have your program emit that data, as in the following:


Location	Position	        Local Time	       Conditions	Temperature	Pressure	Humidity
						
Sydney	        -33.86,151.21,39	2015-12-23 16:02:12	Rain	        +12.5	        1010.3	        97
Melbourne	-37.83,144.98,7	        2015-12-25 02:30:55	Snow	        -5.3	        998.4	        55
Adelaide	-34.92,138.62,48	2016-01-04 23:05:37	Sunny	        +39.4	        1114.1	        12
						

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
          Solution platform : Ubuntu 18.04 on windows 10 (please refer Ubuntu 18.04 on windows 10 set up document to set up environment)
          Language Used : (my_env) amitra@AU2148238W1:~/environments$ python -V
                                                                      Python 3.6.7
          Software installation : python, pip, pyb -> Please see respective information from web
          Additional pakages : please see git Weather/requirements.txt

## 2. Directory Tree
          A file system directory structure gives an idea about how the file and folder has been structured within project environment

          ---------------------Dir Structure : Weather ----------------
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
│   │   │   ├ paylint_Score_Core_Module
│   │   │   ├ paylint_Score_helpers_module
│   │   │   ├ paylint_Score_loghelpers_module
│   │   │   ├ paylint_Score_subhelpers_module
│   │   │   ├ weather_data.dat
│   │   │   └ weather_data.log
│   │   ├ python
│   │   │   ├ core.py
│   │   │   ├ helpers.py
│   │   │   ├ loghelpers.py
│   │   │   └ subhelpers.py
│   │   └ scripts
│   └ unittest
│       └ python
│           ├ __pycache__
│           │   └ core_tests.cpython-36.pyc
│           └ core_tests.py
└ target
    ├ dist
    │   └ Weather-1.0
    │       ├ Weather.egg-info
    │       │   ├ PKG-INFO
    │       │   ├ SOURCES.txt
    │       │   ├ dependency_links.txt
    │       │   ├ namespace_packages.txt
    │       │   ├ top_level.txt
    │       │   └ zip-safe
    │       ├ __pycache__
    │       ├ build
    │       │   ├ bdist.linux-x86_64
    │       │   └ lib
    │       │       ├ core.py
    │       │       ├ helpers.py
    │       │       └ loghelpers.py
    │       ├ core.py
    │       ├ dist
    │       │   ├ Weather-1.0-py3-none-any.whl
    │       │   └ Weather-1.0.tar.gz
    │       ├ helpers.py
    │       ├ loghelpers.py
    │       ├ scripts
    │       └ setup.py
    ├ install_dependencies_constraints
    ├ logs
    │   └ install_dependencies
    │       ├ install_batch
    │       └ install_batch.err
    └ reports
-----------------------------------------------------------

## 3. Code Structure (execution) :
          
          The code structure is simpele and follows below dependencies :
 
          core.py -> helpers.py -> subhelpers.py
                                |
                                -> loghelpers.py
          Description : core.py module is the main function which calls helper.py to prepare the data, then the helpers.py calls both subhelpers.py, loghelpers.py to
                        populate data and logs the excution time.  
## 4. Output:
             Once the project executed the output file will be created on Weather->src->main->output 
             The folder consists :
             paylint_score_core_Module (Code standard score for core module)
             paylint_Score_helpers_module (Code standard score for helpers module)
             paylint_Score_loghelpers_module (Code standard score for loghelpers module)
             paylint_Score_subhelpers_module (Code standard score for subhelpers module)
             weather_data.dat (Final Output depending iterations)
             weather_data.log (Code execution log)

### Prerequisites

This project is capable to process .tif* files to generate random weather data, but for high resolution .tif* file processing it requires more processing power.

```
e.g - > 8GB Ram should process < 1 MB files very quickly.

```
    ##   Please find the steps needed to be follow before executing the project :
          1. A static 'cea.tif file to be placed in data folder (for this project) -> 
          2. A static '2018-12-21 UN/LOCODE by Country version 2018-2' file has been created from exporting ms_access db to .txt file  

          Git location: Weather/src/main/data
          UNLOCODE.txt*
          cea.tif*

 *Note you might have to change file permission depending on your env setup using -> chmod


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Avishek Mitra** - *Initial work* - amitraa2012@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc



