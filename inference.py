"""
This script visualizes P(Infected|Test-positive) depending on the
prevalence P(Infected) and the specificity P(test-negative|not-infected)
"""

import matplotlib.pyplot as plt


def calculate_posterior(sensitivity, prevalence, specificity):
    p_not_infected = (1.0 - prevalence)
    p_testpos_given_notinfected = (1.0 - specificity)
    p_testpos = (sensitivity * prevalence) + (p_testpos_given_notinfected * p_not_infected)
    return _bayes_rule(likelihood=sensitivity, prior=prevalence, evidence=p_testpos)

def _bayes_rule(likelihood, prior, evidence):
    return ((likelihood * prior) / evidence)


if __name__ == "__main__":
    specificities = [0.99, 0.999, 0.9999, 0.99999]
    prevalences = list([i/100000 for i in range(1, 50001)])
    sensitivity = 0.99

    # for each specificity calculate prevalence for eeach prevalence value
    for specificity in specificities:
        p_values = [calculate_posterior(sensitivity, prevalence, specificity) for prevalence in prevalences]
        plt.plot(prevalences, p_values, label=f"specificity {specificity}")
    
    plt.legend()
    plt.xlabel("prevalence P(infected)")
    plt.ylabel("P(infected | test-positive)")
    plt.show()
