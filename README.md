# Amazon Catalog Scrapping Using Selenium
Made a web scrapping script, which scraps product information from amazon on searching some specific query using selenium module, and storing the name, original price, discounted price and the link of the product to a csv file using pandas module.

This is a pretty straightforward way to scrap the product information, but before running the script, make sure you have a rotating proxy server setup. It protects your original IP address from getting banned from amazon. 

First install all the required dependencies with the following command
```bash
pip install -r requirements.txt
```

Now run the main scrapping code, which would scrap the data. Feel free to replace the `element` variable in the code with something of your own choice. 
```bash
python scrapper.py
```
The link might need to be updated as it changes dynamically for different user.

After the above code gets executed without any error, you would see the `data/` folder populated with the html files, each containing some product information of the searched query

Now, its time to parse the necessary information from this sheet.
```
python collector.py
```
After the above code is finished executing properly, the data.csv is populated with the required entries.

Though I used selenium for scrapping purpose, but it is mainly used by testers to check the durability of a site with edge case inputs. 

Feel free to submit issues or pull requests to improve this API. Was just learning about flask and dockerfiles.

**Connect with me on**:
* [Linkedin](https://www.linkedin.com/in/siddharth-chaberia/)
* [Telegram](https://t.me/SiddharthChaberia)
* [Facebook](https://www.facebook.com/chaberia.siddharth/)
* [Instagram](https://www.instagram.com/siddharth_chaberia_02/)
* [Twitter](https://x.com/03Chaberia)
