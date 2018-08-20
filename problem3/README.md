This project was bootstrapped with [Create React App](https://github.com/facebookincubator/create-react-app).

#Install

To begin, navigate to the directory and enter the following command in your terminal to start:

```
  yarn start
```

#Prompt
Please provide any well-commented Javascript source code using the standard libraries of your choice. Commonplace and well-tested libraries are preferred to exotic ones.

##Problem
Construct an interface for displaying a simple table, represented as a CSV file. During your in-person interview, we will provide a CSV file for you to demonstrate your code. It will conform to the following specifications: (i) the first row contains only titles, as strings; (ii) all other rows contain numerical or text data; and (iii) columns are homogeneous (i.e., not mixed numerical and text data). The interface should be as user-friendly, efficient, and intuitive as possible. Support the following functionality:

1. The table may have lots of rows, so provide either pagination or scrolling; it does not have lots of columns. Next to each row or data, display the original row number (with the header counting as row 0).
2. Preserving rows, allow for the table to be sorted (by a variety of methods of your choice) by a particular column; sorting methods should be appropriate for the column type.
3. Preserving rows, allow for the table to be filtered (by a variety of methods of your choice) by a particular column; filtering methods should be appropriate for the column type. Text filtering should include at least one wildcard-based (i.e., pattern matching) option.
4. Allow for multiple filters to be applied at once, but the interface need not allow for multiple-column sorting.
5. Display (in any manner) summary statistics for a selected column including, but not limited to count and range; for numerical columns, also display sum, arithmetic mean, and any other interesting statistics of your choice.
6. When hovering over a particular cell, identify its row number in the current display. When hovering over column names, identify the the column type and which filtering or sorting methods are currently being applied to the column.

Extra Credit: Allow for columns to be reordered, and to be added to or removed from the display. Also, augment the interface with any graphical visualizations you find interesting, useful, or appropriate.