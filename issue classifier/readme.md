Issue Classifier
------------------------
For a given issue suggest labels

### History
Mined around `` issue-label pair from Github open-source reporistories.

#### Experiment - 1: train a model on standard issue. Dataset has following stats
```json
{
    enhancement: 75436,
    bug: 36017,
    question: 8082,
    'help wanted': 3173,
    wontfix: 627
    duplicate: 299,
    invalid: 236,
}
```

1. Training with {max 2000} entries in each category and using remaining for verification.
    - `svm` - Accuracy with SVM: 43.85%
    - by reducing labels to first four accuracy increased to - 43.957701%
```md
Dataset
------------------
enhancement: 2000,
question: 2000,
bug: 2000,
'help wanted': 2000,
duplicate: 299,
invalid: 236,
wontfix: 627
Testset
---------------------
enhancement: 73436,
bug: 34017,
question: 6082,
'help wanted': 1173
  ```

2. Training with {max: 3000} entries in each category and using remaining for verification.
    - with `svm` and first four labels - `44.570401% on testset` and `82.428218% on dataset`


Note: project requires `numpy`, `scipy` & `sklearn`