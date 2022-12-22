# lisbon-prices-small-multiples

The python script ```lisbon_prices_s_multiples.py``` makes the visualization of several datasets using Small multiples graphs. In this case study it was use the data from Lisbon house prices at local level between 1st quarter 2018 and 2nd quarter 2022.

Small multiples are sets of charts of the same type, with the same scale, presented together at a small size and with minimal detail, usually in a grid of some kind. Small multiples improves comparison when you want to compare more than 5 datasets.

![alt text](/example_view.jpg "testing")

## The dataframe

The dataframe used in this case was the file  ```INEHousingPriceData.csv```, it contains the Lisbon house prices at local level based on administrative data from [ine.pt](https://ine.pt/), "the data released refers to the median (value that separates the sorted set of prices per square meter in two equal parts) of dwellings sales (€/m2)" source: INE.

## Execution

The python script ```lisbon_prices_s_multiples.py``` runs the Dash framework with the dataframe in the file   ```INEHousingPriceData.csv``` to make the visualization of the datasets in the Plotly libray converting the standard line charts to a Small multiples, improving the comparison of Lisbon house in ten Boroughs in the list bellow.

| Lisbon house boroughs |
| ------------- |
| Areeiro |
| Arroios |
| Avenidas Novas |
| Estrela |
| Misericórdia |
| Penha de França |
| Santa Clara |
| Santa Maria Maior |
| Santo António |
| São Vicente |

## Dependencies

Make sure you have the following frameworks, libraries and modules installed:

-	Dash
-	Plotly
-	Pandas
