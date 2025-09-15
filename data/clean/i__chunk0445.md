# mse_1 = MSE(y_test2, pred_tree)

print('MSE of unpruned tree is', mse_1)

MSE of unpruned tree is 0.20923913043478262

Because the previous simple linear regression performs better, tree should be pruned

params = {"criterion":("gini", "entropy"),

"splitter":("best", "random"),

"max_depth":(list(range(1, 20))),

"min_samples_split":[2, 3, 4],

"min_samples_leaf":list(range(1, 20)),

}