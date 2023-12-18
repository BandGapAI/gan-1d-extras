# 1-D Least-Squares Generative Adversarial Networks: optimal discriminators
## Reference: "Quasi-Analytical Least-Squares Generative Adversarial Networks: Further 1-D Results and Extension to Two Data Dimensions."

This repository (see [notebooks](notebooks))  contains Python implementations of the 1-D LS-GAN using an **optimal discriminator**. Note that these implementations are **not** quasi-analytical: the calculations for the cost function replace expectations by sample-based Monte Carlo estimates rather than Monte Carlo integrals.

By 1-D, it means that both the data $x$ and latent variable $z$ are 1-D random variables. The data are (scaled) exponential, and the latent variable is (scaled) Rayleigh.  The generator is $\hat{x}=G(x)=gz^2+h$ with $g>0$.

There are two different versions of this 1-D LS-GAN.
1. **Optimal discriminator** with $n_z = n_x = 1$ (section Sec IV-A of the paper): the discriminator is a scaled logistic function whose parameters are determined by those of the generator according to Proposition 1 of Goodfellow et al.'s 2014 paper on GANs. Note that this is a valid discriminator (continuous and differentiable) since the variable dimensions satisfy $n_z\geq n_x$. There are just 2 free parameters $(g,h)$. See [notebook](notebooks/optimal_discriminator.ipynb)
2. **Mistuned optimal discriminator** (section Sec IV-B of the paper): the discriminator is a scaled logistic function whose parameters $(a,b)$ are free. The functional form of the discriminator is the _same_ as the optimal discriminator (OD), but its parameters are _not_ the same as the OD: $$D(x)=\frac{1}{1+a\exp(-bx)}$$ This version therefore has 4 parameters $(a,b,g,h)$. See [notebook](notebooks/four_params.ipynb)
