from flask import Flask , jsonify
from flask_cors import CORS
import os 
import random
countries = [
    "Bhutan", "Monaco", "Grenada", "Romania", "Malaysia", "Chile", "Marshall Islands", 
    "Burkina Faso", "Malawi", "Kuwait", "Iceland", "Bahamas", "Sao Tome and Principe", 
    "Serbia", "Saint Vincent and the Grenadines", "Portugal", "Syria", "India", 
    "Tajikistan", "Angola", "Rwanda", "Fiji", "Costa Rica", "Mauritius", "Estonia", 
    "Saudi Arabia", "Mexico", "商Afghanistan", "Brunei", "Vietnam", "Nigeria", "China", 
    "Guatemala", "Croatia", "Netherlands", "Benin", "Madagascar", "Sweden", "Ghana", 
    "San Marino", "Swaziland", "Austria", "Slovakia", "El Salvador", "Latvia", "Samoa", 
    "Comoros", "Azerbaijan", "Macau", "Luxembourg", "Bermuda", "Cape Verde", "Senegal", 
    "Turkmenistan", "Barbados", "Seychelles", "Somalia", "Iraq", "Central African Republic", 
    "Guyana", "Aruba", "Mozambique", "Georgia", "Guinea-Bissau", "Dominican Republic", 
    "Cyprus", "Macedonia", "Andorra", "Germany", "Maldives", "Taiwan", "Egypt", "Haiti", 
    "Tonga", "Malta", "Bahrain", "Hong Kong", "United States", "Uruguay", "Chad", 
    "Mongolia", "Micronesia", "Holy See", "Hungary", "Bangladesh", "Botswana", "Liberia", 
    "Australia", "Cambodia", "Paraguay", "Djibouti", "Saint Lucia", "Togo", "Singapore", 
    "Mali", "Sri Lanka", "Uganda", "Lesotho", "Nauru", "Suriname", "Italy", "Congo", 
    "Norway", "Liechtenstein"
]
emog = [
    "🇧🇹", "🇲🇨", "🇬🇩", "🇷🇴", "🇲🇾", "🇨🇱", "🇲🇭", "🇧🇫", "🇲🇼", "🇰🇼", "🇮🇸", "🇧🇸", "🇸🇹", 
    "🇷🇸", "🇻🇨", "🇵🇹", "🇸🇾", "🇮🇳", "🇹🇯", "🇦🇴", "🇷🇼", "🇫🇯", "🇨🇷", "🇲🇺", "🇪🇪", "🇸🇦", 
    "🇲🇽", "🇦🇫", "🇧🇳", "🇻🇳", "🇳🇬", "🇨🇳", "🇬🇹", "🇭🇷", "🇳🇱", "🇧🇯", "🇲🇬", "🇸🇪", "🇬🇭", 
    "🇸🇲", "🇸🇿", "🇦🇹", "🇸🇰", "🇸🇻", "🇱🇻", "🇼🇸", "🇰🇲", "🇦🇿", "🇲🇴", "🇱🇺", "🇧🇲", "🇨🇻", 
    "🇸🇳", "🇹🇲", "🇧🇧", "🇸🇨", "🇸🇴", "🇮🇶", "🇨🇫", "🇬🇾", "🇦🇼", "🇲🇿", "🇬🇪", "🇬🇼", "🇩🇴", 
    "🇨🇾", "🇲🇰", "🇦🇩", "🇩🇪", "🇲🇻", "🇹🇼", "🇪🇬", "🇭🇹", "🇹🇴", "🇲🇹", "🇧🇭", "🇭🇰", "🇺🇸", 
    "🇺🇾", "🇹🇩", "🇲🇳", "🇫🇲", "🇻🇦", "🇭🇺", "🇧🇩", "🇧🇼", "🇱🇷", "🇦🇺", "🇰🇭", "🇵🇾", "🇩🇯", 
    "🇱🇨", "🇹🇬", "🇸🇬", "🇲🇱", "🇱🇰", "🇺🇬", "🇱🇸", "🇳🇷", "🇸🇷", "🇮🇹", "🇨🇬", "🇳🇴", "🇱🇮"
]
myshit=Flask(__name__)
CORS(myshit)
@myshit.route('/api/countries')
def select():
    index=random.randint(0,len(countries)-1)
    country_name=countries[index]
    country_emoji=emog[index]
    return jsonify(countries=country_name,short=country_emoji, source="idk but form the interent ! ! ! ")
@myshit.route('/api/data')
def urdata():
    return jsonify({"countries": countries, "emojis": emog})
if __name__ == '__main__':
   port=int(os.environ.get("PORT",5000))
   myshit.run(host='0.0.0.0', port=port)