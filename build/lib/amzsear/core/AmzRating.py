import re

try:
    from amzsear.core.AmzBase import AmzBase
    from amzsear.core import requires_valid_data, capture_exception
except ImportError:
    from .amzsear.core.AmzBase import AmzBase
    from .amzsear.core import requires_valid_data, capture_exception


"""
    AmzRating(html_element=None):

    The AmzRating class extends the AmzBase class and, as such the following
    attributes are available to be called as an index call or as an attribute:

        ratings_text (str): The star rating (e.g. "4.5/5").
        ratings_count_text (str): The number of votes (e.g. "100").

    This class should usually not be instantiated directly (rather be used as
    part of an AmzProduct element) but can be created by passing an HTML element
    to the constructor. If nothing is passed, an empty AmzRating object is created.

    Optional Args:
        html_element (LXML root): A root for an HTML tree derived from an element
          on an Amazon search page.
"""
class AmzRating(AmzBase):
    ratings_text = None
    ratings_count_text = None
    _all_attrs = ['ratings_text', 'ratings_count_text']

    """
        Constructor takes an lxml Element and extracts (if possible)
          the first ratings text and ratings count text
    """
    def __init__(self, html_element=None):
        if html_element != None:
            (ratings_text, ratings_count_text) = self._get_from_html(html_element)

            # Values are only set if there are 2 ratings_text floats (the text should
            #  be of the form "N out of N stars") and one ratings_count float (the text
            #  should be of the form "N").

            if (len(self._extract_all_values(ratings_text)) == 2 and 
              len(self._extract_all_values(ratings_count_text)) == 1):

                self.ratings_text = ratings_text
                self.ratings_count_text = ratings_count_text
                self._is_valid = True


    """
        Private method - extracts the ratings text and count from the lxml element passed.

        Returns:
            tuple: Tuple of the ratings text followed by (a string of) the count
              for the rating. Both of these are strings.
    """
    @capture_exception(IndexError, ('',''))
    def _get_from_html(self, root):
        ratings_text = root.cssselect('i[class*="star"]')[0].text_content()
        ratings_count_text = root.cssselect('a[href*="customerReviews"]')[0].text_content()

        return (ratings_text,ratings_count_text)

    """
        Private method - extracts any numbers from some text.

        e.g. _extract_all_values("4.5 out of 5 stars") == [4.5, 5.0]

        Optional Args:
            data(str): The string to extract from. If not data is passed
              the ratings_text attribute is used.

        Returns:
            list: List of floats for any numbers in the text.

    """
    def _extract_all_values(self, data=None):
        if data == None:
            data = self.ratings_text

        return [float(re.sub('[^\d.]','',x)) for x in re.findall('[\d.,-]+',data)]

    """
        Gets a percentage value of the rating - 0% being a 0/5 star rating and
        100% being a 5/5 star rating.

        Returns:
            float: The star percentage.
    """
    @requires_valid_data(default=0)
    def get_perc(self):
        return self.get_numerator()/self.get_denominator()
 
    """
        Gets the value the average value of the star rating (usually between 0 and 5).

        Returns:
            float: The numerator of the star rating.
    """
    @requires_valid_data(default=0)
    def get_numerator(self):
        return sorted(self._extract_all_values())[0]

    """
        Gets the value the star rating is out of (usually 5).

        Returns:
            float: The denominator of the star rating.
    """ 
    @requires_valid_data(default=0)
    def get_denominator(self):
        return sorted(self._extract_all_values())[-1]

    """
        Gets the total number of ratings.

        Returns:
            int: The number of ratings.
    """ 
    @requires_valid_data(default=0)
    def get_count(self):
        return int(self._extract_all_values(self.ratings_count_text)[0])

    """
        Gives a visual representation of the star rating, rounding to the nearest star.

        Optional Args:
            star_repr(str): A (typically) single character used to represent a star.

        Returns:
            str: A representation of the star rating.
    """
    @requires_valid_data(default='')
    def get_star_repr(self,star_repr='*'):
        return star_repr*round(self.get_numerator())
