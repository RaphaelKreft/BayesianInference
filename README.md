# BayesianInference
This Repo contains the solution to some funny tasks regarding Bayesian Inference and  statistics.


## Task 1

The company Fränzi and Friends developed a new quick test at home for SARS-Cov-2 which is pending regulatory agency’s review. The test has been shown to have a sensitivity of 99% and a specificity of 99%. Suppose that Fred uses the test by Fränzi and Friends and the test was positive. Assume that 5% of the population is in fact infected. Was is your guess about the probability that Fred is indeed infected?

### Solution

To solve this Task you first need to clarify what the Terms sensitivity and specificity mean!

**sensitivity:** Is the probability, that given, a person is positive, the test will be positive (ex. sensitivity = 99%: If 100 people are infected, the test will be positive for 99 of them)

**specificity:** the ability of a test to correctly identify people without the disease, so the probability, that the test is negative given a person is negative(ex. specificity = 99%: If 100 people are not infected, the test will be negative in 99 cases).

In this Task we basically want to calculate **P(Infected|Test-positive)**. 
We know that our sensitivity P(Test-positive | infected) = 0.99 and that our specificity P(Test-negative|not-infected) = 0.99, furthermore we know that the prevalence P(Infected) = 0.05.

We can figure out **P(Infected|Test-Positive)** using Bayes Rule:
```
P(Infected|Test-Positive) = P(test-positive|Infected) * P(Infected) / P(Test-positive)
```

The missing value **P(test-positive)** can be obtained like this:
```
P(test-positive) = P(Test-positive|Infected) * P(Infected) + P(test-positive|not-infected) * P(not-infected)
```

- `P(Test-positive|Infected) * P(Infected) = 0.99 * 0.05 = 0.0495`
- `P(not-infected) = 1 - P(infected) = 0.95`
- `P(test-positive|not-infected) = 1 - specificity = 0.01`

Plugging in these values in bayes rule we get:
```
P(Infected|Test-Positive) = P(test-positive|Infected) * P(Infected) / P(Test-positive) = 0.0495 / (0.0495 + (0.01 * 0.95)) = 0.8389
```

**The result is 0.8389. This means that out of 100 people tested positive, just 83,89 people really have the infection.**


## Task 2 - Simulation

Please share a piece of code that visualizes the probability that **Fred is indeed infected as the dependent variable**, with the **infection prevalence** (5% in the example above, which takes any real-number value between 0.001% to 50%) **and the specificity** (99% in the example above, which takes values 99%, 99.9%,99.99%, and 99.999%) **as independent variables**. For simplicity, we fix the sensitivity at 99%. Visualize the results if possible, and use integers to check and explain your results. Use any programming language that you prefer. Please put your code in GitHub or GitLab or other code-hosting service and paste the link below. 

### Solution

The code for the simulation can be found in this repo and can be used like so:

1. make sure matplotlib is installed on the system.
2. run script with `python inference.py`

I also added the result graphics to the repo in case you cannot execute the program.