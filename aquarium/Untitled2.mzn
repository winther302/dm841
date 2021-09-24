constraint forall(l in 1..b where y_black[l] == s \/ 
                                  x_black[1] == s)
         ((result[x_black[l], y_black[l]]) == 1 -> 
                                  result[x_black[l] +1, y_black[l]] == 2  \/
         (result[x_black[l], y_black[l]] == 2) -> 
                                  result[x_black[l], y_black[l]-1 ] == 1);