import pandas as pd

# add parent row indeces to each sub_row
def add_parent_row_index(df: pd.DataFrame, parent_df: pd.DataFrame) -> pd.DataFrame:
    """ Add the parent index based on the given row numbers.

    Args:
        df (`pd.DataFrame`): The DataFrame of child rows
        parent_df (`pd.DataFrame`): The DataFrame of parent rows
        check_col (`str`): The column to check

    Returns: 
        `pd.DataFrame`: `df`, except with a `parent_index` column.
    """
    
    def get_parent_index(sub_index: int) -> int:
        """ Get the parent associated with the given child row's index.

        Args:
            sub_index (`int`): Child row's index

        Returns:
            `int`: The parent index.
        """
        
        # index of the parent_discriminator rows
        parent_index = parent_df.index
        return max(parent_index[parent_index <= sub_index], default=-1)
    
    # copy the index of df
    df_index = df.index.to_series()

    # add the new column
    df.loc[:, "parent_index"] = df_index.apply(get_parent_index)
    return df
