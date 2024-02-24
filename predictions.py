from datascience import Table
from IPython.display import display
table = Table.read_table("diamonds.csv")

display(table.show(5))
