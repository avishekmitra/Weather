# Project Title

This project involves plan, scope and supporting document (as per SDLC) to Create a toy simulation of the environment (taking into account things like atmosphere, topography, geography, oceanography, or similar) that evolves over time. Then take measurements at various locations and times, and have your program emit that data, as in the following:


Location	Position	        Local Time	       Conditions	Temperature	Pressure	Humidity
						
Sydney	        -33.86,151.21,39	2015-12-23 16:02:12	Rain	        +12.5	        1010.3	        97
Melbourne	-37.83,144.98,7	        2015-12-25 02:30:55	Snow	        -5.3	        998.4	        55
Adelaide	-34.92,138.62,48	2016-01-04 23:05:37	Sunny	        +39.4	        1114.1	        12
						

Obviously you can’t give it to us as a table (ok, yes, you could feed us markdown, but let’s not do that?) so instead submit your data to us in the following format:

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
          Additional pakages : please see git Weather/requirements.txt

### Prerequisites

This project is capable to process .tif* files to generate random weather data, but for high resolution .tif* file processing it requires more processing power.

```
e.g - > 8GB Ram should process < 1 MB files very quickly.

```
Please find the steps needed to be follow before executing the project :
  1. A static 'cea.tif file to be placed in data folder (for this project) -> 
  2. A static '2018-12-21 UN/LOCODE by Country version 2018-2' file has been created from exporting ms_access db to .txt file  

~/environments/Weather/src/main/data$ ll
 -rwxrwxrwx 1 amitra amitra 2781761 Feb 14 14:34 UNLOCODE.txt*
 -rwxrwxrwx 1 amitra amitra  270993 Feb 13 17:23 cea.tif*

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



