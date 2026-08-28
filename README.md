##Car Market Analysis 

## Objective
Analyze historical used-car data to identify pricing patterns and factors associated with selling price.

## Dataset
Car Dekho used-car dataset supplied for the DIY project.

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn.

## Key dataset checks
- Rows: 301
- Unique car models: 98
- Missing values: 0
- Duplicate rows: 2 (removed before cleaned-data analysis)

## Key findings
- Present Price has a strong positive relationship with Selling Price (correlation ≈ 0.88).
- Average selling price varies substantially by fuel type, transmission and seller type.
- Manufacturing year shows an overall upward pattern in average selling price for newer vehicles in this sample, although yearly values vary.
- Kilometers driven has a much weaker linear correlation with selling price than Present Price (correlation ≈ 0.03).

## How to run
1. Install dependencies: `pip install pandas numpy matplotlib seaborn`
2. Keep the CSV and `analysis.py` in the same folder.
3. Run `python analysis.py`.

## Note
Add the final GitHub repository URL to the PPT after pushing this folder to GitHub.
