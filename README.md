# MyPyCountries Lib
> MyPyCountries : Library to get information about countries need for project [Ransomware.live](https://www.ransomware.live)


The Country Library is a Python module that offers easy access to the latitude and longitude of countries and territories around the world, based on their ISO 3166-1 alpha-2 codes. It also allows users to retrieve country codes or names based on the provided input. This module is ideal for developers needing quick geographical data without relying on external APIs.

## Features

Coordinates Lookup: Retrieve latitude and longitude by ISO country code.
Country Code Lookup: Get the ISO country code by providing a country name.
Country Name Lookup: Obtain the full country name using the ISO country code.

## Installation
To use this library, simply download the mypycountries.py file and include it in your project directory. Make sure Python is installed on your system.

## Usage
Here's how you can use the functions provided by the Country Coordinates Library:

### Getting Coordinates
Retrieve the geographic coordinates (latitude and longitude) for a given country using its ISO country code:

```python
Copy code
from country_coords import get_coordinates

coords = get_coordinates('US')
print(f"Coordinates of the United States: {coords}")
````

### Getting Country Code
Look up the ISO country code for a given country by name:

```python
Copy code
from country_coords import get_country_code

country_code = get_country_code("United States of America")
print(f"ISO country code for the United States of America: {country_code}")
```

### Getting Country Name
Get the official name of a country from its ISO country code:

```python
Copy code
from country_coords import get_country_name

country_name = get_country_name('US')
print(f"Country name for 'US': {country_name}")
````

## Contributions

Contributions to the Country Coordinates Library are welcome! If you would like to improve the module or add new features, please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the GNU License - see the LICENSE file for details.

## Acknowledgments

This data is based on ISO 3166-1 alpha-2 standards.
Thanks to all contributors who have helped in maintaining and updating the geographical data.
