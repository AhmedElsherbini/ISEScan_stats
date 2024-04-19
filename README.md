# ISEScan_stats

**What is this script?**

[ISEScan](https://github.com/xiezhq/ISEScan#isescan--) is a great tool for insertion elements locator. However, if you used it for many genomes, and you want to summarize the many basic summary (.fna.sum) stats into an overview Excel sheet, then this simple Python3 script shall do this job.


**What do you need?**

This script is working on python3.9

You shall have the .sum files in one folder and these dependencies (pandas, openpyxl ,glob, warnings,and argparse)

Just type this command and you will get two Excel sheets in the same folder of your sum files.

"-i /--input_dir"  is your path to the directory of sum files.

"-p /--prefix"  is your preferred prefix for your run


```python
python ise_stats_with_nis.py -i summ_folder/ -p Trial_two
```
Important: This analysis **uses** the copy number (nIS) for your frequency or your heatmap. 


**What do you get?**


Currently, two CSV files.

1- "prefix"_frequency.csv (The general one like a summary of systems per the whole run).

Here you have the "frequency" of each family in your genomes


2- "prefix"_heatmap.csv  (The more detailed one).Easy to feed to R heatmaps.
