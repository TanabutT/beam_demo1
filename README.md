# Apache Beam CSV Processing Demo

This project demonstrates a simple Apache Beam pipeline for processing CSV files.

## Overview

The pipeline reads an input CSV file, transforms each row by removing the last column, and writes the result to an output file.

## Files

- `simplecsv.py` - Main Apache Beam pipeline script
- `input.csv` - Sample input file
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Setup

1. Create a virtual environment with Python 3.12:
```bash
python3.12 -m venv venv312
source venv312/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Pipeline

Execute the script with input and output file arguments:

```bash
python simplecsv.py --input_file_name input.csv --output_file_name output.csv
```
or
```bash
python3.12 simplecsv.py
```

## Input Format

The input CSV should have comma-separated values. The pipeline removes the last column from each row.

## Output Format

The output will be written to files with a naming pattern like `output.csv-00000-of-00001`. This is standard for Apache Beam, which splits output into shards even when running on a single worker.

## Pipeline Components

### transformcsv
A custom DoFn that:
1. Splits each input line on commas
2. Removes the last element from the resulting list
3. Returns the modified row

### Example
Input: `value1,value2,value3,extra`
Output: `['value1', 'value2', 'value3']`

## Dependencies

- Apache Beam 2.69.0
- Python 3.12+

## Project Structure

```
beam_demo1/
├── simplecsv.py      # Main pipeline implementation
├── input.csv         # Sample input file
├── output.csv-00000-of-00001  # Output file (generated)
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── venv312/          # Virtual environment (excluded from git)
```

## Running Tests

To test the pipeline with your own data:
1. Place your CSV file in the project directory
2. Update the input and output filenames in the command
3. Execute the pipeline as shown above

## Tips

- The output file naming convention (`{filename}-{shard}-of-{total-shards}`) is standard in Apache Beam
- To merge output files for smaller datasets, you can manually concatenate them
- For large datasets, the parallel processing capability of Apache Beam will create multiple output files
