# iRail API (use case)

### What it does :
The scripts parses the [official SNCB API](http://api.irail.be/) and proposes the 6 next trains going from Nivelles to either Ath or Yvoir (3 for each destination), as JSON.

For each train journey, it shows :
* the destination
* the departure time
* the expected departure delay 
* the expected duration

### How-to use :
* install python 2.7
* install the requirements with pip
* launch the script
* visit [http://localhost:8090](http://localhost:8090)

### Potential improvements :
* by default, the API only proposes train routes, whereas the SNCB website also includes bus and metro into its routes.
* plan for inevitable API connectivity failures.
