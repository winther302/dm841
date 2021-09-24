include "global_cardinality.mzn";
int: s;
set of int: size = 1..s;
array[size] of int: row_data;
array[size] of int: collum_data;
array[size,size] of int: box_data;
array[size,size] of var 0..1: result;

constraint forall(i in size)(global_cardinality([result[i,j]|j in size],[1],[row_data[i]]));
constraint forall(j in size)(global_cardinality([result[i,j]|i in size],[1],[collum_data[j]]));

constraint forall(i in 1..s-1, j in size where result[s-i,j] == 1)
                (forall(k in s-i..s, l in 1..s where box_data[s-i,j] == box_data[k,l])
                              (result[k,l] == 1));
solve satisfy;
output[show(result[i,j]) ++ if j == s then " \n" else " " endif| i,j in size]
