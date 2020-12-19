from django.db import models

# Create your models here.
class Restaurant(models.Model):
    columns = ['Table ID', 'Sourcing_competitor', 'Common_sources', 'Restaurant_name', 'Tags', 'Average basket value', 'Country', 'City_code',
     'Address', 'Latitude', 'Longitude', 'Phone_number', 'Rating', 'Number_of_reviews', 'Website', 'URL', 'Postal_code',
     'Opening_hours', 'Place ID', 'user_ratings_total', 'google_grade', 'competitor_grade1(%)', 'competitor_grade2(%)',
      'competitor_grade3(%)', 'id']
    Table_ID            = models.TextField(null=False)
    Sourcing_competitor = models.TextField(null=False)
    Common_sources      = models.TextField(null=False)
    Restaurant_name     = models.TextField(null=False)
    Tags                = models.TextField(null=False)
    Average_basket_value= models.TextField(null=False)
    Country             = models.TextField(null=False)
    City_code           = models.TextField(null=False)
    Address             = models.TextField(null=False)
    Latitude            = models.TextField(null=False)
    Longitude           = models.TextField(null=False)
    Phone_number        = models.TextField(null=False)
    Rating              = models.TextField(null=False)
    Number_of_reviews   = models.TextField(null=False)
    Website             = models.TextField(null=False)
    URL                 = models.TextField(null=False)
    Postal_code         = models.TextField(null=False)
    Place_ID            = models.TextField(null=False)
    user_ratings_total  = models.TextField(null=False)
    google_grade        = models.TextField(null=False)
