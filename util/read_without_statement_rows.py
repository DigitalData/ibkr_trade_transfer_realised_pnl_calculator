import pandas as pd

# remove extra IBKR header rows
def read_without_statement_rows(filepath: str):
    """ Read the `.csv` file without the statement rows.

    Args:
        filepath (str): The filepath of the IBKR report relative to this notebook.

    Returns:
        `Pandas.DataFrame`: The resulting data in this file without statement rows.
    """

    # open the file context
    with open(filepath) as f:
        
        # create a list of the output lines
        out_lines = []
        
        # iter on lines and add if not statement
        for l in f.readlines():
            row_cells = l.split(",")
            if "statement" in row_cells[0].lower(): continue
            out_lines += [l]
            
        # get the filename (without folder)
        filename = filepath.split("/")[-1]
        clean_filepath = f"./data/cleaned/without_statements/{filename}"

        # write to the file
        with open(clean_filepath, "w") as f:
            f.writelines(out_lines)

        # create the dataframe
        return pd.read_csv(clean_filepath)