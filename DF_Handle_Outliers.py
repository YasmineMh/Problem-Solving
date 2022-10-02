import  pandas as pd

#This function wil handle the outliers within each column of the input DataFrame
#We define an outlier as being strictly less than Q1 -1.5 IQR or strictly greater than Q3 +1.5 * IQR
# Q1 is the value at the 25th percentile of the column
# Q3 is the value at the 75th percentile of the column
# IQR = Q3 - Q1
def handle_outliers(df):
    output_df = pd.DataFrame()
    columns = list(df.columns)

    for index, i in enumerate(columns):
        Q1 = df[i].quantile(0.25)
        Q3 = df[i].quantile(0.75)
        IQR = Q3 - Q1
        outliers_less = Q1 - 1.5 * IQR
        outliers_greater = Q3 + 1.5 * IQR

        min_value = outliers_greater
        max_value = outliers_less
        for j in df[i]:
            if j >= outliers_less and j < min_value:
                min_value = j
            if j <= outliers_greater and j >  max_value:
                max_value = j

        new_column = []

        for j in df[i]:
            if j > outliers_greater:
                new_column.append(max_value)
            elif j < outliers_less:
                new_column.append(min_value)
            else:
                new_column.append(j)

        output_df['C'+str(index)] = new_column

    return output_df
        
df_before_process = pd.DataFrame({
    'C1' : [-21.57, 1.24, -0.84, 32.25, 0.82, -3.11, 0.46, -18.68, 0.04, 30.87],
    'C2' : [2.49, 2.27, 0.25, -2.33, -2.91, -3.61, 0.58, -2.59, -3.99, 1.54],
    'C3' : [1.14, 4.76, 14.23, -2.65, -3.53, -0.03, 17.50, -0.21, 2.96, 2.31]
})

print(df_before_process)
df_after_process = handle_outliers(df_before_process)
print(df_after_process)
