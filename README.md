# pop_wgt_heat_map

Package that leverages the google geocoding api to grab lat/long of addresses then creates a population weighted heat index and maps



### Getting Started

After cloning, navigate to the repo location and use conda to create the environment from the environment.yml file:

~~~
conda env create --name popheat --file "environment.yml"
~~~

Next, activate the environment:

~~~
conda activate popheat
~~~

Additionally, you'll need an api key from the Google geocoding api, which you can get here: https://developers.google.com/maps/documentation/geocoding/get-api-key

Once you get the api, you need to store it in the local repo in a json file called api_cfg.json.  The file should contain the a json dictionary that is of the format:

~~~
{"API_KEY":"YOURAPIKEYFROMGOOGLEHERE"}
~~~

The craft brewery data can be sourced from here (membership required):
https://www.brewersassociation.org/

