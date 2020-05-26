# expected-levenshtein
![Python application](https://github.com/nickmachnik/expected-levenshtein/workflows/Python%20application/badge.svg)
![License](https://img.shields.io/github/license/nickmachnik/codon-degeneracy)
![PyPI version](https://badge.fury.io/py/expected-levenshtein.svg)

This repository contains empirically determined approximate expected [Levenshtein distances](https://en.wikipedia.org/wiki/Levenshtein_distance) between random strings over alphabets of different sizes, as well as simple python code to generate them.

## Dependencies

To use the code, you will need `numpy` and `numba`.

## Installing

Simply clone this repo:

```
git clone https://github.com/nickmachnik/expected-levenshtein.git [TARGET DIR]
```

and then install  via pip
```
pip install [TARGET DIR]
```

## Testing

Test the cloned package:
```
cd [TARGET DIR]
python -m unittest
```

## Geting started

### Computing average levenshtein distances

To compute the approximate expected Levenshtein distances of random strings of lengths 1 ≤ lengths ≤ n, use `random_average_levenshtein` in `sample.py`.

This example shows how to compute the distances of random strings up to length 100 over a 4-letter alphabet, averaged over 1000 replicates.
```python
from sample import random_average_levenshtein
import numpy as np

random_average_levenshtein(100, 1000, np.arange(4))
```

### Generating models for expected distances

For long sequences, the distance matrix returned by `random_average_levenshtein` can get quite large.
If you prefer not to load and query a large matrix object every time you need an expected distance,
`fit.model_average_levenshtein` generates a polynomial model for each row in
the distance matrix. That way, the information that needs to be stored to compute approximate
expected levenshtein distances is reduced to the coefficients of the polynomials. Once computed,
these can be used to predict expected distances with `fit.poly`.

This example shows how to generate and use such models for random strings from length 25 to length 50.
```python
from sample import random_average_levenshtein
from fit import poly, model_average_levenshtein
import numpy as np

# sample distances
average_distances = random_average_levenshtein(50, 1000, np.arange(4))

# make models
row_indices, coefficients, mean_squared_deviations = model_average_levenshtein(
    average_distances, model_rows=np.arange(25, 51))

# predict expected distance for n=50, m=44
coeff_n_50 = coefficients[-1]
predicted_expected_distance = poly(44, coeff_n_50)
```

## License

MIT license ([LICENSE](LICENSE.txt) or https://opensource.org/licenses/MIT)

<!-- 
End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

 -->