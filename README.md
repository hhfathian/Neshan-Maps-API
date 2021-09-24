# Neshan-Maps-API
Using neshan maps api for geolocation analysis like distance and duration between locations, finding the municipality zone of a location, etc. 

neshan website: https://platform.neshan.org/api


responce format: 
{
	"status": "Ok",
	"rows": [
    	{
        	"elements": [
            	{
                	"status": "Ok",
                	"duration": {
                    	"value": 699,
                    	"text": "۱۲ دقیقه"
                	},
                	"distance": {
                    	"value": 8332,
                    	"text": "۸ کیلومتر"
                	}
            	},
            	{
                	"status": "Ok",
                	"duration": {
                    	"value": 605,
                    	"text": "۱۰ دقیقه"
                	},
                	"distance": {
                    	"value": 5373,
                    	"text": "۵ کیلومتر"
                	}
            	}
        	]
    	},
    	{
        	"elements": [
            	{
                	"status": "Ok",
                	"duration": {
                    	"value": 511,
                    	"text": "۹ دقیقه"
                	},
                	"distance": {
                    	"value": 5317,
                    	"text": "۵ کیلومتر"
                	}
            	},
            	{
                	"status": "Ok",
                	"duration": {
                    	"value": 69,
                    	"text": "۱ دقیقه"
                	},
                	"distance": {
                    	"value": 389,
                    	"text": "۴۰۰ متر"
                	}
            	}
        	]
    	}
	],
	"origin_addresses": [
    	"36.317559,59.532226",
    	"36.337077,59.530843"
	],
	"destination_addresses": [
    	"36.350681,59.545227",
    	"36.337012,59.530023"
	]
}
