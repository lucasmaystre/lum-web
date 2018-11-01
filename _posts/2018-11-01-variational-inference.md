---
title: Variational Inference
references:
  - author: D. Blei et al.
    title: "Variational Inference: A Review for Statisticians"
    year: 2016
    url: https://arxiv.org/abs/1601.00670
---

Let $\mathbf{z}$ be a vector of latent variables with prior distribution $p(\mathbf{z})$.
Consider a vector of observations $\mathbf{x}$ linked to the latent variables through the observation model $p(\mathbf{x} \mid \mathbf{z})$.
The central problem in Bayesian inference is the computation of the posterior distribution

$$
    \begin{align*}
    p(\mathbf{z} \mid \mathbf{x}) = \frac{p(\mathbf{x} \mid \mathbf{z}) p(\mathbf{z})}{p(\mathbf{x})}.
    \end{align*}
$$

A subproblem of interest is the computation of $\log p(\mathbf{x}) = \log \int p(\mathbf{x} \mid \mathbf{z}) p(\mathbf{z}) d\mathbf{z}$, known as the *marginal log-likelihood*.
This can be interpreted as the *evidence* for the model, and provides a principled way to perform model selection—i.e., to choose $p(\mathbf{z})$ and $p(\mathbf{x} \mid \mathbf{z})$.
In many models of interest (even models as simple as logistic regression), computing the posterior or the marginal log-likelihood is intractable.

*Variational inference* is a family of methods that attempt to approximate the posterior distribution by a simpler distribution (e.g., a multivariate Gaussian).
The key idea is to transform the computation of the posterior into an optimization problem.
Letting $\mathcal{Q}$ be a family of distributions (the *variational family*), the inference problem turns into the optimization problem

$$
    \begin{align*}
    \min_{q \in \mathcal{Q}} \ell(p(\mathbf{z} \mid x), q(\mathbf{z})),
    \end{align*}
$$

where $\ell$ is a functional that tells us how close $q(\mathbf{z})$ is to $p(\mathbf{z} \mid \mathbf{x})$.
Strictly speaking, any method that attempts to solve this problem should be called a "variational inference method", but usually what people refer to when using this term is $\ell(p, q) = \mathrm{KL}(q \Vert p)$.
There are two key advantages of optimizing this "reverse KL-divergence":

1. It is computationally tractable, and
2. it can be seen as maximizing a lower-bound of the marginal log-likelihood.

We can show this through a series of algebraic manipulations starting from the KL-divergence.

$$
    \begin{align*}
    \mathrm{KL}[q(\mathbf{z}) \Vert p(\mathbf{z} \mid \mathbf{x})]
        &= \mathbb{E}_{q} \left[ \log \frac{q(\mathbf{z})}{p(\mathbf{z} \mid \mathbf{x})} \right]
         = \mathbb{E}_{q} \left[ \log \frac{q(\mathbf{z}) p(\mathbf{x})}{p(\mathbf{x} \mid \mathbf{z}) p(\mathbf{z})} \right] \\
        &= \log p(\mathbf{x}) + \mathrm{KL}[q(\mathbf{z}) \Vert p(\mathbf{z})] - \mathbb{E}_{q}[\log p(\mathbf{x} \mid \mathbf{z})].
    \end{align*}
$$

Even though $\mathrm{KL}[q(\mathbf{z}) \Vert p(\mathbf{z} \mid \mathbf{x})]$ cannot be computed directly, we can optimize it via gradient descent.
The term $\mathrm{KL}[q(\mathbf{z}) \Vert p(\mathbf{z})]$ (which can be thought of as regularization term) and its derivative can often be computed in closed form.
The term $\mathbb{E}\_{q}[\log p(\mathbf{x} \mid \mathbf{z})]$ is more challenging, but can often be simplified.
In many important cases (e.g., Gaussan processes with non-conjugate observation models), the observations $\\{x_i\\}$ are independent and every observation depends on a single latent variable.
The term then simplifies to $\sum_i \mathbb{E}\_{q(z_i)}[\log p(x_i \mid z_i)]$, and can be computed efficiently by a sum of one-dimensional integrals.

Minimizing the reverse KL-divergence is equivalent to maximizing a lower bound on the marginal log-likelihood; this viewpoint comes from the fact that

$$
    \begin{align*}
    \log p(\mathbf{x})
        \ge \log p(\mathbf{x}) - \mathrm{KL}[q(\mathbf{z}) \Vert p(\mathbf{z} \mid \mathbf{x})]
        = \mathbb{E}_{q}[\log p(\mathbf{x} \mid \mathbf{z})] - \mathrm{KL}[q(\mathbf{z}) \Vert p(\mathbf{z})].
    \end{align*}
$$

An alternative way to obtain this result (one that is often mentioned in the literature) uses Jensen's inequality:

$$
    \begin{align*}
    \log p(\mathbf{x})
        &= \log \int p(\mathbf{x} \mid \mathbf{z}) p(\mathbf{z}) d\mathbf{z}
         = \log \int p(\mathbf{x} \mid \mathbf{z}) \frac{p(\mathbf{z})}{q(\mathbf{z})} q(\mathbf{z}) d\mathbf{z} \\
        &\ge \int \log \left[ p(\mathbf{x} \mid \mathbf{z}) \frac{p(\mathbf{z})}{q(\mathbf{z})} \right] q(\mathbf{z}) d\mathbf{z}
         = \mathbb{E}_{q}[\log p(\mathbf{x} \mid \mathbf{z})] - \mathrm{KL}[q(\mathbf{z}) \Vert p(\mathbf{z})].
    \end{align*}
$$
