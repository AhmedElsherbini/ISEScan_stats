# ISEScan_stats

**What is this script?**

[ISEScan](https://github.com/xiezhq/ISEScan#isescan--) is a great tool for insertion elements locator. However, if you used it for many genomes, and you want to summarize the many basic summary (.fna.sum) stats into an overview Excel sheet, then this simple Python3 script shall do this job.


**What do you need?**

You shall have the .sum files in one folder and these dependencies (pandas, openpyxl ,glob,warnings,and argparse)

Just type this command and you will get two Excel sheets in the same folder of your sum files.

"-i /--input_dir"  is your path to the directory of sum files 

"-p /--prefix"  is your preferred prefix for your run

```python
 python padloc_stats.py -i ./txt -p Corynebacterium
```

**What do you get?**


Currently, two Excel files.

1- "prefix"_frequency.xlsx (The general one like a summary of systems per the whole run).

Here you have the "frequency" of each family in your genomes

Important: this analysi igores the copy number (nIS).

2- "prefix"_presence absence.xlsx  (The more detailed one). 
