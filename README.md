# shpock-mean-price
Calculate the mean and total price of articles sold on Shpock.com. Uses Python and Selenium.
<br>
Running the script - video of the calculation: https://www.youtube.com/watch?v=FSRPpX8036Y
<br>

## User variables:

 * <b>searchUrls</b>          - array with URLs the user wants to be searched

 * <b>excludeStrings</b>      - words and phrases which will be excluded from the searches

 * <b>minPrice & maxPrice</b> - Products must be in this range or they will be excluded from the calculations

 * <b>scrollAmounts</b>       - how many times the window will be scrolled down (results in more entries being found)

 * <b>currencySign</b>        - your local currency, e.g. "€", "£", "$"

 * <b>wait</b>                - used for sleep(int) commands in the script
