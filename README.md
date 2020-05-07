# expected-levenshtein

This repository contains empirically determined approximate expected [Levenshtein distances](https://en.wikipedia.org/wiki/Levenshtein_distance) between random strings over alphabets of different sizes, as well as simple python code to generate them.

## Dependencies

To use the code, you will need `numpy` and `numba`.

## Installing

Simply clone this repo:

```
git clone https://github.com/nickmachnik/expected-levenshtein.git
```

## Compute average levenshtein distances

To compute the approximate expected Levenshtein distances of random strings of lengths 1 ≤ lengths ≤ n, use `random_average_levenshtein` in `sample.py`.

This example shows how to compute the distances of random strings up to length 100 over a 4-letter alphabet, averaged over 1000 replicates.
```python
from sampling import random_average_levenshtein
import numpy as np

random_average_levenshtein(100, 1000, np.arange(4))
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