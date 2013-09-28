"""
Run SMC on the simple model.

Author:
    Ilias Bilionis

Date:
    9/28/2013

"""


import simple_model as model
import pymc
import pysmc
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Construct the MCMC sampler
    mcmc_sampler = pymc.MCMC(model)
    # Construct the SMC sampler
    smc_sampler = pysmc.SMC(mcmc_sampler, num_particles=1000,
                            num_mcmc=10, verbose=1)
    # Initialize SMC at gamma = 0.01
    smc_sampler.initialize(0.01)
    # Move the particles to gamma = 1.0
    smc_sampler.move_to(1.0)
    # Get the weights of each particle
    w = smc_sampler.weights
    # Get the particles pertaining to the mixture
    x = smc_sampler.get_particles_of('mixture')
    # Plot a histogram
    plt.hist(x, weights=w, bins=100, normed=True)
    plt.xlabel('$x$', fontsize=16)
    plt.ylabel('$p(x)$', fontsize=16)
    plt.show()