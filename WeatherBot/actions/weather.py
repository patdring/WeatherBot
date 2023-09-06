from bs4 import BeautifulSoup as bs
import requests

"""Code ist based on https://github.com/x4nth055/pythoncode-tutorials/tree/master/web-scraping/weather-extractor"""

"""Constant to simualte a browser session request"""
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"
URL = "https://www.google.com/search?ie=UTF-8&hl=en&lr=lang_en&q=weather"

class Weather:
    """
    A class that retrieves weather data from google.com for a specific location or based on the IP address of a specific location.

    Attributes
    ----------
    session : Session
        Browser session for interaction with google.com

    Methods
    -------
    getTemperature(region=""): str
        Returns the current temperature in °C for a location/region
    getRegion(region=""): str
        Returns the current location based on your IP address
    getDescription(region=""): str
        Returns a weather description (e.g. cloudy, sunny) for a location/region
    getPrecipitation(region=""): str
        Returns current precipitation in % for a location/region
    getHumidity(region=""): str
        Returns current humidity in % for a location/region
    getWind(region=""): str
        Returns current wind speed in km/h for a location/region
    getForecast(region=""): list
        Returns weather forecast data a location/region
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Weather object.
        """
        
        self.session = requests.Session()
        self.session.headers['User-Agent'] = USER_AGENT
        self.session.headers['Accept-Language'] = LANGUAGE
        self.session.headers['Content-Language'] = LANGUAGE
    
    def getTemperature(self, region=""):
        """
        Returns the current temperature in °C for a location/region

        If the argument 'region' is passed, then then the location 
        determined from the IP address is not used, 
        but the specified area, such as Berlin.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        data (str): Temperature in °C
        """

        if region:
            region = region.replace(" ", "+")
            url = URL + f"+{region}"
        else:
            url = URL
        html = self.session.get(url)
        soup = bs(html.text, "html.parser")
        data =  soup.find("span", attrs={"id": "wob_tm"}).text
        
        return data
    
    def getRegion(self, region=""):
        """
        Returns the current location based on your IP address

        If the argument 'region' is passed, then then the location 
        determined from the IP address is not used, 
        but the specified area, such as Berlin.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        data (str): Current location/region based on your IP address
        """

        if region:
            region = region.replace(" ", "+")
            url = URL + f"+{region}"
        else:
            url = URL
        html = self.session.get(url)
        soup = bs(html.text, "html.parser")
        data =  soup.find("div", attrs={"id": "wob_loc"}).text
        return data
    
    def getDescription(self, region=""):
        """
        Returns a weather description (e.g. cloudy, sunny) for a location/region

        If the argument 'region' is passed, then then the location 
        determined from the IP address is not used, 
        but the specified area, such as Berlin.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        data (str): Description (e.g. cloudy, sunny)
        """

        if region:
            region = region.replace(" ", "+")
            url = URL + f"+{region}"
        else:
            url = URL
        html = self.session.get(url)
        soup = bs(html.text, "html.parser")
        data =  soup.find("span", attrs={"id": "wob_dc"}).text
        return data
    
    def getPrecipitation(self, region=""):
        """
        Returns current precipitation in % for a location/region

        If the argument 'region' is passed, then then the location 
        determined from the IP address is not used, 
        but the specified area, such as Berlin.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        data (str): Precipitation in %
        """

        if region:
            region = region.replace(" ", "+")
            url = URL + f"+{region}"
        else:
            url = URL
        html = self.session.get(url)
        soup = bs(html.text, "html.parser")
        data =  soup.find("span", attrs={"id": "wob_pp"}).text
        return data

    def getHumidity(self, region=""):
        """
        Returns current humidity in % for a location/region

        If the argument 'region' is passed, then then the location 
        determined from the IP address is not used, 
        but the specified area, such as Berlin.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        data (str): Humidity in %
        """

        if region:
            region = region.replace(" ", "+")
            url = URL + f"+{region}"
        else:
            url = URL
        html = self.session.get(url)
        soup = bs(html.text, "html.parser")
        data =  soup.find("span", attrs={"id": "wob_hm"}).text
        return data
    
    def getWind(self, region=""):
        """
        Returns current wind speed in km/h for a location/region.

        If the argument 'region' is passed, then then the location 
        determined from the IP address is not used, 
        but the specified area, such as Berlin.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        data (str): wind speed in km/h
        """

        if region:
            region = region.replace(" ", "+")
            url = URL + f"+{region}"
        else:
            url = URL
        html = self.session.get(url)
        soup = bs(html.text, "html.parser")
        data =  soup.find("span", attrs={"id": "wob_ws"}).text
        return data
    
    def getForecast(self, region=""):
        """
        Returns weather forecast data for the next 7 days 
        (total 8 days with description, min., max., temperature)
        based on your IP address.

        If the argument 'region' is passed, then then the location 
        determined from the IP address is not used, 
        but the specified area, such as Berlin.

        Parameters
        ----------
        region : str, optional
            Specific location (default is location based on IP adress)

        Returns
        -------
        next_days (list): weather forecast data
        """

        if region:
            region = region.replace(" ", "+")
            url = URL + f"+{region}"
        else:
            url = URL
        html = self.session.get(url)
        soup = bs(html.text, "html.parser")

        next_days = []
        days = soup.find("div", attrs={"id": "wob_dp"})
        for day in days.findAll("div", attrs={"class": "wob_df"}):
            # extract the name of the day
            day_name = day.findAll("div")[0].attrs['aria-label']
            # get weather status for that day
            weather = day.find("img").attrs["alt"]
            temp = day.findAll("span", {"class": "wob_t"})
            # maximum temparature 
            max_temp = temp[0].text
            # minimum temparature 
            min_temp = temp[2].text
            next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
        return next_days